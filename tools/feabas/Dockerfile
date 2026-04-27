FROM python:3.10.14

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
RUN pip install -e .