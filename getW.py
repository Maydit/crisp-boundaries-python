import numpy as np
import time
from getFeatures import *
from buildW_pmi import *
from learnP_A_B import *
from learnPMIPredictor import *

'''
image NxMxC

returns:
Ws - list of affinity matrices: Ws[i] is the affinity matrix for the image at scale i
im_sizes = im_sizes[i] gives dimensions of the image at scale i
'''
def getW(image, opts):
  num_scales = opts['num_scales']
  scale_offset = opts['scale_offset']
  im_sizes = [0]*num_scales #list of np shapes, one for each scale
  Ws = [0]*num_scales #list
  Ws_each_feature_set = [0]*num_scales

  for s in range(num_scales):
    if opts['display_progress']:
      print(f'\n\nProcessing scale {s + 1 + scale_offset}:\n')
    f_maps = []
    for i in range(len(opts['features']['which_features'])):
      f_maps.append(getFeatures(image.astype(double)/255, s + 1 + scale_offset, opts['features']['which_features'][i], opts))
    
    Ws_each_feature_set[s] = [0]*len(f_maps) #init these
    
    for feature_set_iter in range(len(f_maps)):
      if opts['display_progress']:
        print(f'\nProcessing feature type "{opts['features']['which_features'][feature_set_iter]}":\n')
      scale = 2**(-(s + scale_offset))
      f_maps_curr = f_maps[feature_set_iter]
      im_sizes[num_scales - s + 1] = [f_maps_curr.shape[1], f_maps_curr.shape[0]]
      if s == 0 or not opts['only_learn_on_first_scale']:
        if opts['display_progress']:
          print('learning image model...')
          op_time = time.time()
        p = learnP_A_B(f_maps_curr, opts)
        if opts['display_progress']:
          op_time = time.time() - op_time
          print('done: {op_time:.2f} sec\n')
        if opts['approximate_PMI']:
          if opts['display_progress']:
            print('learning PMI predictor...')
            op_time = time.time()
          rf = learnPMIPredictor(f_maps_curr,p,opts)
          if opts['display_progress']:
            op_time = time.time() - op_time
            print('done: {op_time:.2f} sec\n')
        else:
          rf = [] #TODO initialize like something
      if opts['display_progress']:
        print('building affinity matrix...')
        op_time = time.time()
      if opts['model_type'] == 'kde':
        Ws_each_feature_set[num_scales - s + 1][feature_set_iter] = buildW_pmi(f_maps_curr, rf, p, opts)
      else:
        raise ValueError('Unrecognized model type')
      if opts['display_progress']:
        op_time = time.time() - op_time
        print('done: {op_time:.2f} sec\n')
      if feature_set_iter == 0:
        Ws[num_scales - s + 1] = Ws_each_feature_set[num_scales - s + 1][feature_set_iter]
      else:
        Ws[num_scales - s + 1] = np.multiply(Ws[num_scales - s + 1], Ws_each_feature_set[num_scales - s + 1][feature_set_iter])
  return Ws, im_sizes