# TASKS

This is list of tasks to do before next session.

**Problem:** the current course is a bit too long and has many unclear concepts. 

**Objectives:** We want to have
1. problem-solving approach to teaching
1. handout/slide materials to introduce concepts
1. enable the participant to work autonomously
1. 1 notebook == 1 biological problem
1. aim for 4 hours in total
1. use scaffolded notebooks
1. use the computer in the image analysis room
1. enable people to run an existing workflow and adapt it.
1. introduce critical checking skills

## Redefine learning objectives (LO)  ✅
Here is current list
1. Bioimage analysis
    1. data and metadata loading (bioio/xarray)
    1. data visualization (napari)
    1. cells segmentation (cellpose)
    1. puncta segmentation (scikit-image)
    1. region properties (scikit-image)
    1. parenting (scikit-image)
    1. particles tracking (laptrack)
    1. export to CSV (pandas)
    1. Pearson correlation coefficient
1. General
    1.  work autonomously 
    1.  use containers/uv env
    1.  rerun and adapt a notebook cell
    1.  choose a library function for a stated analysis step

We remove concepts that are not used to solve a problem (Gaussian blur, etc.) to avoid distraction.

We test on second day the concept learned on the first day.

## Revise computing infrastructure
We want participants to be able to work autonomously in a reproducible environment in the analysis room.

1. [ ] write container file using uv and pyproject.toml corresponding with the required packages.

## Support Material (slide, handout)
We want to be more efficient at explaining concepts or providing reference notes in the handout.
1. [ ] write an introduction to Jupyter notebooks/VS Code and containers
1. [ ] add a few words about Python
1. [ ] write intro to image processing concepts
1. [ ] write problem description
1. [ ] update README.md to match the file

## Refine problems list ✅

The current problem list is


### Peroxisome
**Type:** guided exercise

**LO:** data and metadata loading, data visualization, cells segmentation, puncta segmentation, region properties, parenting, export to CSV

**Data:** A HeLa cell is imaged in fluorescence microscopy with 4 channels: 1. mitochondria, 2. actin, 3. peroxisomes and 4. DNA. 

**Synopsis:** We are interested in counting the number of peroxisomes per cell.

**Expected results:** A CSV with one row per cell and its peroxisome count, plus a napari view showing cell labels and detected peroxisomes. ⚠️ We have only one cell in the picture.

### Cargo tethering
**Type:** practice exercise

**LO:** data and metadata loading, data visualization, cells segmentation, region properties, export to CSV

**Data:** Cells are imaged using fluorescence confocal microscopy with four channels: 1. Golgi, 2. cargo, 3. mitochondria, and 4. nuclei.

**Synopsis:** In this cargo relocation assay, we want to quantify the amount of cargo protein associated with the mitochondria versus the amount associated with the Golgi apparatus using the Pearson correlation coefficient. We are going to report both the PCC for each cell and the intensity of the mitochondria channel.

**Expected results:** A CSV with one row per cell, including the cargo signal associated with mitochondria, the signal associated with Golgi, and the resulting per-cell ratio. Include a napari view of the relevant masks and channels.

### Tracking
**Type:** extension/advanced

**LO:** data and metadata loading, data visualization, puncta segmentation, particles tracking, export to CSV

**Data:** An image sequence with a single channel depicting a transcription factor moving.

**Synopsis:** Track the transcription factor across time.

**Expected results:** A table with one row per detection and columns for frame/time, position, and track ID, plus a trajectory visualization.

## Define the flow ✅
The duration can be adjusted by adding more or less scaffolding.
1. Day 1 [120min]
    1. **Learning:** Introduction [30min]
    1. **Learning:** Peroxisome [90min]
1. Day 2 [120min]
    1. **Practice:** Cargo tethering [60min]
    1. **Extension:** Tracking [60min]