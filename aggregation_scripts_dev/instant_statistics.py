import pandas as pd
from utils_kpis import *


##### LOAD DATA #####
instantHistory = pd.read_csv('../data_whosup/instantHistory.csv')


##### FUNCITONS #####
def members_in_instant(_id):
	members_in_instant = instantHistory[instantHistory['_id'] == _id]['members'].values[0]
	nb_members_in_instant = len(members_in_instant.split('_id'))
	return nb_members_in_instant

def count_messages(messages):
	nb_messages = len(messages.split('author'))
	return nb_messages

##### APPLY FUNCTIONS ##### PAS DE DATE POUR LE MOMENT
#instantHistory['day'] = instantHistory['timestamp'].apply(to_day) 
#instantHistory['hour'] = instantHistory['timestamp'].apply(to_hour) 
instantHistory['participants'] = instantHistory['_id'].apply(members_in_instant) 
instantHistory['nb_messages'] = instantHistory['messages'].apply(count_messages) 

##### SELECT COLUMNS #####
df_agg = instantHistory[['participants', 'hashtag', 'mood', 'nb_messages']]

##### STOCK #####
df_agg.to_csv('../KPI/instant_statistics.csv', ';')