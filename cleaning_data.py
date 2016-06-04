import numpy as np 
import pandas as pd 

data = pd.read_csv('data.csv')

predicting_set = data.loc[data['shot_made_flag'].isnull() , :]
training_data = data.loc[ data['shot_made_flag'].notnull() , :]
predicting_set.to_csv('predicting_set.csv')
data.to_csv('training_set.csv')