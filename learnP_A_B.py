from sampleF import *
from scipy.stats import gaussian_kde

'''
learns a model p for P(A,B) based on f_maps which are image statistics
f_maps - NxMxF array of F feature maps for NxM image

p - model for P(A,B)
'''
def learnP_A_B(f_maps, opts):
  if opts['model_type'] == 'kde':
    Nsamples = opts['kde']['Nkernels']
    F = sampleF(f_maps, Nsamples, opts)
    #we don't have multivariate 'epav' kernel in python :(
    if not opts['kde']['learn_bw']:
      p = gaussian_kde(F.T, bw_method=0.05)
    else:
      p = gaussian_kde(F.T)
  else:
    raise ValueError('unrecognized model type')
  return p