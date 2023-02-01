import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import pandas as pd
import seaborn as sns
from database_loading import get_raw_emg

# TODO:
# dictionnaire des ADL et mouvement associé
# drop the time column ?

if __name__ == "__main__":

    raw_data = pd.read_csv('data.csv')
    subject = 1
    adl = 9
    time_vector, raw_emg_values = get_raw_emg(raw_data, subject, adl, display=True)

    #features = pd.DataFrame
    #labels = None