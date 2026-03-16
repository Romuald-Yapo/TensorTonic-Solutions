import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    values, counts  = np.unique(y, return_counts= True)
    
    probs = counts / len(y)
    #useless conditions but might be useful if you took as input directly the probabilities (e.g [0.1,0.2,0.7,0.0])
    probs = probs[probs > 0]
    
    entropy = -np.sum(probs*np.log2(probs))

    return entropy
        
        
    