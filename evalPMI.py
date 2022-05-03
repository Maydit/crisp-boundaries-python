import numpy as np
from scipy.stats import gaussian_kde

def getPoints(p):
  pts = np.zeros(p.d, p.n)
  pts[:, double(p.perm(p.n + ))]
  #idk anymore man...
  return pts

def marginal(p, rnge):
  pts = getPoints(p)
  if not opts['kde']['learn_bw']:
    p2 = gaussian_kde(pts, bw=0.05)
  else:
    p2 = gaussian_kde(pts)
  return p2

'''
pmi evaluated at A, B in F
P(A, B)
P(A)P(B)
'''
def evalPMI(p, F, F_unary, A_idx, B_idx, opts):
  reg = opts['p_reg']
  tol = opts['kde']['kdtree_tol']
  if opts['model_half_space_only']:
    pJoint = reg + p.evaluate(F.T)/2
  else:
    pJoint = reg + p.evaluate(F.T)
  N = int(np.floor(F.shape[1]/2))
  print(p.dataset.shape)
  print(p.d)
  p2_1 = marginal(p, np.arange(0, N))
  p2_2 = marginal(p, np.arange(N+1, N*2))
  p2 = joinTrees
  
  #print(p2_1)
  #print(p2_2)
  pMarg = np.zeros((F_unary.shape[0], 1))
  ii = np.argwhere(np.isnan(F_unary[:, 0]))
  pMarg[ii] = p2.evaluate(F_unary[ii, :].T)
  pProd = np.multiply(pMarg[A_idx], pMarg[B_idx]) + reg
  pmi = np.log(np.divide(np.power(pJoint,opts['joint_exponent']), pProd));
  return pmi, pJoint, pProd