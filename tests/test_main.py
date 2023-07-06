"""Module to test main.py"""

import os

import pytest

from fw_gear_n4_correction.main import run


def test_run(tmp_path, mocker):
    input_file = tmp_path / "test_file.nii.gz"
    input_file.touch()
    dim = 3
    dist = 300
    shrink_f = 3

    out_dir = tmp_path / "output"
    n4 = mocker.patch(
        "fw_gear_n4_correction.main.N4BiasFieldCorrection"
    )  # returns MagicMock
    # n4 = mocker.patch.object('fw_gear_n4_correction.main.N4BiasFieldCorrection')
    e_code = run(input_file, dim, dist, shrink_f, out_dir)

    head_tail = os.path.split(input_file)

    assert e_code == 0
    assert n4.return_value.inputs.input_image == input_file
    assert n4.return_value.inputs.dimension == dim
    assert n4.return_value.inputs.bspline_fitting_distance == dist
    assert n4.return_value.inputs.shrink_factor == shrink_f

    test = head_tail[1].split(".")
    if test[-1] == "gz":
        head_tail = head_tail[1].split(".nii.gz")
        head_tail = head_tail[0].split("/")
        head_tail = head_tail[-1] + "_corrected.nii.gz"
    elif test[-1] == "nii":
        head_tail = head_tail[1].split(".nii")
        head_tail = head_tail[0].split("/")
        head_tail = head_tail[-1] + "_corrected.nii"

    # head_tail = head_tail[1].split(".nii.gz")
    # head_tail = head_tail[0] + "_corrected.nii.gz"

    assert n4.return_value.inputs.output_image == str(out_dir) + "/" + head_tail

    # assert n4.return_value.inputs.output_image == str(out_dir / "corrected_image.nii")

    n4.return_value.run.assert_called_once()
    # assert n4.call_count == 1
