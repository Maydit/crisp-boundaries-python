import numpy as np
from orderAB import *
'''
f_maps - list of feature maps
ii - indices of samples for feature A
jj - indices of samples for feature B
'''
def extractF(f_maps, ii, jj, opts):
  Npixels = np.prod(f_maps[0].shape)
  F = np.zeroes(ii.shape[0], len(f_maps)*2)
  for c, f_map in enumerate(f_maps):
    tmp = np.transpose(f_map, (1, 0, 2))
    F[:, c] = tmp(ii)
    F[:, c + len(f_maps)] = tmp(jj)
  kk = np.concatenate((ii, jj), axis=0)
  F_unary = np.empty(Npixels, len(f_maps))
  F_unary[:] = np.nan
  for c, f_map in enumerate(f_maps):
    tmp1 = np.transpose(f_map, (1, 0, 2))
    tmp2 = F_unary[:, c]
    tmp2[kk] = tmp1[kk]
    F_unary[:, c] = tmp2
  if opts['model_half_space_only']:
    F = orderAB(F)
  return F, F_unary