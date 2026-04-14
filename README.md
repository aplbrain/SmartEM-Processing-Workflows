# SmartEM-Processing-Workflows

A Dockerized, step-by-step processing pipeline designed to take electron microscopy (EM) images from SmartEM and transform them into connectome-ready outputs using a reproducible, modular, and scalable approach.

## Key Features

* **Dockerized tools** for reproducibility and portability
* **Modular workflows** that can be composed and extended
* **End-to-end processing** from SmartEM outputs to connectome generation
* **Scalable design** suitable for local, cluster, or cloud execution

Tools included:
* Stitching
* Alignment
* Dense neuron segmentation
* Synapse detection
* Conversion to precomputed format
* Upload to the cloud

## Getting Started

### Prerequisites

* Docker (>= 20.x)
* Git
* Tiled EM images in TIF or PNG format

### Clone the Repository

```
git clone https://github.com/<your-org>/SmartEm-Processing-Workflows.git
cd SmartEm-Processing-Workflows
```

### Build Docker Images

Navigate to a specific Dockerfile and build the image:

```
cd dockerfiles/<example-step>
docker build -t smartem/<example-step>:latest .
```


## Running Workflows

Workflows are defined in the `workflows/` directory and are responsible for chaining together multiple Dockerized steps.

Example:

```
cd workflows/<example-workflow>
./run.sh
```

Each workflow will document:

* Required inputs
* Expected outputs
* Configuration parameters


## Contact

For questions or collaboration inquiries, please email hannah.martinez@jhuapl.edu, caitlyn.bishop@jhuapl.edu, or daniel.xenes@jhuapl.edu.

