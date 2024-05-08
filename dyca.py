import numpy as np
import scipy.linalg as linalg
from additional_functions_dyca import *


def reconstruction(signal: np.ndarray, projectedsignal: np.ndarray):
    """Find modes such that modes*projectedsignal approximates signal

    Arguments:
        signal {np.ndarray} -- input signal (time, channels)
        projectedsignal {np.ndarray} -- projected signal (n, time)

    Returns:
        dictionary with:
            modes {np.ndarray} -- modes (channels, n)
            reconstruction {np.ndarray} -- reconstructed signal (time, channels)
            cost {float} -- cost of the reconstruction

    """

    modes = signal @ np.linalg.pinv(projectedsignal)

    # reconstructed time-series
    reconstruction = modes @ projectedsignal

    cost = np.linalg.norm(reconstruction - signal) / np.linalg.norm(signal)

    output = {
        'modes': modes,
        'reconstruction': reconstruction,
        'cost': cost
    }

    return output


def dyca(signal: np.ndarray, m: int = -1, n: int = -1, time_signal: np.ndarray = None, derivative_signal: np.ndarray = None):
    """ Calculates the dynamical Components of the input signal and its projected signal

    Arguments:
        signal {np.ndarray} -- input signal (time, channels) with full rank
        m {int} -- number of linear components to be used for reconstruction - if m = -1, only the eigenvalues are returned
        n {int} -- number of equations to be used for reconstruction - if n = -1, only the eigenvalues and singular values are returned
        (optional) time_signal {np.ndarray} -- the corresponding time array of the signal (time,)
        (optional) derivative_signal {np.ndarray} -- the derivative of the signal with respect to the time array (time, channels)

    Returns:
        dictionary with:
            projectedsignal {np.ndarray} -- projected signal (n, time)
            eigenvalues {np.ndarray} -- eigenvalues (channels,)
            singular_values {np.ndarray} -- singular_values of the projected signal (2*m,)

    """

    output = {
        'projectedsignal': None,
        'eigenvalues_dyca': None,
        'singular_values': None
    }

    signal, m, n, time_signal, derivative_signal = input_check(signal, m, n, time_signal, derivative_signal)
    time_length = signal.shape[0]

    # Calculate correlation matrices C0, C1 and C2
    C0 = (np.transpose(signal) @ signal) / time_length
    C1 = (derivative_signal.transpose() @ signal) / time_length
    C2 = (derivative_signal.transpose() @ derivative_signal) / time_length

    # calculate the inverse of C0 by Cholesky decomposition
    try:
        C0_inv = cholesky_inverse(C0)
    except Exception as e:
        print(e)
        raise ValueError('Failed calculating the inverse of C0. Check your rank of the input signal.')

    # Solve the generalized eigenvalue problem
    # C1* inv(C0)* C1^T* u_i = lambda_i * C2 * u_i
    lambda_i, u_i = linalg.eig(C1 @ C0_inv @ np.transpose(C1), C2)

    # Check if eigenvalues are real
    lambda_i = check_eigenvalues_real(lambda_i)

    # Sort eigenvalues lambda_i and eigenvectors u_i
    indices = np.flip(np.argsort(lambda_i))
    lambda_i_sort = lambda_i[indices]
    u_i = (u_i[:, indices])

    # Stop algorithm, if m is unknown
    if m == -1:
        output['eigenvalues_dyca'] = lambda_i_sort
        return output

    # Select m linear components
    u_i = u_i[:, :m]

    # Calculate v_i
    v_i = C0_inv @ np.transpose(C1) @ u_i

    # calculating the svd to select n equations
    projectionMatrix = np.concatenate((u_i, v_i), axis=1)
    amplitude = signal @ projectionMatrix
    amplitude_norm = np.divide(amplitude, np.sqrt(np.diag(amplitude.transpose() @ amplitude))).transpose()
    U_svd, S_svd, V_svd = linalg.svd(amplitude_norm, full_matrices=False)

    # stop algorithm, if n is unknown
    if n == -1:
        output['eigenvalues_dyca'] = lambda_i_sort
        output['singular_values'] = S_svd
        return output

    projectedsignal = U_svd[0:n, 0:n] @ np.diag(S_svd[0:n]) @ V_svd[0:n, :]

    output['projectedsignal'] = projectedsignal
    output['eigenvalues_dyca'] = lambda_i_sort
    output['singular_values'] = S_svd

    return output
