import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import seaborn as sns


def get_raw_emg(df: pd.DataFrame, subject: int, adl: int, display: False):

    row = df.loc[(df['subject'] == subject) & (df['ADL'] == adl)]
    time = row['time'].values[0]
    raw_emg = row['raw_emg'].values[0]
    if display:
        sns.lineplot(x=time, y=raw_emg)
        plt.xlabel('time')
        plt.ylabel('EMG')
        plt.title(f'subject: {subject}, ADL: {adl}')
        plt.show()
    return time, raw_emg


if __name__ == '__main__':

    data = pd.read_csv("raw_data.csv")
    raw_data = data.copy()
    subject = 20
    adl = 15
    time_vector, raw_emg_values = get_raw_emg(raw_data, subject, adl, display=True)
