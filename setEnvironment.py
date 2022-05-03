def setEnvironment(_type):
  opts = {}
  opts['num_scales'] = 3
  opts['scale_offset'] = 0
  opts['features'] = {}
  opts['features']['which_features'] = ['color', 'var']
  opts['features']['decorrelate'] = 1
  opts['model_type'] = 'kde'
  opts['joint_exponent'] = 1.25
  opts['p_reg'] = 100
  opts['kde'] = {}
  opts['kde']['Nkernels'] = 10000
  opts['kde']['kdtree_tol'] = 0.001
  opts['kde']['learn_bw'] = True
  opts['kde']['min_bw'] = 0.01
  opts['kde']['max_bw'] = 0.1
  opts['model_half_space_only'] = True
  opts['sig'] = 0.25
  opts['only_learn_on_first_scale'] = False
  opts['approximate_PMI'] = True
  opts['PMI_predictor'] = {}
  opts['PMI_predictor']['Nsamples_learning_PMI_predictor'] = 10000
  opts['PMI_predictor']['Ntrees'] = 4
  opts['globalization_method'] = 'spectral_clustering'
  opts['spectral_clustering'] = {}
  opts['spectral_clustering']['approximate'] = False
  opts['spectral_clustering']['nvec'] = 100
  opts['border_suppress'] = 1
  opts['display_progress'] = True
  if _type == 'speedy':
    opts['kde']['Nkernels'] = 5000
    opts['kde']['learn_bw'] = False
    opts['approximate_PMI'] = True
    opts['scale_offset'] = 1
    opts['num_scales'] = 1
    opts['spectral_clustering']['approximate'] = True
  elif _type == 'accurate_low_res':
    opts['kde']['Nkernels'] = 5000
    opts['kde']['learn_bw'] = False
    opts['approximate_PMI'] = True
    opts['scale_offset'] = 1
    opts['num_scales'] = 1
  elif _type == 'accurate_high_res':
    opts['kde']['Nkernels'] = 5000
    opts['kde']['learn_bw'] = False
    opts['approximate_PMI'] = True
    opts['num_scales'] = 1
    opts['spectral_clustering']['approximate'] = True
  elif _type == 'accurate_multiscale':
    opts['approximate_PMI'] = True
    opts['PMI_predictor']['Ntrees'] = 32
  elif _type == 'MS_algorithm_from_paper':
    opts['approximate_PMI'] = False
  elif _type == 'compile_test':
    opts['kde']['Nkernels'] = 10
    opts['kde']['learn_bw'] = False
    opts['approximate_PMI'] = True
    opts['PMI_predictor']['Ntrees'] = 1
    opts['scale_offset'] = 0
    opts['num_scales'] = 1
    opts['which_features'] = ['color']
    opts['display_progress'] = False
  else:
    raise ValueError(f'Unknown setting type {_type}')
  return opts