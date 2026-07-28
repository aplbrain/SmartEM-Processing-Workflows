# Running Containerized Vsvi2Precomputed 

This directory containerizes [vsvi2precomputed](https://github.com/aplbrain/vsvi2precomputed), an APL tool built for converting VAST datasets to precomputed format. It supports conversion of both local and AWS-hosted datasets to both local and AWS-hosted locations.

## Requirements
* Docker
* Image volume in VSVI format

## Setup

If you are planning to upload or download a dataset from AWS, you will need to obtain an AWS access key. Here is some documentation: https://docs.aws.amazon.com/sdkref/latest/guide/feature-static-credentials.html

Build the Docker container. 
```
docker build . -t vsvi2precomputed:latest
```

## Running

Convert a dataset locally:
```
docker run vsvi2precomputed -v /path/to/local/working/dir:/working_dir \
    --i /working_dir/path/to/config.vsvi --o /working_dir/path/to/output/dir/
```

Convert a dataset and upload it to an S3 location:
```
docker run vsvi2precomputed -v /path/to/local/working/dir:/working_dir \
    -e AWS_ACCESS_KEY_ID=<your-access-key> \
    -e AWS_SECRET_ACCESS_KEY=<your-secret-key> \
    -e AWS_DEFAULT_REGION=us-east-1 \
    --i /working_dir/path/to/config.vsvi --o s3://path/to/output/dir/
```