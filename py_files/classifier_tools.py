from sklearn.linear_model import LogisticRegression
import soundfile as sf
import numpy as np
import pickle

def get_data(wav_names):
    all_data = []

    for wav_filename in wav_names:
        data, _ = sf.read(wav_filename)
        all_data.append(data)

    all_data = np.vstack(([i for i in all_data]))

    return all_data

def get_statistics(data):

    stats = [np.mean(data, axis=1),
            np.std(data, axis=1),
            np.max(data, axis=1),
            np.min(data, axis=1)]

    stats = [i.reshape(-1, 1) for i in stats]
    
    stats = np.hstack((stats))    
    return stats

def get_logreg(weights_path):
    with open(weights_path, 'rb') as file:  
        model = pickle.load(file)
    return model

    