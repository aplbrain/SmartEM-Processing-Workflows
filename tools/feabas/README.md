# Running Containerized FEABAS

This directory containerizes [FEABAS](https://github.com/YuelongWu/feabas), the stitching and alignment algorithm based on finite-element analysis.

## Requirements
* Docker
* Tiled images in PNG or TIF format

## Setup
All the setup that is required is to create a working directory which contains a specific directory structure with configuration files and your tiled images. 

Here we have included the configuration files we used to stitch and align the SmartEM mouse dataset.

We recommend following the instructions in the [FEABAS readme](https://github.com/YuelongWu/feabas?tab=readme-ov-file#preparation) to determine how to structure the working directory and how to customize the configuration files. Generating the stitch coordinate files will likely require the most work. You should create the working directory on the local machine and mount it into the container at runtime so that the results are persisted.

Finally, build the Docker container. 
```
sudo docker build . -t feabas:latest
```

## Running
Below are linked the documentation sections for running stitching and alignment. Follow the instructions in each section to accomplish the respective task. To run with Docker, prepend each command with the following. 
```
sudo docker run feabas -v /path/to/local/working/dir:/working_dir
```
The final argument will mount the working directory you created into the Docker container at container path `/working_dir`. You will need to ensure that your configuration files and stitch coord files reflect the paths inside the Docker container, not the paths on your local machine.

So, the first command would be:
```
sudo docker run feabas -v /path/to/local/working/dir:/working_dir \
python scripts/stitch_main.py --mode matching
```
And so on.

### Stitching
https://github.com/YuelongWu/feabas?tab=readme-ov-file#stitching

### Thumbnail Alignment
https://github.com/YuelongWu/feabas?tab=readme-ov-file#thumbnail-alignment

### Fine Alignment
https://github.com/YuelongWu/feabas?tab=readme-ov-file#fine-alignment