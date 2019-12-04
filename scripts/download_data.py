#!/usr/bin/python3.6
import configparser
config = configparser.ConfigParser()
config.read('/home/airflow/flixbus/conf/conf.py')
import sys
import base64
import requests
import json
import logging
import datetime

#ct (current time)
ct=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
logfile_name = '{}_{}{}'.format(sys.argv[0].split('.')[0],ct,'.log')
log_file_path = '{}/{}'.format(config['DEFAULT']['log_dir'],logfile_name)
logging.basicConfig(level=logging.DEBUG,filename=log_file_path,filemode='a')
access_token_file_path = '{}/{}'.format(config['DEFAULT']['conf_dir'],config['DEFAULT']['access_token_file_name'])
access_token=''
current_raw_tweet_file_path = '{}/{}'.format(config['DEFAULT']['conf_dir'],config['DEFAULT']['current_raw_tweet_file_name'])
target_file_name = '{}_{}{}'.format('flixbus_tweets',ct,'.txt')
file_path = config['DEFAULT']['data_dir']+'/'+target_file_name
processed_date=''
processed_partition_file_path = '{}/{}'.format(config['DEFAULT']['conf_dir'],config['DEFAULT']['processed_partition_file_name'])


def main():
	try:
		with open(access_token_file_path,'rt') as f:
			access_token=f.read()
	except IOError as e:
		logging.error(str(e))
		sys.exit()
	
	try:
		with open(current_raw_tweet_file_path,'wt') as f:
			f.write(target_file_name)
	
	except IOError as e:
		logging.error(e)
	
	search_headers = {
		'Authorization': 'Bearer {}'.format(access_token)
	}
		
	search_params = {
	'q': '#FlixBus',
	'result_type': 'recent',
	'count': 50,
	'include_entities' : 'true'
	}
	
	
	#Adding changes to set fromDate to previous processed date to fetch only last day data/after previously processed data.

	try:
		with open(processed_partition_file_path,"rt") as f:
			processed_date = f.read()
		#if processed_date != '':
			#search_params['fromDate'] = processed_date
	except IOError as e:
		logging.error(e)
	
	
	search_url = '{}1.1/search/tweets.json'.format(config['DEFAULT']['base_url'])
	
	search_resp = requests.get(search_url, headers=search_headers, params=search_params)
	
	tweet_data = search_resp.json()

	try:
		if len(tweet_data['statuses']) == 0:
			with open(current_raw_tweet_file_path,'wt') as f:
				f.write('')
			sys.exit(0)
	except IOError as e:
		logging.error(1)

	
	
	try:
		with open(file_path,'wt') as f:
			for line in tweet_data['statuses']:
				f.write(json.dumps(line)+"\n")

	except IOError as e:
		logging.error(e)
	
	
	while 'next_results' in search_resp.json()['search_metadata'].keys():
		since_id = search_resp.json()['search_metadata']['since_id']
		max_id = search_resp.json()['search_metadata']['next_results'].split('max_id=')[1].split('&')[0]
		search_params['max_id'] = max_id
		search_params['since_id'] = since_id
		search_resp = requests.get(search_url, headers=search_headers, params=search_params)
		tweet_data = search_resp.json()
		try:
			with open(file_path,'at') as f:
				for line in tweet_data['statuses']:
					f.write(json.dumps(line)+"\n")
		except IOError as e:
			logging.error(str(e))
			sys.exit()

	#Adding current date in processed partition file to pick it next run to process next set of records
	try:
		with open(processed_partition_file_path,"wt") as f:
			f.write(ct[0:8])
	except IOError as e:
		logging.error(e)



if __name__ == "__main__":
	main()



