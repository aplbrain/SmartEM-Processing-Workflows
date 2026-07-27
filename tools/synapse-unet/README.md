# Running Synapse Unet on Docker

This Dockerfile is based on PyTorch Connectomics, commit [f29a6bf](https://github.com/PytorchConnectomics/pytorch_connectomics/tree/f29a6bf71b2d82171392a6b69cec37fa6c898f92).

## Requirements
* Hardware or cloud resources with one or more Nvidia GPUs
* Docker
* A working directory
* An aligned EM image volume, and labeled training data
  * PyTorch Connectomics expects a 3D H5 file
  * In `example_working_dir/meirovitch2025`, we provide a pre-downloaded test volume
  * We also provide a script `download_training_data.py` for downloading a precomputed volume and converting to the correct format

## Setup
1. Ensure that Nvidia drivers are installed on the machine so that the GPU can be used. If nothing is printed from the following command, you will need to install the appropriate drivers for your OS.
```
nvidia-smi
```

2. Install `nvidia-container-toolkit`. Installation guide can be found on [Nvidia's website](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).

3. Run the following commands to expose the GPU to Docker:
```
nvidia-ctk runtime configure --runtime=docker
systemctl restart docker
```

4. Build the Docker container.
```
docker build -t synapse-unet:latest .
```

5. Copy images to a working directory. We have provided an example image at `example_working_dir/meirovitch2025/image_volume.h5`.

## Training
Coming soon

## Inference

1. Pre-trained weights and yaml config files can be found in `example_working_dir/meirovitch2025/synapse_unet_configs`. We recommend mounting the working directory to the root of the Docker container (as shown in the following command) and have done so in our example. You will need to open the yaml config files and update the paths to route within the Docker container, not on your local machine.

2. Run inference on a single block.
```
docker run --rm \
--gpus all \
-v /path/to/working/dir:/working_dir \
synapse-unet \
python -u /home/pytc/pytorch_connectomics/scripts/main.py \
--config-base /working_dir/nk_mouse.yaml \
--config-file /working_dir/nk_mouse_unet.yaml \
--inference \
--checkpoint /working_dir/nk_mouse_synapse_network.tar
```

3. Use the provided notebook `view_data.ipynb` to view the results.
```
uv sync
uv run --with jupyter jupyter lab
```
Then open the notebook, and for the kernel, use "Existing Jupyter Server" with the URL that was printed in the terminal. It should be formatted as http://localhost:8888/lab?token=<token>.

## Troubleshooting

The Dockerfile installs Torch and Torchvision versions that align with Cuda 11.8. If the first line printed does not include `device: cuda`, you may need to troubleshoot the container's versions to align with your host machine's drivers.