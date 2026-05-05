# Based on cuda ready nivdia image
FROM nvidia/cuda:11.3.1-base-ubuntu20.04
  
# Update the package manger and install base functions
RUN apt-get update && apt-get install -y wget unzip curl bzip2 git libgl1

# Install and setup miniconda
RUN curl -LO http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash Miniconda3-latest-Linux-x86_64.sh -p /miniconda -b
RUN rm Miniconda3-latest-Linux-x86_64.sh
ENV PATH=/miniconda/bin:${PATH}

# Accept Anaconda Terms of Service (required for non-interactive builds)
RUN conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main \
 && conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r

# Update conda, add dependencies
RUN conda update -y conda && conda install -y python=3.10 pytorch torchvision

# We do not require a conda environment since the container is allready isolated
# However, we switch user to not install pip packges as root
RUN useradd -ms /bin/bash pytc
ENV PATH="/home/pytc/.local/bin:${PATH}"
USER pytc

# Setup and install the git repo
WORKDIR /home/pytc/
RUN cd /home/pytc/ && git clone https://github.com/zudi-lin/pytorch_connectomics.git
RUN pip install --upgrade pip setuptools==59.5.0
RUN cd pytorch_connectomics && \
    git checkout f29a6bf && \
    pip install --upgrade pip && \
    pip install --editable . && \
    pip install numpy==1.26.4