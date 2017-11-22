import pandas as pd

##### LOAD DATA #####
instantHistory = pd.read_csv('../data_whosup/instantHistory.csv')
signIns = pd.read_csv('../data_whosup/signIns.csv')
userSwipes = pd.read_csv('../data_whosup/userSwipes.csv')
moodActivates = pd.read_csv('../data_whosup/moodActivations.csv')


##### GET ALL USER IDS #####
users_code = []

for i in instantHistory['_id']:
	users_code.append(i)
for i in signIns['userId']:
	users_code.append(i)
for i in userSwipes['userId']:
	users_code.append(i)
for i in moodActivates['userId']:
	users_code.append(i)


##### CONCAT ALL USERS + USER CODE #####
users = list(set(users_code))
user_ids = range(0, len(users))


##### TO DATAFRAME #####
user_list = [user_ids, users]

df_user = pd.DataFrame(user_list).transpose()
df_user.columns = ['user_id', 'user_code']

##### STOCK #####
df_user.to_csv('../KPI/users.csv', ';')