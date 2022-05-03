from sampleF import *
from sklearn.neighbors import KernelDensity

'''
learns a model p for P(A,B) based on f_maps which are image statistics
f_maps - NxMxF array of F feature maps for NxM image.. really a list

p - model for P(A,B)
'''
def learnP_A_B(f_maps, opts):
  if opts['model_type'] == 'kde':
    Nsamples = opts['kde']['Nkernels']
    F = sampleF(f_maps, Nsamples, opts)
    Nsamples_val = 500
    F_val = sampleF(f_maps, Nsamples_val, opts)
    if not opts['kde']['learn_bw']:
      kde = KernelDensity(bandwidth=0.05, kernel='epanechnikov')
      p = kde.fit(F)
    else:
      #TODO!? it automagically searches for a good bandwidth
      raise NotImplementedError()
  else:
    raise ValueError('unrecognized model type')
  return p