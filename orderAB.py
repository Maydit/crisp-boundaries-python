import numpy as np

#copied the code, no idea if it works the same in python
def orderAB(F):
  swap_idx1 = 0
  swap_idx2 = int(F.shape[1]/2)
  m = (F[:, swap_idx1] <= F[:, swap_idx2])
  F_tmp = np.copy(F)
  F[m, swap_idx1] = F_tmp[m, swap_idx2]
  F[m, swap_idx2] = F_tmp[m, swap_idx1]
  return F