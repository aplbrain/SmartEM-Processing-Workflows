"""
Copyright © 2026 The Johns Hopkins University Applied Physics Laboratory LLC

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to
deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import numpy as np
import h5py
from cloudvolume import CloudVolume
import os

# This file serves as an example for downloading a chunk of data for testing the FFN image
# Start by filling out the Configuration section
# Then run:
#   python download_training_data.py

# ---------------------- Configuration ----------------------

# Replace these with your paths
# s3://path/to/em and s3://path/to/segmentation
# This can also be a local path or cloud path on a different provider
# See cloud-volume docs for more examples
IMAGE_PRECOMP_PATH = 's3://bossdb-open-data/meirovitch2025/composite_dwell_time/composite_em'
LABEL_PRECOMP_PATH = 's3://bossdb-open-data/meirovitch2025/composite_dwell_time/composite_3dseg'

# Desired bounding box in XYZ
# This example is small for demo purposes
# FFN recommends 150 Mvx of annotated ground truth for training
CROP_SIZE_XYZ = [700, 700, 94]  # in voxels
# Define the start of your bounding box (e.g., (0, 0, 0) or custom offset)
BBOX_START_XYZ = [21224/2, 13843/2, 0]

# Output HDF5 paths
OUTPUT_IMAGE_H5 = 'image_volume.h5'
OUTPUT_LABEL_H5 = 'label_volume.h5'

# Dataset names inside HDF5 files
H5_IMAGE_DATASET = 'raw'
H5_LABEL_DATASET = 'labels'

# Uint16 Clamping values
UINT16_MIN = 0
UINT16_MAX = 52221
# ---------------------- Load Volumes ----------------------

def load_cloudvolume_data(path, bbox_start_xyz, crop_size_xyz, mip=0):
    vol = CloudVolume(path, progress=True, use_https=True, mip=mip)
    bbox_end_xyz = [s + c for s, c in zip(bbox_start_xyz, crop_size_xyz)]

    # CloudVolume slicing: [X, Y, Z]
    start_xyz = bbox_start_xyz
    end_xyz = bbox_end_xyz

    data = vol[start_xyz[0]:end_xyz[0], start_xyz[1]:end_xyz[1], start_xyz[2]:end_xyz[2]]
    return np.squeeze(np.asarray(data))


# Load data
print("Downloading image data...")
image_data = load_cloudvolume_data(IMAGE_PRECOMP_PATH, BBOX_START_XYZ, CROP_SIZE_XYZ, mip=1)

print("Downloading label data...")
label_data = load_cloudvolume_data(LABEL_PRECOMP_PATH, BBOX_START_XYZ, CROP_SIZE_XYZ, mip=0)

# ---------------------- Compute Stats ----------------------

image_mean = float(np.mean(image_data))
image_stddev = float(np.std(image_data))

print(f"Image mean: {image_mean:.4f}")
print(f"Image stddev: {image_stddev:.4f}")

# ---------------------- Save to HDF5 ----------------------

# Transpose data before saving, as FFN expects ZYX
def save_h5(data, filepath, dataset_name):
    with h5py.File(filepath, 'w') as f:
        f.create_dataset(dataset_name, data=np.transpose(data), compression='gzip')
    print(f"Saved {dataset_name} to {filepath}")


# Save image and label volumes
save_h5(image_data, OUTPUT_IMAGE_H5, H5_IMAGE_DATASET)
save_h5(label_data, OUTPUT_LABEL_H5, H5_LABEL_DATASET)
