import pandas as pd


##### LOAD & CLEAN USER FILE #####
users = pd.read_csv('../KPI/users.csv', ';')
users = users.drop('Unnamed: 0', 1)

def userID(id_code):
	user_id = users[users['user_code'] == id_code]['user_id'].values[0]
	return user_id


##### INITIALIZATION AGES ##### 
signIns = pd.read_csv('../data_whosup/signIns.csv')
signIns['user_id'] = signIns['userId'].apply(userID) 

def give_first_age(id_code):
	ages = list(signIns[signIns['user_id'] == id_code]['age'])
	if len(ages) != 0:
		return ages[-1]
	else:
		return 'null'


##### FUNCTIONS #####
users['age'] = users['user_id'].apply(give_first_age)


##### STORE #####
users.to_csv('../KPI/users.csv', ';')