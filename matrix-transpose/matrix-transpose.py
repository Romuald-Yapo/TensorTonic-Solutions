import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    #create the transpose matrix
    mat = np.asarray(A, dtype= float)
    num_r, num_c = mat.shape
    tr_mat = np.zeros([num_c, num_r])

    for i in range(num_c) :
        for j in range(num_r):
            tr_mat[i,j] = mat[j,i]

    return tr_mat

    
