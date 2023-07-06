#!/usr/bin/env python
"""The run script"""
import logging
import sys

from flywheel_gear_toolkit import GearToolkitContext

from fw_gear_n4_correction.main import run
from fw_gear_n4_correction.parser import parse_config

log = logging.getLogger(__name__)

def main(context: GearToolkitContext) -> None:
    """This parses config and run."""

    input_image, dim, dist, shrink_f, output_dir = parse_config(context)
    e_code = run(input_image, dim, dist, shrink_f, output_dir)
    sys.exit(e_code)

if __name__ == "__main__":

    with GearToolkitContext() as gear_context:

        gear_context.init_logging()
        main(gear_context)
