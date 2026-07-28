# Meirovitch2025 Example Working Directory

The configurations for running this repository on the [data](https://doi.org/10.60533/boss-2023-4w35) from the [Meirovitch et al., 2025 paper](https://doi.org/10.1038/s41592-025-02929-3) are provided here in the form of an example working directory.

Use this directory as the mounted workspace for the dockerized `tools/`.

For the broader pipeline overview, see the repository [README](../../README.md) and the end-to-end Docker walkthrough in [workflows/docker.md](../../workflows/docker.md).

## What is included

- `configs/`
  FEABAS configuration bundle for stitching, thumbnail alignment, fine alignment, and tensorstore rendering.
- `stitch/stitch_coord/`
  Stitch coordinate files for five z slices. These files expect the image tiles to exist under `/meirovitch2025/tiles/...` inside the FEABAS container.
- `image_volume.h5`
  Example EM volume for Synapse U-Net inference.
- `image_volume_uint8.h5`
  Canonical ZYX uint8 EM volume used to prepare the FFN input.
- `image_volume_legacy.h5`
  XYZ-ordered and transposed uint8 EM volume used by the tuned legacy-axis FFN checkpoint. Used for testing FFN container as a standalone.
- `label_volume.h5`
  RGB-encoded instance labels used to score FFN output.
- `ffn_results/`
  Tuned FFN segmentation and its adapted Rand, variation-of-information, and
  coverage metrics, plus a PNG comparison against the EM and ground truth.
  See [`tools/ffn/README.md`](../../tools/ffn/README.md) for reproduction and
  scoring commands.
- `synapse_unet_configs/`
  Pretrained Synapse U-Net weights plus example YAML configs.

## What you still need to download

If you want to run FEABAS from raw tiles, download the example tiles (530 MB):

```bash
cd SmartEM-Processing-Workflows/example_working_dir/meirovitch2025
wget https://s3.us-east-1.amazonaws.com/bossdb-open-data/meirovitch2025/workflow_example_data/tiles.tar.gz
tar -xvzf tiles.tar.gz
```
This will download a set of 1768x2048 tiles, each with a resolution of 4nm per pixel. The set is 4 tiles by 4 tiles by 5 slices large for a total of 80 tiles. The thickness of each slice is 30 nm. These tiles serve as the input to FEABAS, which will stitch and align them into a single volume.

If you only want to inspect or reuse a pre-rendered aligned volume, download the published tensorstore output instead (385 MB):

```bash
cd SmartEM-Processing-Workflows/example_working_dir/meirovitch2025
wget https://s3.us-east-1.amazonaws.com/bossdb-open-data/meirovitch2025/workflow_example_data/aligned_tensorstore.tar.gz
tar -xvzf aligned_tensorstore.tar.gz
```
This will download a precomputed volume of size 7168x6272x5 voxels at resolution 4x4x30 nm.
