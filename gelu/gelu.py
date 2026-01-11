import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: scalar, list, or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    x = np.array(x, dtype = float)
    erf = np.vectorize(math.erf)
    erf = erf(x/math.sqrt(2))
    gelu = 0.5*x*(1 + erf)
    return gelu
    pass