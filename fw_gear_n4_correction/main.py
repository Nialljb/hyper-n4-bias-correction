"""Main module."""

import logging
import os

from nipype.interfaces.ants import N4BiasFieldCorrection

log = logging.getLogger(__name__)

def run(input_image, dim, dist, shrink_f, output_dir):

    """Runs the N4 Bias Field Correction algorithm.

    N4 is a variant of the popular N3 (non-parametric nonuniform normalization) retrospective bias correction algorithm.
    Based on the assumption that the corruption of the low frequency bias field can be modeled as a convolution of the
    intensity histogram by a Gaussian, the basic algorithmic protocol is to iterate between deconvolving the intensity
    histogram by a Gaussian, remapping the intensities, and then spatially smoothing this result by a B-spline modeling
    of the bias field itself. The modifications from and improvements obtained over the original N3 algorithm are
    described in Tustison-2010 paper.

    Args:
        input_image: A nifti file.
        dim: Dimension of the image.
        dist: B-spline fitting distance.
        shrink_f: Shrink factor resampling.
        output_dir: Directory of corrected output file.

    Returns:
        (int): Status code for N4BiasFieldCorrection workflow.
    """

    log.info("Starting the process of N4 Bias Field Correction...")
    n4 = N4BiasFieldCorrection()
    n4.inputs.input_image = input_image
    n4.inputs.dimension = dim
    n4.inputs.bspline_fitting_distance = dist
    n4.inputs.shrink_factor = shrink_f

    print("input_image: ", input_image)
    input_image = str(input_image)
    test = input_image.split(".")
    if test[-1] == "gz":
        file_name = input_image.split(".nii.gz")
        file_name = file_name[0].split("/")
        file_name = file_name[-1] + "_corrected.nii.gz"
    elif test[-1] == "nii":
        file_name = input_image.split(".nii")
        file_name = file_name[0].split("/")
        file_name = file_name[-1] + "_corrected.nii"

    # head_tail = os.path.split(input_image)
    # file_name = "corrected_" + str(head_tail[1])
    # input_image = str(input_image)
    # file_name = input_image.split('.nii.gz')
    # file_name = file_name[0].split('/')
    # file_name = file_name[-1] + '_corrected.nii.gz'

    n4.inputs.output_image = str(output_dir / file_name)

    n4.run()

    return 0
