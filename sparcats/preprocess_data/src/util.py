import numpy as np


# Define a function to create the dataset for the LSTM model
def create_dataset(signal, window_size=20):
    X, y = [], []
    for i in range(len(signal) - window_size):
        X.append(signal[i:i + window_size])
        y.append(signal[i + window_size])
    return np.array(X), np.array(y)
