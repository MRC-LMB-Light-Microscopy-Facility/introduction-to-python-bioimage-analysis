# Bio image analysis in python
[![Binder](https://mybinder.org/badge_logo.svg)](https://github.com/MRC-LMB-Light-Microscopy-Facility/introduction-to-python-bioimage-analysis/HEAD)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/MRC-LMB-Light-Microscopy-Facility/introduction-to-python-bioimage-analysis)

This course introduces the analysis of light microscopy data using python and Jupyter notebooks through a problem-solving approach. It illustrates how to extract relevant information from an image using common Python packages.

You can use the badges at the top to open the repository on Google Colab and Binder.

### Learning objectives
Jupyter notebooks, loading images, numpy arrays, image visualization with matplotlib and napari, image filtering, mask post-processing, spot detection, region measurement, object parenting, cell segmentation with cellpose, particle tracking, statistical analysis.


### Problems
1. Quantification of perixosomes in cells
2. Cargo relocation 
3. Segmentation of bone marrow cells
4. Tracking of transcription factors

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
