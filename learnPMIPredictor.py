import numpy as np
from getLocalPairs import *
from extractF import *
from evalPMI import *
from sklearn.ensemble import RandomForestClassifier

def fastRFreg_train(F, pmi, Ntrees):
  RF = RandomForestClassifier(n_estimators = Ntrees, \
    max_features=min(3, X.shape[1]), min_samples_leaf = 5)
  #bruh they really don't support it anymore..
  RF.fit(F, pmi)
  return RF

'''
f_maps - list of feature maps
p - kde model
rf - random forest that approx PMI_rho
'''
def learnPMIPredictor(f_maps, p, opts):
  Nsamples = opts['PMI_predictor']['Nsamples_learning_PMI_predictor']
  im_size = f_maps[0].shape
  ii, jj = getLocalPairs(im_size, 5, 0, Nsamples) #defaults to 5, 0
  F, F_unary = extractF(f_maps, ii, jj, opts)
  pmi = evalPMI(p, F, F_unary, ii, jj, opts)
  Ntrees = opts['PMI_predictor']['Ntrees']
  rf = fastRFreg_train(F, pmi, Ntrees)
  return rf