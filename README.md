# SmartEM-Processing-Workflows

A Dockerized, step-by-step processing pipeline designed to take electron microscopy (EM) images from SmartEM and transform them into connectome-ready outputs (e.g., segmentation, synapse detection) using a reproducible, modular, and scalable approach.

SmartEM is a novel EM imaging approach which allows for intelligent, data-aware imaging of specimens. Please read [the paper](https://doi.org/10.1038/s41592-025-02929-3) for details on the method and visit [the BossDB project page](https://doi.org/10.60533/boss-2023-4w35) to view and download SmartEM datasets.

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

Build all the images:

```
./workflows/docker-setup.sh
```


## Running Workflows

Workflows are defined in the `workflows/` directory and are responsible for chaining together multiple Dockerized steps. Steps can also be run standalone from the `tools/` directory.

## Contact

For questions or collaboration inquiries, please email hannah.martinez@jhuapl.edu, caitlyn.bishop@jhuapl.edu, or daniel.xenes@jhuapl.edu.

## License
See [LICENSE](LICENSE) for license information.

## Acknowledgements
This software was created by the Johns Hopkins University Applied Physics Laboratory and Harvard University, with funding supported by the NIH BRAIN Initiative under grant no. U01NS132158.

The views, opinions, and/or findings expressed are those of the author(s) and should not be interpreted as representing the official views or policies of the NIH.

© 2026 The Johns Hopkins University Applied Physics Laboratory LLC
