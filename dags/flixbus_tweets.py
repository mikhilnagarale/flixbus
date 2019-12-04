# load the dependencies
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.hive_operator import HiveOperator
from datetime import date, timedelta, datetime
import configparser
config = configparser.ConfigParser()
config.read('/home/airflow/flixbus/conf/conf.py')

import download_data
import transform_tweets
import get_access_token 
import check_api_status

current_time = datetime.now().strftime("%Y%m%d%H%M%S")

# default_args are the default arguments applied to the DAG and all inherited tasks
DAG_DEFAULT_ARGS = {
	'owner': 'airflow',
	'depends_on_past': False,
	'retries': 1,
	'retry_delay': timedelta(minutes=1)
}

raw_file_name = config['DEFAULT']['conf_dir']+"/"+config['DEFAULT']['current_parsed_tweet_file_name']
parsed_file_name = ''

with open(raw_file_name,"rt") as f:
	parsed_file_name = f.read()

parsed_file_path = config['DEFAULT']['data_dir']+"/"+parsed_file_name
hdfs_parsed_file_path = config['DEFAULT']['hdfs_tmp']+"/"+parsed_file_name

with DAG('flixbus_tweets_dag_v2', start_date=datetime(2018, 10, 1), schedule_interval="@daily", default_args=DAG_DEFAULT_ARGS, catchup=False) as dag:
	check_api_status_task = PythonOperator(task_id='check_api_status_task',python_callable=check_api_status.main)
	get_access_token_task = PythonOperator(task_id='get_access_token_task',python_callable=get_access_token.main)
	download_tweets_task = PythonOperator(task_id='download_tweets_task',python_callable=download_data.main)
	transform_tweets_task = PythonOperator(task_id='transform_tweets_task',python_callable=transform_tweets.main)
	copy_to_hdfs_task = BashOperator(task_id='copy_to_hdfs_task', bash_command="hadoop fs -put -f "+parsed_file_path+" /tmp")
	load_hive_table_task = HiveOperator(task_id='load_hive_table_task',hql='LOAD DATA INPATH \'{}\' into table flixbus_tweets PARTITION(load_timestamp=\'{}\')'.format(hdfs_parsed_file_path,current_time))

	check_api_status_task >> get_access_token_task >> download_tweets_task >> transform_tweets_task >> copy_to_hdfs_task >> load_hive_table_task
	
		
