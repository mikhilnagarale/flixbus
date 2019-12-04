# flixbus

This is a processing pipeline for Tweets for FlixBus. Below are the steps-

- searching for last week tweets with hashtag #FlixBus in tweeter search.
- download the data in text file.
- extract the required fields from data.
	- Anonymized User id 
	- Location of the user 
	- Number of followers 
	- Date time of the tweet 
	- Hashtag (including all hashtags included in the tweet) 
	- Number of tweets 
	- Is it a retweet? 
- Store the transformed data in text file.
- copy the transformed text file to HDFS.
- Load the transformed data in hive table with partition as load_timestamp.
	
- Logging is implemented using 'logging' package. This is being overriden while running airflow dag by airflow. 
  This will be usefull while running/testing any script manually.

References

- Tweeter Standard Search API: https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
 
- Request package use: https://realpython.com/api-integration-in-python/
 
- Tweeter Standard Search API response Object: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object
 
- Tweeter Barer Token: https://developer.twitter.com/en/docs/basics/authentication/guides/bearer-tokens
 
- Next results in search request: https://developer.twitter.com/en/docs/tweets/timelines/guides/working-with-timelines
 
- Auth2 use: https://requests.readthedocs.io/en/master/user/authentication/
 
- Auth2 Authentication Twitter: https://developer.twitter.com/en/docs/basics/authentication/api-reference/token
 
- How to use Twitter App Auth: https://developer.twitter.com/en/docs/basics/authentication/overview/application-only
 
- String to byte: https://stackoverflow.com/questions/7585435/best-way-to-convert-string-to-bytes-in-python-3
 
- base64 encoding in python : https://stackoverflow.com/questions/23164058/how-to-encode-text-to-base64-in-python
 
- how to send header in python request.post : https://stackoverflow.com/questions/10768522/python-send-post-with-header
 


For suggestion please drop me mail on 'mikhil.nagarale@gmail.com'.

Thank You!
