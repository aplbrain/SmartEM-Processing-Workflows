# Running Containerized FEABAS

This directory containerizes [FEABAS](https://github.com/YuelongWu/feabas), the stitching and alignment algorithm based on finite-element analysis.

## Requirements
* Docker
* Tiled images in PNG or TIF format

## Setup
All the setup that is required is to create a working directory which contains a specific directory structure with configuration files and your tiled images. 

We recommend following the instructions in the [FEABAS readme](https://github.com/YuelongWu/feabas?tab=readme-ov-file#preparation) to determine how to structure the working directory and how to customize the configuration files (default ones are included in this directory). Generating the stitch coordinate files will likely require the most work. You should create the working directory on the local machine and mount it into the container at runtime so that the results are persisted. Be sure to generate the files so that they are in order when sorted alphabetically, as this is the order in which they will be stacked.

In `example_working_dir/meirovitch2025` we have set up an example which already includes the `configs/` that were used for the SmartEM paper and `stitch/` directory for a subset of SmartEM data. However, the subsetted data (530 MB) still remains to be downloaded. 

```
cd SmartEM-Processing-Workflows/example_working_dir/meirovitch2025
wget https://s3.us-east-1.amazonaws.com/bossdb-open-data/meirovitch2025/workflow_example_data/tiles.tar.gz
tar -xvzf tiles.tar.gz
```

Finally, build the Docker container. 
```
sudo docker build . -t feabas:latest
```

## Running
Below are linked the documentation sections for running stitching and alignment. Follow the instructions in each section to accomplish the respective task. To run with Docker, prepend each command with the following. 
```
docker run -v /path/to/local/working/dir:/working_dir \
-v /path/to/local/working/dir/configs/general_configs.yaml:/opt/feabas/configs/general_configs.yaml \
feabas
```
The final argument will mount the working directory you created into the Docker container at container path `/working_dir`. You will need to ensure that your configuration files and stitch coord files reflect the paths inside the Docker container, not the paths on your local machine.

So, the first command would be:
```
docker run -v /path/to/local/working/dir:/working_dir \
-v /path/to/local/working_dir/configs:/opt/feabas/configs \
feabas \
python scripts/stitch_main.py --mode matching
```
And so on.

### Stitching
https://github.com/YuelongWu/feabas?tab=readme-ov-file#stitching

### Thumbnail Alignment
https://github.com/YuelongWu/feabas?tab=readme-ov-file#thumbnail-alignment

### Fine Alignment
When you get to the rendering step, choose `--tsr` instead of `--rendering`.

https://github.com/YuelongWu/feabas?tab=readme-ov-file#fine-alignment

## Visualizing

Use the included notebook `view_data.ipynb` to view the data. 
```
uv sync
uv run --with jupyter jupyter lab
```
Then open the notebook, and for the kernel, use "Existing Jupyter Server" with the URL that was printed in the terminal. It should be formatted as http://localhost:8888/lab?token=<token>.

As a shortcut, we have uploaded the result of running this workflow to the cloud (385 MB).
```
cd SmartEM-Processing-Workflows/example_working_dir/meirovitch2025
wget https://s3.us-east-1.amazonaws.com/bossdb-open-data/meirovitch2025/workflow_example_data/aligned_tensorstore.tar.gz
tar -xvzf aligned_tensorstore.tar.gz
```
