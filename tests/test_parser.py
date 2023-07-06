"""Module to test parser.py"""
from unittest.mock import MagicMock

from flywheel_gear_toolkit import GearToolkitContext

from fw_gear_n4_correction.parser import parse_config


def test_parse_config(tmp_path):
    gear_context = MagicMock(spec=GearToolkitContext)
    gear_context.config = {"dist": 300, "dim": 3, "shrink_f": 1}
    gear_context.output_dir = tmp_path
    gear_context.get_input_path.return_value = tmp_path / "test_image.nii.gz"

    (input_image, dim, dist, shrink_f, out_dir) = parse_config(gear_context)
    assert dim == 3
    assert shrink_f == 1
    assert dist == 300
    assert out_dir == tmp_path
    # assert gear_context.get_input_path.assert_called_once_with('nifti-input')
    assert gear_context.get_input_path.call_args.args[0] == "nifti-input"
    assert input_image == (tmp_path / "test_image.nii.gz")
