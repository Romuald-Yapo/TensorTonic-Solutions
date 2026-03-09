import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    ar = np.asarray(x, dtype=float)
    out = 1 / (1+ np.exp(-ar))
    return out