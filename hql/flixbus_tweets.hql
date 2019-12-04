create table if not exists flixbus_tweets(
user_id string,
user_location string,
user_followers string,
tweet_time string,
tweet_hashtags string,
No_of_tweets string,
is_retweet string
)
PARTITIONED BY (load_timestamp string)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '|';
