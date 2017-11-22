import pandas as pd
import datetime 

users = pd.read_csv('../KPI/users.csv', ';')
users = users.drop('Unnamed: 0', 1)

##### FUNCTIONS ##### 
def give_age(user_id):
	age = users[users['user_id'] == user_id]['age'].values[0]
	return age

def userID(id_code):
	user_id = users[users['user_code'] == id_code]['user_id'].values[0]
	return user_id

def to_day(el):
	dt = datetime.datetime.fromtimestamp(el/1000).strftime('%D')
	return dt

def to_hour(el):
	dt = datetime.datetime.fromtimestamp(el/1000).strftime('%H')
	return dt

def swipe_count(swiper):
	df_interm = userSwipes[userSwipes['user_id'] == swiper]
	nb_swipes = df_interm.size / 6
	return nb_swipes

