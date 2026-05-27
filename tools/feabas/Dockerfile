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

FROM python:3.10.14
LABEL maintainer="Hannah Martinez <hannah.martinez@jhuapl.edu>"

ENV PATH=/usr/local/bin:$PATH
ENV PYTHON_VERSION=3.10.14

# dev setup
RUN apt update && \
    apt-get install sudo git s3fs gcc pkg-config libhdf5-dev ffmpeg libsm6 libxext6 -yqq && \
    pip install --upgrade --no-cache-dir pip && \
    apt-get clean

# Install
WORKDIR /opt
RUN git clone https://github.com/YuelongWu/feabas.git
WORKDIR /opt/feabas
RUN git checkout 90a42c4
RUN pip install -e .
