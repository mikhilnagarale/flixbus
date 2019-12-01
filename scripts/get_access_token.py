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
import os

ct=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
logfile_name = '{}_{}{}'.format(sys.argv[0].split('.')[0],ct,'.log')
log_file_path = '{}/{}'.format(config['DEFAULT']['log_dir'],logfile_name)
logging.basicConfig(level=logging.DEBUG,filename=log_file_path,filemode='a')
client_key = 'vYdqq8ZAbiPawJnjk63WB8Lqi'
client_secret = 'YypynQ7riulCJ7Zbf9PQOHLz5rSQiSJZWViHr3z1yeyMbE1log'
key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')
access_token_file_path = '{}/{}'.format(config['DEFAULT']['conf_dir'],config['DEFAULT']['access_token_file_name'])
permission = '744'
change_mode_cmd = '{} {} {}'.format('chmod',permission,access_token_file_path)
auth_url = '{}oauth2/token'.format(config['DEFAULT']['base_url'])

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

def main():
	auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

	access_token = auth_resp.json()['access_token']

	with open(access_token_file_path,"wt") as f:
		f.write(access_token)

	os.system(change_mode_cmd)

if __name__ == "__main__":
	main()
