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

path = "file://../../example_working_dir/meirovitch2025/aligned_tensorstore"
output_path = "../../example_working_dir/meirovitch2025/aligned_tensorstore.h5"

vol = CloudVolume(path, progress=True, fill_missing=True)
image_data = vol[:, :, :]

# Transpose data before saving, as FFN expects ZYX
def save_h5(data, filepath, dataset_name):
    with h5py.File(filepath, 'w') as f:
        f.create_dataset(dataset_name, data=np.transpose(data), compression='gzip')
    print(f"Saved {dataset_name} to {filepath}")


# Save image volume
save_h5(image_data, output_path, "raw")
