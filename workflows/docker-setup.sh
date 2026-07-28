#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
REPO_ROOT=$(cd -- "$SCRIPT_DIR/.." && pwd)
WORKING_DIR="$REPO_ROOT/example_working_dir/meirovitch2025"

TILES_URL="https://s3.us-east-1.amazonaws.com/bossdb-open-data/meirovitch2025/workflow_example_data/tiles.tar.gz"

log() {
  printf '[docker-build] %s\n' "$*"
}

require_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    printf 'Missing required command: %s\n' "$1" >&2
    exit 1
  fi
}

download_file() {
  local url=$1
  local output=$2

  if command -v wget >/dev/null 2>&1; then
    wget -O "$output" "$url"
  elif command -v curl >/dev/null 2>&1; then
    curl -L "$url" -o "$output"
  else
    printf 'Missing required command: wget or curl\n' >&2
    exit 1
  fi
}

ensure_archive_extracted() {
  local archive_name=$1
  local extract_target=$2
  local url=$3
  local archive_path="$WORKING_DIR/$archive_name"

  if [ -e "$WORKING_DIR/$extract_target" ]; then
    log "Found $extract_target; skipping download"
    return
  fi

  if [ ! -f "$archive_path" ]; then
    log "Downloading $archive_name"
    download_file "$url" "$archive_path"
  else
    log "Found $archive_name; reusing existing archive"
  fi

  log "Extracting $archive_name"
  tar -xzf "$archive_path" -C "$WORKING_DIR"
}

build_image() {
  local context_dir=$1
  local image_tag=$2

  log "Building $image_tag from $context_dir"
  docker build -t "$image_tag" "$context_dir"
}

require_cmd tar
require_cmd docker
require_cmd uv

if [ ! -d "$WORKING_DIR" ]; then
  printf 'Expected working directory not found: %s\n' "$WORKING_DIR" >&2
  exit 1
fi

ensure_archive_extracted "tiles.tar.gz" "tiles" "$TILES_URL"

log "Syncing uv environment at $REPO_ROOT"
(
  cd "$REPO_ROOT"
  uv sync
)

build_image "$REPO_ROOT/tools/feabas" "feabas:latest"
build_image "$REPO_ROOT/tools/ffn" "ffn:latest"
build_image "$REPO_ROOT/tools/synapse-unet" "synapse-unet:latest"
build_image "$REPO_ROOT/tools/vsvi2precomputed" "vsvi2precomputed:latest"

log "Setup complete"
