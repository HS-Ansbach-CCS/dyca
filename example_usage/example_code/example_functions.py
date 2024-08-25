# if needed: pip install -r requirements.txt

import matplotlib.pyplot as plt
from dyca import dyca, reconstruction


def plot_data(eigenvalues, singular_values, amplitudes, signal, reconstructedsignal, time):
    try:
        plt.figure()
        plt.bar(range(len(eigenvalues)), eigenvalues)
        plt.title('DyCA generalized eigenvalues')
    except:
        plt.close()
        print('No Eigenvalues found')

    try:
        plt.figure()
        plt.bar(range(len(singular_values)), singular_values)
        plt.title('SVD of Correlation Projectionmatrix')
    except:
        plt.close()
        print('No Singular Values found')

    # Plot 3D-trajectory of projected signal in phase space
    try:
        plt.figure()
        ax3 = plt.axes(projection='3d')
        ax3.plot3D(amplitudes[0, :],
                   amplitudes[1, :],
                   amplitudes[2, :])
        plt.title('DyCA trajectory in phase space')
        ax3.set_xlabel('$x_{1}$')
        ax3.set_ylabel('$x_{2}$')
        ax3.set_zlabel('$x_{3}$')
    except IndexError:
        plt.close()
        plt.figure()
        plt.plot(amplitudes[0, :],
                 amplitudes[1, :])
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

    # try:
    plt.figure()
    plt.plot(amplitudes[0, :],
             amplitudes[1, :])
    plt.title('DyCA')
    # except:
    #     plt.close()
    #     print('No projected signal found')


def apply_dyca(signal, time, n, m):
    result_dyca = dyca(signal.transpose(), time_index=time, n=n, m=m)

    amplitudes = result_dyca['amplitudes']
    eigenvalues = result_dyca['generalized_eigenvalues']
    singular_values = result_dyca['singular_values']

    result_reconstruction = reconstruction(signal, amplitudes)

    modes = result_reconstruction['modes']
    reconstructedsignal = result_reconstruction['reconstruction']
    cost = result_reconstruction['cost']

    plot_data(eigenvalues, singular_values, amplitudes, signal, reconstructedsignal, time)
