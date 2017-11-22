import pandas as pd


##### LOAD DATA #####
userSwipes = pd.read_csv('../KPI/daily_swipes.csv', ';')
users = pd.read_csv('../KPI/users.csv', ';')


##### USER JOIN #####
swipers = list(set(list(userSwipes['user_id'])))

def swipe_count(swiper):
	df_interm = userSwipes[userSwipes['user_id'] == swiper]
	nb_swipes = df_interm.size / 6
	return nb_swipes

def match_count(swiper):
	df_interm = userSwipes[userSwipes['user_id'] == swiper]
	df_interm = df_interm[df_interm['isMatch'] == True]
	nb_swipes = df_interm.size / 6
	return nb_swipes


##### FUNCTIONS #####
users['nb_swipes'] = users['user_id'].apply(swipe_count) 
users['nb_match'] = users['user_id'].apply(match_count) 


##### STOCK #####
users.to_csv('../KPI/users.csv', ';')