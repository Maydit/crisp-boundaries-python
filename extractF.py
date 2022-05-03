import numpy as np
from orderAB import *
'''
f_maps - NxMxF
ii - indices of samples for feature A but unraveled
jj - indices of samples for feature B
'''
def extractF(f_maps, ii, jj, opts):
  Npixels = np.prod(f_maps.shape[:2])
  F = np.zeros((ii.shape[0], f_maps.shape[2]*2))
  for c in range(f_maps.shape[2]):
    tmp = np.ravel(np.transpose(f_maps[:,:,c], (1, 0)), 'F')
    F[:, c] = tmp[ii]
    F[:, c + f_maps.shape[2]] = tmp[jj]
  kk = np.concatenate((ii, jj), axis=0)
  F_unary = np.empty((Npixels, f_maps.shape[2]))
  F_unary[:] = np.nan
  for c in range(f_maps.shape[2]):
    tmp1 = np.ravel(np.transpose(f_maps[:,:,c], (1, 0)), 'F')
    tmp2 = F_unary[:, c]
    tmp2[kk] = tmp1[kk]
    F_unary[:, c] = tmp2
  if opts['model_half_space_only']:
    F = orderAB(F)
  return F, F_unary