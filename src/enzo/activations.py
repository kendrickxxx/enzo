"""Activation functions."""

import numpy as np
from . import derivatives
from .derivatives import with_derivative


@with_derivative(derivatives.d_noactivation)
def noactivation(rows):
    """Do nothing, return `rows`."""
    return rows


@with_derivative(derivatives.d_relu)
def relu(rows):
    """Apply max(0, n) to each n in `rows`.

    Parameters
    ----------
    rows : array_like
    """
    rows = np.asarray(rows)
    return rows * (rows > 0)


@with_derivative(derivatives.d_sigmoid)
def sigmoid(rows):
    """Apply 1 / (1 + e ^ -n) to each n in `rows`.

    Parameters
    ----------
    rows : array_like
    """
    rows = np.asarray(rows)
    return 1 / (1 + np.exp(-rows))


def _softmax(row):
    raised_to_the_e = np.exp(row)
    return raised_to_the_e / sum(raised_to_the_e)


@with_derivative(derivatives.d_softmax)
def softmax(rows):
    """Perform softmax scaling for each row in `rows`."""
    rows = np.asarray(rows)
    return np.apply_along_axis(_softmax, arr=rows, axis=1)
