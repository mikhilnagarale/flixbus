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

ct=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
logfile_name = '{}_{}{}'.format(sys.argv[0].split('.')[0],ct,'.log')
log_file_path = '{}/{}'.format(config['DEFAULT']['log_dir'],logfile_name)
logging.basicConfig(level=logging.DEBUG,filename=log_file_path,filemode='a')
current_raw_tweet_file_path = '{}/{}'.format(config['DEFAULT']['conf_dir'],config['DEFAULT']['current_raw_tweet_file_name'])

current_parsed_tweet_file_path = '{}/{}'.format(config['DEFAULT']['conf_dir'],config['DEFAULT']['current_parsed_tweet_file_name'])

try:
	with open(current_raw_tweet_file_path,"rt") as f:
		source_file_name = f.read()
except IOError as e:
	logging.error(e)
	sys.exit()

target_file_name = '{}_{}{}'.format('flixbus_parse_tweets',ct,'.txt')
source_file_path = config['DEFAULT']['data_dir']+'/'+source_file_name
target_file_path = config['DEFAULT']['data_dir']+'/'+target_file_name



with open(target_file_path,"wt") as tf:
	with open(source_file_path,"rt") as sf:
		for line in sf.read().splitlines():
			tweet_json=json.loads(line)
			source=tweet_json['source']
			user_id=tweet_json['user']['id']
			user_location=tweet_json['user']['location']	
			follower_count=tweet_json['user']['followers_count']		
			tweet_date_time=tweet_json['created_at']
			hashtag_list=list(map(lambda x: x['text'],tweet_json['entities']['hashtags']))
			Tweet_Count=tweet_json['user']['statuses_count']	
			is_retweet=tweet_json['retweeted']
			result_set = '{}|{}|{}|{}|{}|{}|{}"\n"'.format(str(user_id),repr(user_location),str(follower_count),str(tweet_date_time),str(hashtag_list),str(Tweet_Count),str(is_retweet))
			tf.write(result_set)


with open(current_parsed_tweet_file_path,"wt") as f:
	f.write(target_file_name)



