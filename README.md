
# Dynamical Component Analysis (DyCA)
Dynamical Component Analysis (DyCA) is a dimension reduction method for multivariate time series data. 

[![DOI](https://img.shields.io/badge/DOI-10.3389%2Ffams.2024.1456635-blue)](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2024.1456635)

## Installing information
``` $ pip install dyca```

## There are different ways to use the DyCA algorithm:
1. You know the number of linear and nonlinear components --> fine, you can use dyca(signal, time, m, n)
2. You know only the number of linear components, but not the dimension n of the underlying deterministic system:
    - with dyca(signal, time, m) you get the generalized eigenvalues and the singular values of the projection matrix and you can decide how many nonlinear components you want to use
    - run a second time dyca(signal, time, m, n) with the number of linear and nonlinear components (m: linear components, n: dimension of the system) you want to use
3. You don't know the number of linear and nonlinear components:
    - with dyca(signal, time) you get the generalized eigenvalues and you can decide how many linear components you want to use (Now you are in scenario 2.)
    - run a second time dyca(signal, time, m) with the number of linear components you want to use --> you get the singular values of the projection matrix and you can decide how many nonlinear components you want to use
    - run a third time dyca(signal, time, m, n) with the number of linear and nonlinear components (n = linear + nonlinear components) you want to use

## Example Usage

The roessler case is in detail explained in ```./example_usage/roessler70_example.ipynb```


Different **Data source** examples are shown in (where componentnoise and additivenoise specify the SNR in dB)

``` ./example_usage/example_data/{attractorname}_{componentnoise}_{additivenoise}.csv```


and implemented in 

```./example_usage/example_code/{attractorname}_{additivenoise}_example.py```

## Contact information
For question please contact: 
- mailto:annika.stiehl@hs-ansbach.de for installation or code-related information or 
- mailto:christian.uhl@hs-ansbach.de for method-related information.


## Citing information
[![DOI](https://img.shields.io/badge/DOI-10.3389%2Ffams.2024.1456635-blue)](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2024.1456635)

Uhl C, Stiehl A, Weeger N, Schlarb M and Hüper K (2024) Disentangling dynamic and stochastic modes in multivariate time series. Front. Appl. Math. Stat. 10:1456635. doi: 10.3389/fams.2024.1456635

BibTex:
```bibtex
@Article{Uhl2024,
  author={Uhl, Christian and Stiehl, Annika and Weeger, Nicolas and Schlarb, Markus and Hüper, Knut},
  journal={Frontiers in Applied Mathematics and Statistics}, 
  title={Disentangling dynamic and stochastic modes in multivariate time series}, 
  year={2024},
  volume={10},
  issn={2297-4687},
  url={https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2024.1456635},
  doi={10.3389/fams.2024.1456635}
  }
```


## Acknowledgement
This work has been supported by the German Federal Ministry of Education and Research (BMBF-Projekt, funding numbers: 05M20WWA and 05M20WBA Verbundprojekt 05M2020—DyCA).


