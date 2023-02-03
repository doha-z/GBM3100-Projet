import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import data_preprocessing as dp
import numpy as np
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

def fit_and_predict(model, x_fit: np.ndarray, y_fit: np.ndarray, x_pred: np.ndarray, y_true: np.ndarray) :
    """
    Fits a sklearn model using x_fit and y_fit and predicts the labels for x_pred. Returns the F1 score between
    the model predictions and y_pred

    Args:
        model: sklearn model
        x_fit: The samples to fit
        y_fit: The labels to fit
        x_pred: The samples to predict
        y_true: The ground truth labels

    Returns:

    """

    model.fit(x_fit, y_fit)
    y_pred_model = model.predict(x_pred)
    f1 = f1_score(y_true, y_pred_model, average='micro')
    acc = accuracy_score(y_true, y_pred_model)
    cm = confusion_matrix(y_true, y_pred_model)
    print('Training f1 score is:', f1)
    print('Training Accuracy:',acc*100,"%")
    print('Training Confusion Matrix is')
    print(cm)


    return f1, acc, cm

if __name__ == "__main__":
    # load data
    raw_data = pd.read_pickle('data.pkl')
    data = raw_data.copy()

    # select features
    adl_list = [1, 2]
    channel_list = [0, 1, 2]
    features, labels = dp.features_lbl(data, adl_list, channel_list)

    # split dataset
    train_ratio = 0.6
    val_ratio = 0.2
    test_ratio = 0.2

    X_train, X_val, X_test, y_train, y_val, y_test = dp.data_splitting(features, labels, train_ratio, val_ratio,
                                                                       test_ratio)


    model = RandomForestClassifier()
    # train the model
    f1_train, acc_train, cm_train = fit_and_predict(model, X_train, y_train, X_train, y_train)

    # compute the eval metrics on the test
    val_pred = model.predict(X_val)
    f1_val = f1_score(y_val, val_pred, average='micro')
    acc = accuracy_score(y_val, val_pred)
    cm = confusion_matrix(y_val, val_pred)

    print("___________________________________________________")

    print('Validation f1 score is:', f1_val)
    print('Validation Accuracy:', acc * 100, "%")
    print('Validation Confusion Matrix is')
    print(cm)