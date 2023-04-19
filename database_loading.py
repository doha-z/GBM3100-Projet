import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import pandas as pd
import seaborn as sns


def load_data(mat_file_path: str, table_name: str):

    data = scipy.io.loadmat(mat_file_path)
    tab = data[table_name][0]
    sample_size = tab.shape[0]
    subject = []
    ADL = []
    time = []
    raw_emg = []

    for sample in range(sample_size):
        subject.append(tab[sample][0][0, 0])
        ADL.append(tab[sample][1][0, 0])
        time.append(tab[sample][2][:, 0])
        raw_emg.append(tab[sample][3][:, 0])

    df = pd.DataFrame({'subject': subject, 'ADL': ADL, 'time': time, 'raw_emg': raw_emg})
    return df


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


if __name__ == "__main__":

    mat_file = 'RAW_EMG.mat'
    tab_name = 'RAW_EMG'
    data = load_data(mat_file, tab_name)
    #display one
    subject = 1
    adl = 15
    time_vector, raw_emg_values = get_raw_emg(data, subject, adl, display=True)
    data.to_csv("data.csv", index=False)
