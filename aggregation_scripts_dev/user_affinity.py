import pandas as pd
from utils_kpis import *
import numpy as np

##### LOAD DATA #####
userSwipes = pd.read_csv('../data_whosup/userSwipes.csv')
users = pd.read_csv('../KPI/users.csv', ';')
users = users.drop('Unnamed: 0', 1)


def userIDS(id_code):
	#print id_code
	try:
		user_id = users[users['user_code'] == id_code]['user_id'].values[0]
		return user_id
	except:
		return 0

userSwipes['user_id'] = userSwipes['userId'].apply(userID) 
userSwipes['swiped_id'] = userSwipes['swipedId'].apply(userIDS) 


##### APPLY FUNCTIONS #####
userSwipes['day'] = userSwipes['timestamp'].apply(to_day) 
userSwipes['hour'] = userSwipes['timestamp'].apply(to_hour) 


##### SELECT COLUMNS #####
df_agg = userSwipes[['user_id', 'swiped_id', 'day', 'hour', 'isMatch', 'mood']]



##### BUILD MATRIX #####
length = max(list(users['user_id'])) + 1
mat = np.zeros((length, length))


##### FILL MATRIX #####
user_list = list(set(list(df_agg['user_id'])))

for i in user_list:
	user_swipes = df_agg[df_agg['user_id'] == i]
	swiped = list(user_swipes['swiped_id'])

	for j in swiped:
		mat[i][j] += 1

correl_matrix = pd.DataFrame(mat)

for i in range(0, length):
	for j in range(0, length):
		val_cell = mat[i][j]
		if val_cell != 0.0:
			print 'user ', i, ' likes user ', j, '  COEF ', val_cell

##### STOCK #####
correl_matrix.to_csv('../KPI/user_affinity.csv', ';')