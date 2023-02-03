import matplotlib.pyplot as plt
import scipy.io
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import data_preprocessing as dp
import seaborn as sns

raw_data = pd.read_pickle('data.pkl')
data = raw_data.copy()

adl_list = [1, 2]
channel_list = [0, 1, 4]

##### fonction  features lbl
# select the wanted ADLs

feature_mat = data[data['ADL'].isin(adl_list)]
# select the source electrodes
#for sample in range(len(feature_mat)):
#    feature_mat['raw_emg'].values[sample] = feature_mat['raw_emg'].values[sample][:, channel_list]

# duplicate the emg columns
for c in channel_list:
    print('c:', c)
    feature_mat = pd.concat([feature_mat, feature_mat['raw_emg'].rename(f'emg_channel_{c+1}')], axis=1)
    print('columns:', feature_mat.columns)

# only keep the wanted channel in every column
for sample in range(len(feature_mat)):
    for c in channel_list:
        print(f'c:{c}, c+1: {c+1}')
        feature_mat[f'emg_channel_{c+1}'].values[sample] = feature_mat[f'emg_channel_{c+1}'].values[sample][:, c]
label_vec = feature_mat[['ADL']] # double [] to make it a DataFrame and not a Series

# we don't need the time column, the label column and the raw_emg column
feature_mat = feature_mat.drop(columns=['time', 'ADL', 'raw_emg'])
