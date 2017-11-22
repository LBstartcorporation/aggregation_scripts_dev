import pandas as pd
from utils_kpis import *


##### LOAD DATA #####
moodActivates = pd.read_csv('../data_whosup/moodActivations.csv')

moodActivates['user_id'] = moodActivates['userId'].apply(userID) 


def users_in_mood(_id):
	users_in_mood = moodActivates[moodActivates['_id'] == _id]['userIdsInMood'].values[0]
	nb_users_in_mood = len(users_in_mood.split(','))
	return nb_users_in_mood


##### APPLY FUNCTIONS #####
moodActivates['day'] = moodActivates['timestamp'].apply(to_day)
moodActivates['hour'] = moodActivates['timestamp'].apply(to_hour)
moodActivates['age'] = moodActivates['user_id'].apply(give_age)
moodActivates['users_in_mood'] = moodActivates['_id'].apply(users_in_mood)

##### SELECT COLUMNS #####
df_agg = moodActivates[['day', 'user_id', 'age', 'hour', 'mood', 'users_in_mood']]

##### STOCK #####
df_agg.to_csv('../KPI/daily_mood_activations.csv', ';')