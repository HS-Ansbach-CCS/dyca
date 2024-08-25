# if needed: pip install -r requirements.txt

import numpy as np
from example_functions import apply_dyca

signal = np.genfromtxt('example_usage/example_data/lorenz_0_70.csv', delimiter=',')
time = np.linspace(0, 100, signal.shape[1])

m = 1
n = 2

apply_dyca(signal, time, n, m)

