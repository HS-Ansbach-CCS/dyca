import numpy as np
import scipy.linalg as linalg
import warnings


def derivativesignal(signal: np.ndarray, time_signal: np.ndarray):
    """Compute the derivative of a signal with respect to its sampling rate

    Arguments: 
        signal {np.ndarray} -- signal to be differentiated (timepoints, channels)
        time_signal {np.ndarray} -- time vector of the signal (timepoints, )

    Returns:
        np.ndarray -- derivative of the signal (timepoints, channels)
    """
    max = len(signal)
    dt = time_signal[1] - time_signal[0]
    derivative_signal = (signal[2:max, :] - signal[0:max - 2, :]) / (2*dt)
    first = (signal[1, :] - signal[0, :]) / (1*dt)
    last = (signal[max - 1, :] - signal[max - 2, :]) / (1*dt)
    derivative_signal = np.vstack((first, derivative_signal, last))

    return derivative_signal



def input_check(signal: np.ndarray, m: int, n: int, time_signal: np.ndarray, derivative_signal: np.ndarray):
    """Check the input of the dyca function

    When time_signal is not provided, it is generated from the number of timepoints in the signal.
    When derivative_signal is not provided, it is calculated from the signal.
    """

    if signal is None:
        raise ValueError('No signal provided')
    if not isinstance(signal, np.ndarray):
        raise ValueError('Signal has to be a numpy array')
    if signal.ndim != 2:
        raise ValueError('Signal has to be a 2D array')
    if signal.shape[0] < signal.shape[1]:
        raise ValueError('Signal has to have more timepoints than channels')

    if time_signal is None:
        time_signal = np.array(range(signal.shape[0]))
    else:
        if not isinstance(time_signal, np.ndarray):
            raise ValueError('Time signal has to be a numpy array')
        if time_signal.ndim != 1:
            raise ValueError('Time signal has to be a 1D array')
        if time_signal.shape[0] != signal.shape[0]:
            raise ValueError('Time signal has to have the same length as the signal')

    if derivative_signal is None:
        derivative_signal = derivativesignal(signal, time_signal)
    else:
        if not isinstance(derivative_signal, np.ndarray):
            raise ValueError('Derivative signal has to be a numpy array')
        if derivative_signal.shape != signal.shape:
            raise ValueError('Derivative signal has to have the same shape as the signal')

    if not isinstance(n, int) or n < -1 or n > signal.shape[1] or n == 0:
        raise ValueError('n has to be an integer greater than 0, or -1 for no limit')

    if not isinstance(m, int) or m < -1 or m > signal.shape[1] or m == 0:
        raise ValueError('m has to be an integer greater than 0, or -1 for no limit')

    # dyca conditions m > n - m
    if m != -1 and n != -1:
        if m < n - m:
            raise ValueError('m has to be greater than n - m')
        if m == n - m:
            warnings.warn('m is equal to n - m. This may lead to worse results.', UserWarning)
        if m > signal.shape[1]:
            raise ValueError('m has to be smaller than the number of channels')
        if n > signal.shape[1]:
            raise ValueError('n has to be smaller than the number of channels')
        if n < m:
            raise ValueError('n has to be greater than m')

    return signal, m, n, time_signal, derivative_signal


def cholesky_inverse(matrix: np.ndarray):
    L_lower_matrix = linalg.cholesky(matrix, lower=True)
    L_lower_inv_matrix = linalg.inv(L_lower_matrix)
    matrix_inv = np.transpose(L_lower_inv_matrix) @ L_lower_inv_matrix
    return matrix_inv


def check_eigenvalues_real(eigenvalues: np.ndarray):
    if np.all(np.imag(eigenvalues) != 0):
        raise ValueError('Complex eigenvalues detected. Check your input signal.')
    return np.real(eigenvalues)
