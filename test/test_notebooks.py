from typing import Literal
import pytest
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors import CellExecutionError
from pathlib import Path
import os

os.environ["JUPYTER_PLATFORM_DIRS"] = "1"

ep = ExecutePreprocessor(timeout=600, kernel_name="python")


def run(path):
    try:
        with open(path) as f:
            nb = nbformat.read(f, as_version=4)
        ep.preprocess(nb, {"metadata": {"path": "./"}})

    except CellExecutionError as ce:
        pytest.fail(f"Unexpected exception raised: {ce}")


@pytest.fixture
def data():
    folder = Path("./data")
    if not folder.exists():
        from urllib.request import urlopen
        from io import BytesIO
        from zipfile import ZipFile

        url = "https://cloud3.mrc-lmb.cam.ac.uk/public.php/dav/files/Wpewom2LwE8YL7d/?accept=zip"

        http_response = urlopen(url)
        zipfile = ZipFile(BytesIO(http_response.read()))
        zipfile.extractall(path="./data")
        return True
    else:
        return True


def test_notebooks(data: Literal[True]):
    for nb in Path("nbs").glob("*.ipynb"):
        run(nb)
