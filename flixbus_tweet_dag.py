# load the dependencies
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.hive_operator import HiveOperator
from datetime import date, timedelta, datetime

import download_data
import transform_tweets
import get_access_token 

# default_args are the default arguments applied to the DAG and all inherited tasks
DAG_DEFAULT_ARGS = {
	'owner': 'airflow',
	'depends_on_past': False,
	'retries': 1,
	'retry_delay': timedelta(minutes=1)
}

with DAG('flixbus_tweets_dag_v2', start_date=datetime(2018, 10, 1), schedule_interval="@daily", default_args=DAG_DEFAULT_ARGS, catchup=False) as dag:
	get_access_token_task = PythonOperator(task_id='get_access_token_task',python_callable=get_access_token.main)
	download_tweets_task = PythonOperator(task_id='download_tweets_task',python_callable=download_data.main)
	transform_tweets_task = PythonOperator(task_id='transform_tweets_task',python_callable=transform_tweets.main)
	get_access_token_task >> download_flixbus_tweets_task >> transform_tweets_task
		
