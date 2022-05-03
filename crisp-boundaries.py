import numpy as np
from scipy import sparse
import time

def getFeatures():
  pass

#this implements evaluate a kde tree
def evaluate_batches(p, F, tol):
  v = np.zeroes(F.shape[1], 1)
  n = 100000
  m = np.floor(F.shape[1] / n)
  end_i = 0
  eps = 10e-6
  for i in range(m):
    start_i = i * n
    end_i = start_i + n
    tmp = F[:, start_i:end_i]
    #add randomness?
    v[start_i:end_i] = evaluate(p, tmp, tol)
  tmp = F[:, end_i:]
  v[end_i:] = evaluate(p, tmp, tol)
  return v

def evalPMI(p, F, F_unary, A, A_idx, B_idx, opts):
  reg = opts['p_reg']
  tol = opts['kde']['kdtree_tol']
  if opts['model_half_space_only']:
    pJoint = reg + evaluate_batches(p, F.T, tol) / 2
  else:
    pJoint = reg + evaluate_batches(p, F.T, tol)
  N = np.floor(F.shape[1] / 2)
  assert (np.round(N) - N) == 0
  #need another library...
  p2_1 = marginal(p, )
  return pmil pJoin, pProd

def buildW_pmi(f_maps, rf, p, opts, samples):
  if not samples:
    samples = np.zeroes() #idk the size yet
  im_size = f_maps.shape[:-1]
  if not samples or samples.shape[1] == 1:
    [ii, jj] = getLocalPairs(im_size, [], [], samples)
  else:
    ii = samples[:, 0]
    jj = samples[:, 1]
  Npixels = np.prod(im_size)
  W = sparse.csr_matrix((0, (ii, jj)), shape=(Npixels, Npixels))
  F, F_unary = extractF(f_maps, ii, jj, opts)
  if opts['approximate_PMI']:
    w = np.exp(fastRFreg_predict(F, rf))
  else:
    pmi = evalPMI(p, F, F_unary, ii, jj, opts)
    w = exp(pmi)
  W2 = sparse.csr_matrix((w, (ii, jj)), shape=(Npixels, Npixels))
  W = W+W2
  W = (W + W.T)
  return W

def borderSuppress(E_oriented):
  border_rad = np.ceil(0.03 * E_oriented.shape[0])
  xx, yy = np.meshgrid([list(range(len(E_oriented.shape[1]))), list(range(len(E_oriented.shape[0])))])
  aspect_ratio = E_oriented.shape[1] / E_oriented.shape[0]
  m1 = xx > aspect_ratio * yy
  m2 = np.fliplr(m1)
  #TODO border suppressor calculation

  norient = E_oriented.shape[2]
  dtheta = np.pi / norient
  ch_per = [4, 3, 2, 1, 8, 7, 6, 5]
  border_suppressor = [] #instead some numpy array
  for o in range(norient):
    theta = dtheta * o
    border_suppressor[:,:,ch_per[o]] = abs(cos(theta)).*hort_border_suppressor + abs(sin(theta)).*vert_border_suppressr
  border_suppressor = 1 - border_suppressor
  E_oriented = np.multiply(border_suppressor, E_oriented)
  return E_oriented

def getE(Ws, im_sizes, image, opts):
  if opts['globalization_method'] == 'spectral_clustering':
    if opts['display_progress']:
      print('\nspectral clustering...')
      op_time = time.time()
    nvec = opts['spectral_clustering']['nvec']
    if len(im_sizes) > 1:
      #todo
      pass
    else:
      W = Ws[0]
      if not opts['spectral_clustering']['approximate']:
        #E_oriented = spectralPb_custom(W, [im_sizes[0] ], '', nvec)
        #TODO fix the above line
      else:
        E_oriented = spectralPb_fast_custom(W, [], nvec)
        #TODO fix the above line
    if opts['display_progress']:
      op_time = time.time() - op_time
      print('done: {op_time:.2f} sec\n')
  else:
    raise ValueError(f'Unknown globalization method {opts['globalization_method']}')
  if opts['border_suppress']:
    E_oriented = borderSuppress(E_oriented)
  E = np.amax(E_oriented, axis=2) #get largest elements along dimension 2
  return E, E_oriented