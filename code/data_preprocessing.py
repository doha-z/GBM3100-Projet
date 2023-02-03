import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split



def display_raw_emg(df: pd.DataFrame, subject: int, channel: int, adl: int):
    """
    Displays a single raw EMG signal with respect to time
    Args:
        df: DataFrame containing the raw emg signals for 22 subjects,
            26 activities of daily living (ADL) and 7 surface electrodes.
        subject: The human subject [1, 22]
        channel: The source electrode [1, 7]
        adl: Activity of daily living [1, 26]
    """

    row = raw_data.loc[(raw_data['subject'] == subject) & (raw_data['ADL'] == adl)]
    time = row['time'].values[0]
    raw_emg = row['raw_emg'].values[0][:, channel]
    sns.lineplot(x=time, y=raw_emg)
    plt.xlabel('time')
    plt.ylabel('Raw EMG signal ')
    plt.title(f'subject: {subject}, Muscle: {channel}, ADL: {adl}')
    plt.show()


def features_lbl(df: pd.DataFrame, adl: list, channel_list: list):
    """

    Args:
        df: DataFrame containing the raw emg signals for 22 subjects,
            26 activities of daily living (ADL) and 7 surface electrodes.
        adl: a list of selected activities of daily living
        channels: a list of selected source electrodes

    Returns:
        features: A feature dataframe with the subject ID and the raw emg signals
                for each selected channel
        labels: a label dataframe containing the ADLs
    """
    # select the wanted ADLs
    feature_mat = df[df['ADL'].isin(adl)]

    # duplicate the emg columns
    for c in channel_list:
        print('c:', c)
        feature_mat = pd.concat([feature_mat, feature_mat['raw_emg'].rename(f'emg_channel_{c + 1}')], axis=1)
        print('columns:', feature_mat.columns)

    # only keep the wanted channel in every column
    for sample in range(len(feature_mat)):
        for c in channel_list:
            print(f'c:{c}, c+1: {c + 1}')
            feature_mat[f'emg_channel_{c + 1}'].values[sample] = feature_mat[f'emg_channel_{c + 1}'].values[sample][:, c]
    label_vec = feature_mat[['ADL']]  # double [] to make it a DataFrame and not a Series

    # we don't need the time column, the label column and the raw_emg column
    feature_mat = feature_mat.drop(columns=['time', 'ADL', 'raw_emg'])
    # todo: feature matrix (encoded) add a column for every emg channel

    return feature_mat, label_vec


def data_splitting(X: pd.DataFrame, y: pd.DataFrame, train_ratio: float, val_ratio: float, test_ratio: float):
    """

    Args:
        X: Feature DataFrame
        y: Label DataFrame
        train_ratio: ratio of data to be in the training dataset
        val_ratio: ratio of data to be in the validation dataset
        test_ratio: ratio of data to be in the test dataset

    Returns:
        split dataset (train val and test)
    """

    X_temp, X_test, y_temp, y_test = train_test_split(X.values, y.values, test_size=test_ratio, random_state=1)
    X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=val_ratio / (val_ratio + train_ratio),
                                                      random_state=2)

    return X_train, X_val, X_test, y_train, y_val, y_test

if __name__ == "__main__":
    # Load the database as a pandas.DataFrame:
    raw_data = pd.read_pickle('data.pkl')
    data = raw_data.copy()

    # Select the subject and the activity of daily life to display
    subject = 1
    channel = 1
    adl = 9
    display_raw_emg(data, subject, channel, adl)

    # select features
    adl_list = [1, 2]
    channel_list = [0, 1, 2]
    features, labels = features_lbl(data, adl_list, channel_list)

    # TODO: data augmentation ?
