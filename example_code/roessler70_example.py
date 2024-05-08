# if needed: pip install -r requirements.txt
import sys
sys.path.append('./')

import numpy as np
import matplotlib.pyplot as plt
from dyca import dyca, reconstruction

signal = np.genfromtxt('./example_data/roessler_0_70.csv', delimiter=',')
time = np.linspace(0, 100, signal.shape[1])

m = 2
n = 3

result_dyca = dyca(signal.transpose(), time_signal=time, n=n, m=m)

projectedSignal = result_dyca['projectedsignal']
eigenvalues = result_dyca['eigenvalues_dyca']
singular_values = result_dyca['singular_values']


result_reconstruction = reconstruction(signal, projectedSignal)

modes = result_reconstruction['modes']
reconstructedsignal = result_reconstruction['reconstruction']
cost = result_reconstruction['cost']


try:
    fig = plt.figure()
    plt.bar(range(len(eigenvalues)), eigenvalues)
    plt.title('DyCA generalized eigenvalues')
except:
    plt.close()
    print('No Eigenvalues found')

try:
    fig = plt.figure()
    plt.bar(range(len(singular_values)), singular_values)
    plt.title('SVD of Correlation Projectionmatrix')
except:
    plt.close()
    print('No Singular Values found')

# Plot 3D-trajectory of projected signal in phase space
try:
    plt.figure()
    ax3 = plt.axes(projection='3d')
    ax3.plot3D(projectedSignal[0, :],
               projectedSignal[1, :],
               projectedSignal[2, :])
    plt.title('DyCA trajectory in phase space')
    ax3.set_xlabel('$x_{1}$')
    ax3.set_ylabel('$x_{2}$')
    ax3.set_zlabel('$x_{3}$')
except:
    plt.close()
    print('No projected signal found')

# Plot channel 2 of the original signal and the reconstructed signal
try:
    plt.figure()
    plt.plot(time, signal[1, :], time, reconstructedsignal[1, :])
    plt.legend(['original', 'reconstructed'])
    plt.title('DyCA reconstructed signal vs original signal, channel 2')
    plt.xlabel('Time in s')
    plt.ylabel('Signalamplitude')
except:
    plt.close()
    print('No reconstruction found')

plt.show()
