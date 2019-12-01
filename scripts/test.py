#!/home/airflow/.sandbox/bin/python
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


logdir = '/home/airflow/flixbus/log'
logfile_name = '{}_{}{}'.format(sys.argv[0].split('.')[0],ct,'.log')
log_file_path = '{}/{}'.format(logdir,logfile_name)


print(log_file_path)
print(str(config['DEFAULT']['log_dir']))

logfile_name = '{}_{}{}'.format(sys.argv[0].split('.')[0],ct,'.log')
log_file_path = '{}/{}'.format(config['DEFAULT']['log_dir'],logfile_name)

print(log_file_path)
