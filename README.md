## Installing information
pip install -r requirements.txt


## Citing information
```bibtex
@Article{Uhl2020,
  author={Uhl, Christian and Kern, Moritz and Warmuth, Monika and Seifert, Bastian},
  journal={IEEE Open Journal of Signal Processing}, 
  title={Subspace Detection and Blind Source Separation of Multivariate Signals by Dynamical Component Analysis (DyCA)}, 
  year={2020},
  volume={1},
  number={},
  pages={230-241},
  keywords={Heuristic algorithms;Signal processing algorithms;Tools;Brain modeling;Mathematical model;Noise measurement;
  Principal component analysis;Biomedical data;blind source separation;differential equations;dimensionality reduction;
  dynamical component analysis;independent component analysis;low dimensional dynamics;motion detection;principal component analysis},
  doi={10.1109/OJSP.2020.3038369}
  }
```

DOI: [10.1109/OJSP.2020.3038369](https://doi.org/10.1109/OJSP.2020.3038369)

## There are different ways to use the DyCA algorithm:
1. You know the number of linear and nonlinear components --> fine, you can use dyca(signal, time, m, n)
2. You know only the number of linear components, but not the dimension n of the underlying deterministic system:
    - with dyca(signal, time, m) you get the generalized eigenvalues and the singular values of the projection matrix and you can decide how many nonlinear components you want to use
    - run a second time dyca(signal, time, m, n) with the number of linear and nonlinear components (m: linear components, n: dimension of the system) you want to use
3. You don't know the number of linear and nonlinear components:
    - with dyca(signal, time) you get the generalized eigenvalues and you can decide how many linear components you want to use (Now you are in scenario 2.)
    - run a second time dyca(signal, time, m) with the number of linear components you want to use --> you get the singular values of the projection matrix and you can decide how many nonlinear components you want to use
    - run a third time dyca(signal, time, m, n) with the number of linear and nonlinear components (n = linear + nonlinear components) you want to use

## Example Code
For the third case: **roessler70_example.ipynb** \
Else: in example_code/{attractorname}\_{additivenoise}\_example.py

## Example data
In ./example_data you find the data for the example code \
Filenamestructure: \
    - {attractorname}\_{componentnoise}\_{additivenoise}.csv \
componentnoise and additivenoise specify the SNR in dB