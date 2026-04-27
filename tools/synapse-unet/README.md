# Running Synapse Unet on Docker

This Dockerfile is based on PyTorch Connectomics, commit [f29a6bf](https://github.com/PytorchConnectomics/pytorch_connectomics/tree/f29a6bf71b2d82171392a6b69cec37fa6c898f92).

## Requirements
* Hardware or cloud resources with one or more Nvidia GPUs
* Docker
* A working directory
* An aligned EM image volume, and labeled training data
  * TODO: Input format unknown...

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

## Training
Coming soon

## Inference

1. Run inference on a single block.
```
docker run --rm \
--gpus all \
-v /path/to/working_dir:/working_dir \
ffn \
python run_inference.py   --inference_request="$(cat inference_config_example.pbtxt)"   --bounding_box 'start { x:0 y:0 z:0 } size { x:250 y:250 z:250 }'
```