"""Parser module to parse gear config.json."""

from typing import Tuple

from flywheel_gear_toolkit import GearToolkitContext


def parse_config(
    gear_context: GearToolkitContext,
) -> Tuple[str, int, int, int, str]:
    """Parses the config info.
    Args:
        gear_context: Context.

    Returns:
        input_image: A nifti file.
        dim: Dimension of the image.
        dist: B-spline fitting distance.
        shrink_f: Shrink factor resampling.
        output_dir: Directory of corrected output nifti file.
    """

    dim = gear_context.config.get("dim")
    dist = gear_context.config.get("dist")
    shrink_f = gear_context.config.get("shrink_f")
    output_dir = gear_context.output_dir

    input_image = gear_context.get_input_path("nifti-input")

    return input_image, dim, dist, shrink_f, output_dir
