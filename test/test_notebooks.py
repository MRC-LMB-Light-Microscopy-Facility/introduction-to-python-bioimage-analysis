from typing import Literal
import pytest
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors import CellExecutionError

ep = ExecutePreprocessor(timeout=600, kernel_name="python3")


def run(path):
    try:
        with open(path) as f:
            nb = nbformat.read(f, as_version=4)
        ep.preprocess(nb, {"metadata": {"path": "./"}})

    except CellExecutionError as ce:
        pytest.fail(f"Unexpected exception raised: {ce}")


@pytest.fixture
def data():
    from urllib.request import urlopen
    from io import BytesIO
    from zipfile import ZipFile

    url = "https://cloud.mrc-lmb.cam.ac.uk/s/wK4m29X6GCYdG8S/download/data.zip"
    http_response = urlopen(url)
    zipfile = ZipFile(BytesIO(http_response.read()))
    zipfile.extractall(path="../data")
    return True


# def test_download_data():
#     run("test/download.ipynb")


def test_ipywidgets(data: Literal[True]):
    run("test/ipywidget.ipynb")


def test_mplinteraction(data: Literal[True]):
    run("test/mplinteraction.ipynb")
