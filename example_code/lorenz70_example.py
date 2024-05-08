# if needed: pip install -r requirements.txt
import sys
sys.path.append('./')

from dyca import dyca, reconstruction
import matplotlib.pyplot as plt
import numpy as np


signal = np.genfromtxt('./example_data/lorenz_0_70.csv', delimiter=',')
time = np.linspace(0, 100, signal.shape[1])

m = 1
n = 2

result = dyca(signal.transpose(), time_signal=time, n=n, m=m)

projectedSignal = result['projectedsignal']
eigenvalues = result['eigenvalues_dyca']
singular_values = result['singular_values']

result_reconstruction = reconstruction(signal, projectedSignal)

modes = result_reconstruction['modes']
reconstructedsignal = result_reconstruction['reconstruction']
cost = result_reconstruction['cost']

try:
    fig = plt.figure()
    plt.bar(range(len(eigenvalues)), eigenvalues)
    plt.title('DyCA Eigenvalues')
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

try:
    plt.figure()
    plt.plot(projectedSignal[0, :],
             projectedSignal[1, :])
    plt.title('DyCA')
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
