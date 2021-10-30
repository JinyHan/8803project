from extractclocation import getcarmenloc
from hydrator import tweetshydrator


#reference
#https://github.com/thepanacealab/covid19_twitter/blob/master/COVID_19_dataset_Tutorial.ipynb

#Twitter API credentials
keyfile = r'api_keys.json'  

#Example
#https://t.co/GUKc1bFXCF?amp=1
rawfile = r'data\chinese_tbcov.tsv'

#output file
hydrated_file = r'hydrated_tweets.json'
  
#hydrate
tweetshydrator(rawfile,hydrated_file,keyfile)

#get carmen location
hydrated_file = r'hydrated_tweets.json'
carmen_file = r'hydrated_tweets_carmen.json'
getcarmenloc(hydrated_file,carmen_file)


    
    