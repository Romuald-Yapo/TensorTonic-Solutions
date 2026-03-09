import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    p = np.asarray(p, dtype=float)
    if (1 - p.sum() ) > 1e-6 :
        raise ValueError("not a valid probability partition")
        
    elif (x.shape != p.shape):
        raise ValueError("No match between x and p")
        return None
    else:
        exp_val = np.sum(x*p)
    return exp_val
        
