# -*- coding: utf-8 -*-
"""
Created on 7/13/17
Author: Jihoon Kim
"""

# import modules
import pandas as pd
import numpy as np
from feature_eng import trim_features
from trim_data import drop_null_columns, categorize_target, split_loan_in_progress
from one_hot_encoding import one_hot_encoder
from one_hot_encoding import encode_neural_net_y
from keras.models import load_model
from keras.models import model_from_json
#import matplotlib.pyplot as plt
import feature_index
import sys

# load data
loan = pd.read_csv('./data/loan.csv')

# pre-process data
drop_null_columns(loan)
loan_in_progress = split_loan_in_progress(loan)
loan = categorize_target(loan)

# Feature Engineering by EDA
trim_features(loan)

# one-hot encoding
loan = loan[feature_index.features]
loan_one_hot_encoded = one_hot_encoder(loan)

#Assigning the new set of data to test
x_test = loan_one_hot_encoded.drop("loan_status_coded", axis=1)

#Preprocessing status
print("Preprocessing completed")
#print(x_test.shape)
#print(x_test.columns)
# load json and create model
json_file = open('neural_net_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("neural_net_model.h5")
print("Loaded model from disk")

#Prediction
#loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])
#preds_class = loaded_model.predict_classes(np.array(x_test))
#preds_class = pd.DataFrame(preds_class)
#print(preds_class.head())