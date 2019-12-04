# flixbus

This is a processing pipeline for Tweets for FlixBus. Below are the steps-

-searching for last week tweets with hashtag #FlixBus in tweeter search.
-download the data in text file.
-extract the required fields from data.
	- Anonymized User id 
	- Location of the user 
	- Number of followers 
	- Date time of the tweet 
	- Hashtag (including all hashtags included in the tweet) 
	- Number of tweets 
	- Is it a retweet? 
-Store the transformed data in text file.
-copy the transformed text file to HDFS.
-Load the transformed data in hive table with partition as load_timestamp.
	
- Logging is implemented using 'logging' package. This is being overriden while running airflow dag by airflow. 
  This will be usefull while running/testing any script manually.

For suggestion please drop me mail on 'mikhil.nagarale@gmail.com'.

Thank You!
