import numpy as np
'''
pmi evaluated at A, B in F
P(A, B)
P(A)P(B)
'''
def evalPMI(p, F, F_unary, A_idx, B_idx, opts):
  reg = opts['p_reg']
  tol = opts['kde']['kdtree_tol']
  if opts['model_half_space_only']:
    pJoint = reg + evaluate_batches(p, F.T, tol)/2
  else:
    pJoint = reg + evaluate_batches(p, F.T, tol)
  N = np.floor(F.shape[1]/2)
  
  return pmi, pJoint, pProd