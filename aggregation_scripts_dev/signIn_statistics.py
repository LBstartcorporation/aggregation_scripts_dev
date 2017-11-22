import pandas as pd
from utils_kpis import *


##### LOAD DATA #####
signIns = pd.read_csv('../data_whosup/signIns.csv')
signIns['user_id'] = signIns['userId'].apply(userID) 


##### APPLY FUNCTIONS ##### 
signIns['day'] = signIns['timestamp'].apply(to_day) 
signIns['hour'] = signIns['timestamp'].apply(to_hour) 


##### SELECT COLUMNS #####
df_agg = signIns[['user_id', 'age', 'timestamp', 'day', 'hour', 'latitude', 'longitude']]

##### STOCK #####
df_agg.to_csv('../KPI/signIn_statistics.csv', ';')