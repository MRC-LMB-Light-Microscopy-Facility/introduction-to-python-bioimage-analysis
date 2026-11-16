# Training on image analysis of light microscopy data in python
[![Binder](https://mybinder.org/badge_logo.svg)](https://github.com/MRC-LMB-Light-Microscopy-Facility/introduction-to-python-bioimage-analysis/HEAD)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/MRC-LMB-Light-Microscopy-Facility/introduction-to-python-bioimage-analysis)

This course introduces the analysis of light microscopy data using python and Jupyter notebooks through a problem-solving approach. It illustrates how to extract relevant information from an image using the relevant Python packages.

This course is ideal for researchers working with microscopy data who want to harness the power of Python-based, open-source tools for image analysis. Python provides a flexible and customizable framework for building reproducible workflows — from quick visual inspections to fully automated pipelines — with support for batch processing and scalable analysis across datasets of any size. 

### Learning objectives
- Notebooks
- Loading images and metadata (BioIO)
- Blob detection.
- Cell segmentation (Cellpose)
- Object parenting
- Region Measurements
- Visualization (Matplotlib/Napari)
- Statistics Analysis (SciPy)
- Batch processing 
- Tracking 

### Problems
1. Stress granule characterization
2. Cargo relocation 
3. Tracking of transcription factors

## Installation

Install first [miniconda](https://docs.anaconda.com/free/miniconda/miniconda-install/). On Windows, install miniconda in a folder without spaces in the path (e.g. `C:\Software\`).

Download, [Visual Code](https://code.visualstudio.com/download).

On Windows with cuda support:
```bash
conda env create -f envs/environment-windows-gpu.yml
conda activate imaging-python-course
```

On MacOS:
```bash
conda env create -f envs/environment-macos.yml
conda activate imaging-python-course
```

On Linux with cuda support:
```bash
conda env create -f envs/environment-linux-gpu.yml
conda activate imaging-python-course
```
