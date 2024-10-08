# if needed: pip install -r requirements.txt

import numpy as np
from example_functions import apply_dyca

signal = np.genfromtxt('example_usage/example_data/roessler_0_50.csv', delimiter=',')
time = np.linspace(0, 100, signal.shape[1])

m = 2
n = 3

apply_dyca(signal, time, n, m)
