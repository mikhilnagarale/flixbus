#!/usr/bin/python3.6
[DEFAULT]
log_dir = /home/airflow/flixbus/log
access_token_file_name = access_token.txt
current_raw_tweet_file_name = raw_tweet.txt
conf_dir = /home/airflow/flixbus/conf
data_dir = /home/airflow/flixbus/data
base_url = https://api.twitter.com/
current_parsed_tweet_file_name = parsed_tweet.txt
hdfs_tmp = /tmp
processed_partition_file_name = processed_partition.txt
