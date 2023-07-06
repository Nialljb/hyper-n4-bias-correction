import shutil
from pathlib import Path

import nibabel
import numpy
import pytest

from fw_gear_n4_correction.main import run

INPUT_PATH = Path(__file__).parents[0] / "assets/input"
OUTPUT_PATH = Path(__file__).parents[0] / "assets/output"


@pytest.mark.skip
@pytest.mark.parametrize(
    "dist, shrink_f",
    [
        (300, 1),
        (500, 3),
        (400, 2),
    ],
)
def test_integration(tmp_path, dist, shrink_f):
    input_file = INPUT_PATH / "sub-51187_T1w.nii"
    dim = 3
    out_dir = tmp_path / "output"
    e_code = run(input_file, dim, dist, shrink_f, out_dir)

    out = nibabel.load(out_dir / "corrected_image.nii")
    expected_output = nibabel.load(
        OUTPUT_PATH / f"sub-51187_T1w_dim-{dim}_dist-{dist}_shrinkf-{shrink_f}.nii"
    )
    # Assert expected output with whatever metric.
    assert numpy.all(out.get_fdata() == expected_output.get_fdata())
