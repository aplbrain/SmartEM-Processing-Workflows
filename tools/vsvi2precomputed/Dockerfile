FROM python:3.13
LABEL maintainer="Hannah Martinez <hannah.martinez@jhuapl.edu>"

# Install
WORKDIR /opt
RUN git clone https://github.com/aplbrain/vsvi2precomputed.git
WORKDIR /opt/vsvi2precomputed
RUN pip install -e .

# Base command
ENTRYPOINT ["python", "vsvi2precomputed.py"]