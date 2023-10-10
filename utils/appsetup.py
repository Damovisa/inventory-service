import pickle
import os
import numpy as np
import pandas as pd
import datetime as dt

def dosetup():
    # if predict_stock_out.pkl file doesn't exist, create it
    if not os.path.exists('predict_stock_out.pkl'):
        createfile()

def predictdate(ids: list) -> list:
    # return an array of random dates within the next 30 days the same length as the input array
    today = pd.to_datetime('now') # today
    in30days = today + dt.timedelta(days=30) # 30 days from today
    return np.random.choice(pd.date_range(today, in30days), len(ids))

# Save the function into a pickle file
def createfile():
    with open('predict_stock_out.pkl', 'wb') as f:
        pickle.dump(predictdate, f)

