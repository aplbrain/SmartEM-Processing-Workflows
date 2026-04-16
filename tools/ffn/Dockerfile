FROM tensorflow/tensorflow:2.17.0-gpu

RUN apt-get update && apt-get install -y git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/google-research/connectomics.git \
    && cd connectomics/ \
    && git checkout c65e963ad9d803bf66331de123624a8e31b1aac6 \
    && pip install . \
    && cd ..

RUN git clone https://github.com/aplbrain/ffn.git

WORKDIR /ffn

RUN pip install protobuf==3.20.* \
    absl-py==2.1.0 \
    numpy==1.26.4 \
    jax \
    tensorstore==0.1.65 \
    tf-slim
