import numpy as np

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