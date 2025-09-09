"""Test loading modules used in the course

This enable to check if the environment is correct.
"""


def test_matplotlib():
    import matplotlib.pyplot as plt

    plt.plot([1, 2, 3], [1, 2, 3])


def test_bioio():
    """Loading images with bioio"""
    from pathlib import Path
    from bioio import BioImage

    data_folder = Path("../data")

    items = [
        ("airyscan-4colors.tif", (1, 4, 1, 1912, 1912)),
        ("181228_CDX2_9s_c48_n073.tif", (105, 1, 1, 114, 168)),
        ("Zeiss1344.lsm", (1, 4, 1, 1220, 1220)),
    ]

    for name, shape in items:
        image = BioImage(data_folder / name)
        assert image.shape == shape


def test_napari():
    import napari
    import numpy as np

    viewer = napari.Viewer()
    viewer.add_image(np.zeros((10, 10)))


def test_skimage():
    import numpy as np
    from skimage import filters

    img = np.zeros((10, 10))
    filters.gaussian(img, 2)
    assert img.shape == (10, 10)


def test_ndi():
    from scipy import ndimage as ndi
    import numpy as np

    mask = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    mask = ndi.binary_fill_holes(mask).astype(int)
    assert mask.shape == (3, 3)
    assert mask.min() == 1


def test_torch():
    import torch

    assert int(torch.__version__.split(".")[0]) >= 2


def test_cellpose():
    from cellpose import models

    model = models.Cellpose(gpu=False, model_type="cyto2")


def test_laptrack():
    import laptrack
