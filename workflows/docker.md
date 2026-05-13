# Running an end-to-end pipeline with Docker

We recommend pairing Docker with a mounted working directory for an interactive workflow because it enables parameter tuning and inspection of intermediate products. This pipeline covers:
* Stitching
* Alignment
* Segmentation
* Synapse detection

You will need:
* A machine with a GPU 
* Docker
* uv
* A working directory with unstitched, unaligned image tiles. Example data is provided in the meirovitch2025 entry in BossDB's cloud storage:
```
cd SmartEM-Processing-Workflows/example_working_dir/meirovitch2025
wget https://s3.us-east-1.amazonaws.com/bossdb-open-data/meirovitch2025/workflow_example_data/tiles.tar.gz
tar -xvzf tiles.tar.gz
```

Briefly, each step will require
* Building the Docker container
* Mounting the working directory so that results are persisted to disk
* Running the commands as documented
* Inspecting the output, adjusting configuration, and repeating as necessary

There will be a few scripts and notebooks that can be run using uv, rather than Docker. Create the `.venv` to use these.
```
uv sync
```

Following is a step by step guide to complete the full workflow.

## Stitching and alignment
For FEABAS it is highly recommended to read the [FEABAS README](https://github.com/YuelongWu/feabas/blob/master/README.md) first. There you will find context for the structure of the working directory and each of the commands that need to be run. 

First, create and populate the working directory. You will need a `stitch/` directory that contains the stitching coordinate files that point to your data (example data is available for download using the `wget` command above) and a `configs/` directory that contains the configurations. In this tutorial, we have created a working directory at `/example_working_dir/meirovitch2025` that is set up for you.

Next, build the Docker container.
```
cd tools/feabas
sudo docker build . -t feabas:latest
```

Finally, in [tools/feabas/README.md#Running](https://github.com/aplbrain/SmartEM-Processing-Workflows/tree/main/tools/feabas#running), we provide instructions for running each step in the stitching and alignment pipeline. We recommend moving to that page and coming back to this one when the aligned stack has been created. At two intermediate points in the pipeline flagged `--rendering`, the algorithm progress can be inspected. We recommend inspecting at each of these points and adjusting configurations as needed.

The output of FEABAS will be a folder called `aligned_tensorstore` which contains a precomputed volume of stitched and aligned data. Use `tools/feabas/view_data.ipynb` to examine it before moving on to segmentation:
```
uv sync
uv run --with jupyter jupyter lab
```
Then open the notebook, and for the kernel, use "Existing Jupyter Server" with the URL that was printed in the terminal. It should be formatted as http://localhost:8888/lab?token=<token>.

## Segmentation
First, you will need to convert the precomputed output of FEABAS to an H5 file.
```
cd tools/ffn
uv run convert_to_h5.py
```
Then, follow the instructions in the [tools/ffn README](https://github.com/aplbrain/SmartEM-Processing-Workflows/blob/main/tools/ffn/README.md) to run inference on the volume. You will need to edit line 2 of `tools/ffn/inference_config_example.pbtext` to point to `example_data/meirovitch2025/aligned_tensorstore.h5`.

To use the `tools/ffn/view_data.ipynb` notebook to view results, you will need the same jupyter setup as in the FEABAS section above.

## Synapse detection

