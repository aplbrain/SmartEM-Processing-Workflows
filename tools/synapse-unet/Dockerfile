# Copyright © 2026 The Johns Hopkins University Applied Physics Laboratory LLC

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
# IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Based on cuda ready nvidia image
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

# Remove CPU-only
RUN pip uninstall -y torch torchvision || true

# Install CUDA-enabled PyTorch
RUN pip install --no-cache-dir \
    torch==2.6.0 torchvision==0.21.0 \
    --index-url https://download.pytorch.org/whl/cu118