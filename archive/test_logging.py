import logging

log_dir='/home/airflow/flixbus/log'
log_file=''
logging.basicConfig(level=logging.DEBUG)

logging.debug('this is debug')
logging.info('this is info')
logging.warning('this is warning')
logging.error('this is error')
logging.critical('this is critical')


