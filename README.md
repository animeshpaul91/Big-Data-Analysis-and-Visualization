# Data Aggregation, Big Data Analysis and Data Visualization

## This project can be categorized in 3 phases:

### Data Collection (Twitter, NY Times and Common Crawl Data:
The first step involved in the project aimed at collecting data. I have used Sports as the main topic with 4 sub topics - baseball, basketball, football, rugby. There were three data sources in the project - Twitter, NY Times and Common Crawl. Twitter data was directly collected from Twitter API. I downloaded URLs of NY Times news articles from NY Times API. For Common Crawl data, I selected the right WARC file from (https://index.commoncrawl.org/CC-MAIN-2019-13-index?url=Wikipedia.com&output=json) by specifying different domains for url and then downloading the WARC files. This was the most challenging part in the data collection step as Common Crawl data is very vast and I was frequently receiving junk data in the API response. 

### Big Data Analysis on Collected Data: 
This is the meat of the project. Here I wrote mapper and reducer programs for MR Jobs for solving the traditional word count and word co-occurrence problems. Word count computes the count of each word in large datasets while word co-occurrence determines the number of occurrences of each word with every other word. I did an initial preprocessing on the downloaded data. This included data cleaning, stemming, stop-words removal. This processed data is then fed to the MR job in Cloudera Docker platform where Map Reduce Jobs were run for Word Count and Word Co-occurrence. A small subset of the data was initially tested on the MR pipeline just to check for correctness and degree of accuracy. The mappers and reducers turned out to be different for each dataset since the scope of neighbourhood for each word were differenent for each dataset.

### Data Visualization and Ranking: 
The data was then ranked from most frequent to least frequent. For the Word Count task, the word with the highest number of occurrences were ranked first, while for  the Word Co-occurrence task, pairs of words that appeared together with the highest frequencies were ranked at the top. The top 10 words for each task were displayed using Tableau on top of a simple Javascript web application.

### Result in Snaps:
#### Word Count's Top 10 Words:

![Basketball_Twitter](https://github.com/animeshpaul91/Big-Data-Pipeline-with-Hadoop-and-MR/blob/master/Part2/Results/Twitter/Basketball_top10WC.png?raw=true)
![Basketball_NY_Times](https://github.com/animeshpaul91/Big-Data-Pipeline-with-Hadoop-and-MR/blob/master/Part2/Results/NYT/Basketball_top10WC.png?raw=true)
![Basketball_Common_Crawl](https://github.com/animeshpaul91/Big-Data-Pipeline-with-Hadoop-and-MR/blob/master/Part2/Results/CC/Basketball_top10WC.png?raw=true)

#### Word Co-Occurrence Top 10 Words:

![Basketball_Twitter](https://github.com/animeshpaul91/Big-Data-Pipeline-with-Hadoop-and-MR/blob/master/Part3/Word_Cooccurrence/Result_Images/Twitter/Basketball.png?raw=true)
![Basketball_NY_Times](https://github.com/animeshpaul91/Big-Data-Pipeline-with-Hadoop-and-MR/blob/master/Part3/Word_Cooccurrence/Result_Images/NYT/basketball.png?raw=true)
![Basketball_Common_Crawl](https://github.com/animeshpaul91/Big-Data-Pipeline-with-Hadoop-and-MR/blob/master/Part3/Word_Cooccurrence/Result_Images/CC/basketball.png?raw=true)
