import matplotlib.pyplot as plt
import scipy.io
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import seaborn as sns

raw_data = pd.read_pickle('data.pkl')
data = raw_data.copy()

adl_list = [1, 2]
channels = [0, 1, 2]

# on veut un dataframe qui contient uniquement les ADL et channels qu<on veut
new_df = data[data['ADL'].isin(adl_list)]

for subject in range(len(new_df)):
    new_df['raw_emg'].values[subject] = new_df['raw_emg'].values[subject][:, channels]
