# N4 Bias Correction Gear
*Ammended from original Flywheel version from 'utility' to 'analysis' gear to pickup outputs of Hyperfine 3D reconstruction 

N4 is a variant of the popular N3 (nonparameteric nonuniform normalization) retrospective bias correction algorithm.

Based on the assumption that the corruption of the low frequency bias field can be modeled as a convolution of the intensity histogram by a Gaussian, the basic algorithmic protocol is to iterate between deconvolving the intensity histogram by a Gaussian, remapping the intensities, and then spatially smoothing this result by a B-spline modeling of the bias field itself. The modifications from and improvements obtained over the original N3 algorithm are described in [Tustison2010].

    Tustison2010
    N. Tustison et al., N4ITK: Improved N3 Bias Correction, IEEE Transactions on Medical Imaging, 29(6):1310-1320,
    June 2010.


## Usage

### Inputs

* nifti-input: A nifti file.

### Configuration
* dim: (integer, default 3) Dimension.
* dist: (integer, default 300) B-spline Fitting Distance isotropic mesh spacing for the smoothing.
* shrink_f: (integer, default 1) Shrink factor Resampling for large images.


## Contributing

For more information about how to get started contributing to that gear, 
checkout [CONTRIBUTING.md](CONTRIBUTING.md).
