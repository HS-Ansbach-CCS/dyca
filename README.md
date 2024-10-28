
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

C. Uhl, A. Stiehl, N. Weeger, M. Schlarb and K. Hüper (2024) Disentangling dynamic and stochastic modes in multivariate time series. Front. Appl. Math. Stat. 10:1456635. doi: 10.3389/fams.2024.1456635


## Acknowledgement
This work has been supported by the German Federal Ministry of Education and Research (BMBF-Projekt, funding numbers: 05M20WWA and 05M20WBA Verbundprojekt 05M2020—DyCA).

## Further research with DyCA

### Presentation of DyCA with further examples
- C. Uhl, A. Stiehl, N. Weeger, M. Schlarb and K. Hüper (2024) Disentangling dynamic and stochastic modes in multivariate time series. Front. Appl. Math. Stat. 10:1456635. doi: 10.3389/fams.2024.1456635 [![DOI](https://img.shields.io/badge/DOI-10.3389%2Ffams.2024.1456635-blue)](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2024.1456635)
- C. Uhl, M. Kern, M. Warmuth and B. Seifert, Subspace Detection and Blind Source Separation of Multivariate Signals by Dynamical Component Analysis (DyCA), IEEE Open Journal of Signal Processing, vol. 1, pp. 230-241, 2020, doi: 10.1109/OJSP.2020.3038369 [![DOI](https://img.shields.io/badge/DOI-10.1109%2FOJSP.2020.3038369-blue)](https://ieeexplore.ieee.org/document/9260962/citations?tabFilter=papers#citations)
- K. Korn, B. Seifert and C. Uhl, „Dynamical Component Analysis (DYCA) and Its Application on Epileptic EEG,“ ICASSP 2019 - 2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Brighton, United Kingdom, 2019, pp. 1100-1104. doi: 10.1109/ICASSP.2019.8682601 [![DOI](https://img.shields.io/badge/DOI-10.1109%2FICASSP.2019.8682601-blue)](https://ieeexplore.ieee.org/document/8682601)
- B. Seifert, K. Korn, S. Hartmann, and C. Uhl, „Dynamical Component Analysis (DyCA): Dimensionality reduction for high-dimensional deterministic time-series,“ 2018 IEEE 28th International Workshop on Machine Learning for Signal Processing (MLSP), Aalborg, 17.-20.09.2018, pp. 1-6. doi: 10.1109/MLSP.2018.8517024 [![DOI](https://img.shields.io/badge/DOI-10.1109%2FMLSP.2018.8517024-blue)](https://ieeexplore.ieee.org/abstract/document/8517024)

### Comparison with Dynamic Mode Decomposition (DMD)
- A. Stiehl, N. Weeger and C. Uhl, Comparison of mode selection and reconstructions obtained by DyCA and DMD with respect to noise robustness and sampling, accepted for publication in CONTROLO 2024, Lecture Notes in Electrical Engineering, Springer-Verlag
- M. Kern, C. Uhl, M. Warmuth, A Comparative Study of Dynamic Mode  Decomposition (DMD) and Dynamical Component Analysis (DyCA). In:  Gonçalves J.A., Braz-César M., Coelho J.P. (eds) CONTROLO 2020. Lecture Notes in Electrical Engineering, vol 695. Springer, Cham, doi: 10.1007/978-3-030-58653-9_9 
[![DOI](https://img.shields.io/badge/DOI-10.1007/978--3--030--58653--9__9-blue)](https://doi.org/10.1007/978-3-030-58653-9_9)


### DyCA to generate additional ML-features
- A. Stiehl, M. Flammer, F. Anselstetter, N. Ille, H. Bornfleth, S. Geißelsöder, C. Uhl, Topological Analysis of Low Dimensional Phase Space
Trajectories of High Dimensional EEG Signals For Classification of Interictal Epileptiform Discharges, 2023 IEEE International Conference
on Acoustics, Speech, and Signal Processing Workshops (ICASSPW), Rhodes Island, Greece, 2023, pp. 1-5, doi: 10.1109/ICASSPW59220.2023.10193167 [![DOI](https://img.shields.io/badge/DOI-10.1109%2FICASSPW59220.2023.10193167-blue)](https://ieeexplore.ieee.org/document/10193167)

### DyCA in combination with SINDy
- C. Paglia, A. Stiehl, C. Uhl (2022), Identification of Low-Dimensional Nonlinear Dynamics from High-Dimensional Simulated and Real-World Data. In: L. Brito Palma, R. Neves-Silva, L. Gomes (eds) CONTROLO 2022. CONTROLO 2022. Lecture Notes in Electrical Engineering, vol 930. Springer, Cham. doi.org/10.1007/978-3-031-10047-5_18 [![DOI](https://img.shields.io/badge/DOI-10.1007/978--3--031--10047--5__18-blue)](https://doi.org/10.1007/978-3-031-10047-5_18)


### DyCA  in combination with derminismus testing
- C. Frühauf, S. Hartmann, B. Seifert and C. Uhl. Determinism testing of low-dimensional signals embedded in high-dimensional multivariate time-series. In: Stavrinides, S.G., Ozer, M. (eds) Chaos and Complex Systems. Springer, Berlin, Heidelberg, 2020, doi: 10.1007/978-3-030-35441-1_1 [![DOI](https://img.shields.io/badge/DOI-10.1007/978--3--030--35441--1__1-blue)](https://doi.org/10.1007/978-3-030-35441-1_1)

### Robust DyCA for noisy data
- M. Warmuth, P. Romberger, C. Uhl, Robust Dynamical Component Analysis via Multivariate Variational Denoising, Signal Processing Conference (EUSIPCO) 2021 29th European, pp. 2000-2004, 2021, doi: 10.23919/EUSIPCO54536.2021.9616108 [![DOI](https://img.shields.io/badge/DOI-10.23919%2FEUSIPCO54536.2021.9616108-blue)](https://ieeexplore.ieee.org/document/9616108)






