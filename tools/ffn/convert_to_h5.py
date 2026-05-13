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
