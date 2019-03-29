def ND(mat,beta=0.99,alpha=1,control=0):

    import scipy.stats.mstats as stat
    from numpy import linalg as LA
    import numpy as np

    if beta>=1 or beta<=0:
        print('error: beta should be in (0,1)')
      
    if alpha>1 or alpha<=0:
            print('error: alpha should be in (0,1)')
     
    
    '''
    ***********************************
     Processing the inut matrix
     diagonal values are filtered
    '''
    
    n = mat.shape[0]
    np.fill_diagonal(mat, 0)
    
    '''
    Thresholding the input matrix
    '''
    y =stat.mquantiles(mat[:],prob=[1-alpha])
    th = mat>=y
    mat_th=mat*th;

    '''
    making the matrix symetric if already not
    '''
    mat_th = (mat_th+mat_th.T)/2

    
    '''
    ***********************************
    eigen decomposition
    '''
    print('Decomposition and deconvolution...')

    Dv,U = LA.eigh(mat_th) 
    D = np.diag((Dv))
    lam_n=np.abs(np.min(np.min(np.diag(D)),0))
    lam_p=np.abs(np.max(np.max(np.diag(D)),0))

    
    m1=lam_p*(1-beta)/beta
    m2=lam_n*(1+beta)/beta
    m=max(m1,m2)
    
    #network deconvolution
    for i in range(D.shape[0]):
        D[i,i] = (D[i,i])/(m+D[i,i])
    
    mat_new1 = np.dot(U,np.dot(D,LA.inv(U)))
    
                    
    '''
    
    ***********************************
     displying direct weights
    '''
    if control==0:
        ind_edges = (mat_th>0)*1.0;
        ind_nonedges = (mat_th==0)*1.0;
        m1 = np.max(np.max(mat*ind_nonedges));
        m2 = np.min(np.min(mat_new1));
        mat_new2 = (mat_new1+np.max(m1-m2,0))*ind_edges+(mat*ind_nonedges);
    else:
        m2 = np.min(np.min(mat_new1));
        mat_new2 = (mat_new1+np.max(-m2,0));
    
    
    '''
    ***********************************
     linearly mapping the deconvolved matrix to be between 0 and 1
    '''
    m1 = np.min(np.min(mat_new2));
    m2 = np.max(np.max(mat_new2));
    mat_nd = (mat_new2-m1)/(m2-m1);


    return mat_nd


