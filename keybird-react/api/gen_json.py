import tensorflow as tf
import os
import librosa
import math
import json

import numpy as np
import tensorflow.keras as keras
import matplotlib.pyplot as plt
import pandas as pd

DATASET_PATH = "gen_file"
JSON_PATH = "predict_this_5.json"
SAMPLE_RATE = 22050

## NEED TO UPDATE TO BE DYNAMIC
DURATION = 30 # measured in seconds, but wont work for us in the long term
##

SAMPLES_PER_TRACK = SAMPLE_RATE * DURATION

# identify the specific track duration
## frames, sample rate --> duration

# split the duration into 3 second segments
## send the number of segments into the save_mfcc function
## update the SAMPLES_PER_TRACK variable used in save_mfcc

#path = os.getcwd() + "/keybird-react/api/"
#os.chdir(path)
def save_mfcc(dataset_path, json_path, n_mfcc=13, n_fft=2048, hop_length=512, num_segments=10):
    # build a dictionary to store data
    data = {
        "mapping": [], #"mapping": ["clacky","thocky"], # 0 = clacky, 1 = thocky
        "labels": [], # target outputs
        "mfcc": [] # training inputs
    }
    
    num_samples_per_segment = int(SAMPLES_PER_TRACK / num_segments)
    expected_num_mfcc_vectors_per_segment = math.ceil(num_samples_per_segment / hop_length) # 1.2 -> 2
    
    # loop through all genres
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):
        print('\n dirpath: {},\n dirnames: {},\n filenames: {}'.format(dirpath,dirnames,filenames))
        
        # ensure that we are not at the root level
        if dirpath is dataset_path:
            # save the semantic
            dirpath_components = dirpath.split("/") # genre/blues ==> ["genre", "blues"]
            semantic_label = dirpath_components[-1]
            data["mapping"].append(semantic_label)
            print("\n Processing {}".format(semantic_label))
            
            # process files for a specific genre
            for f in filenames:
                
                # load audio file
                file_path = os.path.join(dirpath, f)
                signal, sr = librosa.load(file_path, sr=SAMPLE_RATE)
                f_duration = librosa.get_duration(y=signal, sr=sr)
                
                # num segments is dependent on the duration / 3 second intervals
                new_num_segments = int(f_duration / 3)
                
                # process segments extracting mfcc and storing data
                
                #for s in range(new_num_segments): -- commenting out the dynamic segment piece
                for s in range(num_segments):    
                    # re-calculate based on specific file --commented out
                    #num_samples_per_segment = int((SAMPLE_RATE * f_duration) / new_num_segments)
                    
                    # reverting to static for now
                    num_samples_per_segment = int((SAMPLE_RATE * DURATION) / num_segments)
                    expected_num_mfcc_vectors_per_segment = math.ceil(num_samples_per_segment / hop_length) # 1.2 -> 2
                    #
                    
                    start_sample = num_samples_per_segment * s 
                    finish_sample = start_sample + num_samples_per_segment
                    
                    mfcc = librosa.feature.mfcc(y=signal[start_sample:finish_sample],
                                                sr=sr,
                                                n_fft=n_fft,
                                                n_mfcc=n_mfcc,
                                                hop_length=hop_length
                                               )
                    
                    mfcc = mfcc.T 
                    # store mfcc for segment only if it has the expected length
                    if len(mfcc) == expected_num_mfcc_vectors_per_segment:
                        data["mfcc"].append(mfcc.tolist())
                        data["labels"].append(i-1)
                        print("{}, segment:{}".format(file_path, s))                  
    with open(json_path, "w") as fp:
        json.dump(data, fp, indent=4)    

def load_data(data_path):
    """Loads training dataset from json file.
        :param data_path (str): Path to json file containing data
        :return X (ndarray): Inputs
        :return y (ndarray): Targets
    """

    with open(data_path, "r") as fp:
        data = json.load(fp)

    X = np.array(data["mfcc"])
    y = np.array(data["labels"])
    return X, y

def predict(model, X):
    """Predict a single sample using the trained model
    :param model: Trained classifier
    :param X: Input data
    :param y (int): Target
    """

    # add a dimension to input data for sample - model.predict() expects a 4d array in this case
    X = X[np.newaxis, ...] # array shape (1, 130, 13, 1)

    # perform prediction
    prediction = model.predict(X)

    # get index with max value
    predicted_index = np.argmax(prediction, axis=1)

    print("Predicted label: {}".format(predicted_index))
    return(predicted_index)

if __name__ == "__main__":
    save_mfcc(DATASET_PATH, JSON_PATH, num_segments=60) # num_segments back to being used

    # access predict_this.json
    PREDICTION_PATH = "predict_this_5.json"
    # load data
    X_p, y_p = load_data(PREDICTION_PATH)
    X_p = X_p[..., np.newaxis]
    
    # load model
    
    new_model = keras.models.load_model('my_model.h5')
    #new_model.summary()

    clacky = 0
    clicky = 0
    muted = 0
    silent = 0
    thocky = 0

    for i in X_p:
        prediction = predict(new_model, i)
        if prediction == 0:
            clacky += 1
        elif prediction == 1:
            clicky += 1
        elif prediction == 2:
            muted += 1
        elif prediction == 3:
            silent += 1
        elif prediction == 4:
            thocky += 1
    
    total = len(X_p)/100
    print('\n Your Keyboard is: \n  {:.2f}% Clacky \n  {:.2f}% Clicky \n  {:.2f}% Muted \n  {:.2f}% Silent \n  {:.2f}% Thocky'.format(clacky/total, clicky/total,muted/total, silent/total, thocky/total))
    outputDict = {"clacky": clacky, "clicky": clicky, "muted": muted, "silent": silent, "thocky": thocky, "total": int(total*100)}
    with open("outputJson.json", "w") as outfile:
        json.dump(outputDict, outfile, indent=4)