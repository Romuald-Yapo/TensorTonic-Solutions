import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    """
    Returns elementwise Leaky ReLU values as a NumPy array matching the input shape.
    """
    # Write code here
    x = np.array(x, dtype=float)
    x[x< 0] = x[x<0] * alpha

    return x
    