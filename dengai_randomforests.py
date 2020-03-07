# -*- coding: utf-8 -*-
"""DengAI_RandomForests.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mBcOuaQoRF6oMEFhs4TJSGcRd1AGLvuT
"""

from __future__ import print_function
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import numpy as np
import seaborn as sns

disease = pd.read_csv("https://s3.amazonaws.com/drivendata/data/44/public/dengue_features_train.csv")
disease.columns = [ "city","year","weekofyear","week_start_date","ndvi_ne","ndvi_nw","ndvi_se","ndvi_sw","precipitation_amt_mm" , "reanalysis_air_temp_k", "reanalysis_avg_temp_k","reanalysis_dew_point_temp_k","reanalysis_max_air_temp_k","reanalysis_min_air_temp_k","reanalysis_precip_amt_kg_per_m2","reanalysis_relative_humidity_percent","reanalysis_sat_precip_amt_mm", "reanalysis_specific_humidity_g_per_kg", "reanalysis_tdtr_k","station_avg_temp_c", "station_diur_temp_rng_c", "station_max_temp_c", "station_min_temp_c", "station_precip_mm"]
disease.head()

#Here deleting some of the unecessary columns to get the results looking for
del disease['city']
del disease['week_start_date']

#Now we use a heatmap to show some Correlation, Just as we did During Linear Regression
heatMap = pd.DataFrame(disease)
test1 = disease[['station_max_temp_c' , 'year' ,'ndvi_se', 'reanalysis_air_temp_k', 'reanalysis_avg_temp_k', 'reanalysis_tdtr_k', 'reanalysis_max_air_temp_k', 'reanalysis_specific_humidity_g_per_kg', 'station_diur_temp_rng_c',  'station_precip_mm' ]]
corr = test1.corr(method='pearson') 
fig, ax = plt.subplots(figsize=(9,9))
sns.heatmap(corr, annot=True, xticklabels=corr.columns, 
            yticklabels=corr.columns, ax=ax, linewidths=.5, 
            vmin = -1, vmax=1, center=0)

disease.columns

X = disease.iloc[:,0:10].values
y = disease.iloc[:, 10].values

#Now split the data into training/Testing
features = disease[["station_max_temp_c", "year",  "ndvi_se" , "reanalysis_air_temp_k", "reanalysis_avg_temp_k" , "reanalysis_tdtr_k", "reanalysis_max_air_temp_k" ,"reanalysis_specific_humidity_g_per_kg" , "station_diur_temp_rng_c", "station_precip_mm" ]]
targets = disease[["weekofyear"]]

features = features.dropna()

# Match features count after removing NaN values
targets = targets[:features.count()[0]]

X = disease.iloc[:,0:10].values
y = disease.iloc[:, 10].values

#Now split the data into training/Testing

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2)
#Here is the n_estimators we chose and giving the values we are desiring.
reg = RandomForestRegressor(n_estimators=24, random_state=5)

#Here using Regression in the Random Forest, Not the Classifier. From a predetermined state.
results = smf.ols("weekofyear ~ station_max_temp_c + year + ndvi_se +reanalysis_air_temp_k + reanalysis_avg_temp_k +reanalysis_tdtr_k + reanalysis_max_air_temp_k + reanalysis_specific_humidity_g_per_kg + station_diur_temp_rng_c + station_precip_mm ", data = disease).fit()

results.summary()

X = disease.iloc[:,0:5].values
y = disease.iloc[:, 5].values

features = disease[["station_max_temp_c", "year",  "ndvi_se" , "reanalysis_air_temp_k", "reanalysis_avg_temp_k" , "reanalysis_tdtr_k", "reanalysis_max_air_temp_k" ,"reanalysis_specific_humidity_g_per_kg" , "station_diur_temp_rng_c", "station_precip_mm" ]]
targets = disease[["weekofyear"]]

results = smf.ols("weekofyear ~ station_max_temp_c + year +reanalysis_air_temp_k + reanalysis_avg_temp_k +reanalysis_tdtr_k + reanalysis_max_air_temp_k + reanalysis_specific_humidity_g_per_kg + station_precip_mm ", data = disease).fit()

results.summary()