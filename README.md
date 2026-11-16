# Training on image analysis of light microscopy data in python
[![Binder](https://mybinder.org/badge_logo.svg)](https://github.com/MRC-LMB-Light-Microscopy-Facility/introduction-to-python-bioimage-analysis/HEAD)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/MRC-LMB-Light-Microscopy-Facility/introduction-to-python-bioimage-analysis)

This course introduces light microscopy image analysis using Python and Jupyter notebooks through a practical, problem-solving approach. It demonstrates how to extract quantitative data from microscopy images using modern, open-source Python packages.

Designed for researchers working with microscopy data, this course shows how to harness Python's flexible ecosystem to build reproducible workflows-from quick visual inspections to automated, scalable batch-processing pipelines.

### Learning Objectives
By the end of this course, you will be able to:
- **Foundations & I/O:** Navigate Jupyter notebooks and load multi-dimensional images and metadata with `BioIO`
- **Visualization:** Inspect images, overlays, and segmentation masks using `Matplotlib` and `napari`
- **Segmentation & Detection:** Perform blob detection, deep-learning cell segmentation with `Cellpose`, and object parenting
- **Quantitative Analysis:** Extract region measurements, track dynamic objects over time, and run statistical analyses with `SciPy`
- **Automation:** Scale workflows across large datasets using batch processing

### Case Studies
You will apply these techniques to three real-world biological problems:
1. **Stress granule characterization** (blob detection, cell segmentation, and object parenting)
2. **Cargo relocation** (compartmental segmentation and intensity/region measurements)
3. **Tracking of transcription factors** (time-lapse particle tracking and dynamics)

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
