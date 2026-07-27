# Running FFN on Docker

This Dockerfile is based on the [JHU/APL fork](https://github.com/aplbrain/ffn) of Google's flood-filling networks segmentation algorithm.

## Requirements
* Hardware or cloud resources with one or more Nvidia GPUs
* Docker
* A working directory
* An aligned EM image volume. 
  * FFN expects a 3D H5 file
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

4. Build the Docker image from source.
```
docker build -t ffn:latest .
```

5. Copy images to a working directory. We have provided an example image at `example_working_dir/meirovitch2025/image_volume.h5`.

## Training
Coming soon

## Inference
1. Write a configuration file. We have provided an example at `inference_config_example.pbtxt`. You will at minimum need to change the paths within this file to point to those in your working directory. We recommend mounting the working directory to the root of the Docker container (as shown in the following command) and have done so in our example.

    More examples are found in the [ffn configs directory](https://github.com/aplbrain/ffn/tree/master/configs) and guidance is found in the [ffn docs](https://github.com/aplbrain/ffn/blob/master/doc/manual.md#segmentation-inference).

2. Run inference on a single block.
```
docker run --rm \
--gpus all \
-v /path/to/working_dir:/working_dir \
ffn \
python run_inference.py   --inference_request="$(cat inference_config_example.pbtxt)"   --bounding_box 'start { x:0 y:0 z:0 } size { x:250 y:250 z:250 }'
```

3. Use the provided notebook `view_data.ipynb` to inspect the results.
```
uv sync
uv run --with jupyter jupyter lab
```
Then open the notebook, and for the kernel, use "Existing Jupyter Server" with the URL that was printed in the terminal. It should be formatted as http://localhost:8888/lab?token=<token>.