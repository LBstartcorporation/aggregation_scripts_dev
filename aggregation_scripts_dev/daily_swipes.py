import pandas as pd
from utils_kpis import *


##### LOAD DATA #####
userSwipes = pd.read_csv('../data_whosup/userSwipes.csv')

userSwipes['user_id'] = userSwipes['userId'].apply(userID) 


##### APPLY FUNCTIONS #####
userSwipes['day'] = userSwipes['timestamp'].apply(to_day) 
userSwipes['hour'] = userSwipes['timestamp'].apply(to_hour) 
userSwipes['age'] = userSwipes['user_id'].apply(give_age) 

##### SELECT COLUMNS #####
df_agg = userSwipes[['day', 'user_id', 'age', 'hour', 'isMatch', 'mood']]

##### STOCK #####
df_agg.to_csv('../KPI/daily_swipes.csv', ';')