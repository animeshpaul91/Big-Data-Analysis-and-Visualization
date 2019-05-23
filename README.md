Please use this report as read-me guide in running the codes and reproducing the results:

We have used Sports as our main topic with 4 sub topics - baseball, basketball, football, rugby.

Part1:
1. This folder contains 2 sub folders - Code and Data.
2. The Code folder contains the code for data collection over all the 3 data sources.
3. 'Collect_Tweets.r' is used for collecting tweets. The data is saved in the local directory. The code downloads 5000 tweets for each sub-topic thereby making the total tweet count to 20,000.
4. 'CollectNYTArticles.r' fetches the URLs of articles of our interest. This script dumps the URLs to file. Parse_NYT_URLS.py fetches the text of the article by individually hitting thise URLs using beautiful soup. You can refer to the topic_web_url.txt file to find out the number of articles.
5. For Common Crawl data, we are selecting the right WARC file from (https://index.commoncrawl.org/CC-MAIN-2019-13-index?url=Wikipedia.com&output=json) by specifying different domains for url and then downloading the WARC files.
6. The 'cc_get_urls.py' fetches all the URLs in the warc. This generates 'topic_urls.txt' file. You can refer to the this file to find out the number of articles. This is written in Python2. A separate Python 3 script (cc_get_content.py) has been written to fetch the content using beautiful soup.
7. All the data has been moved to the 'Data' directory.

Part 2:
1. This part only has the 'mapper.py' and 'reducer.py' for the Word Count Problem. The result images are placed in Results directory. A prior pre-processing id done before running the MR jobs. This is explained in Part 3.

Part 3:
This is the meat of the Project.
1. There are two directories. Word Count and Word Co-occurrence.
2. In the Word Count, all the data that has been generated from Part1 has been placed in the Input directory.
3. The 'preprocess.py' does all the preprocessing (data cleaning, stemming, stop-words removal) and dumps the processed input for MR job into the Processed directory.
4. This processed data is then fed to the MR job in Cloudera Docker with 'mapper.py' as the mapper and 'reducer.py' as the reducer for Word Count. The results are placed in the 'Results' directory. You can have a look and cross-cjheck them.
5. A small subset of the data was initially tested on the MR pipeline. We have included this in the 'Small_Data' folder. This does the same thing for the small data.
6. For the Word Co-occurrence problem, we have documented all the files in the 'Word_Cooccurrence' directory.
7. The mappers and reducers are different for different datasets here since we have to define the neighbourhood for each word. Each folder ('Twitter', 'NYT', 'CC') has its own mapper.py and reducer.py.
8. The input directory already contains the processed input from step 3. On this, the MR job is run with the corresponding mapper and reducers to get the desired results. The results have been placed in the 'Results' directory. The images have been placed in the 'Result_Images' directory.
9. All the visualizations have been done in Tableau. Please refer to these links to view them in detail.
    9.1 https://public.tableau.com/profile/soumya.mitra5275#!/vizhome/PA_2_Viz/Sheet1?publish=yes - Word Counts
    9.2 https://public.tableau.com/profile/soumya.mitra5275#!/vizhome/PA_2_Viz_Coocc/Sheet2?publish=yes - Word Co-Occurrence



WebPage:
1. A simple web page in Javascript is developed to display the top 10 words with their counts and their highest co-occurrences.
2. Please refer to 'SimpleViz_WordCount.html' to view Word Counts.
3. Please refer to 'SimpleViz_WordCo-occurance.html' to view Word Co-Occurrences.
4. The code is placed in 'script.js'.

Video: 
1. There is a sequence of 2 videos - Video1 and Video2 because the first recording stopped at 10-minute mark. Please have a look at both. Link to both vieos in UBBOX are: 
2. https://buffalo.box.com/s/y2zpstjwqd1233a0na0lg3kwe20bse8a - First Video 
3. https://buffalo.box.com/s/oz9b91urfryqprrylw6ougdpymtf670j - Second Video


Note: the WARC files had been downloaded in the local file system to get CC data. They have not been uploaded in the ZIP nor UB BOX due to their size. You may download the first WARC file from
1. https://index.commoncrawl.org/CC-MAIN-2019-13-index?url=mlb.com&output=json for Baseball
2. https://index.commoncrawl.org/CC-MAIN-2019-13-index?url=fifa.com&output=json for Football
3. https://index.commoncrawl.org/CC-MAIN-2019-13-index?url=nba.com&output=json for Basketball
4. https://index.commoncrawl.org/CC-MAIN-2019-13-index?url=rugbyworld.com&output=json for Rugby
And place them in Part1/Code/<Topic>/ to run CC code 


The Word Cooccurrence Input for CC is uploaded to UBBOX. I could not upload this is timberlake. disk space quota had exceeded. The Input files are kept at. 
https://buffalo.box.com/s/1e0rtb5kv83ynaj13fqbawavdlrrjd24. Please place them to ./Part3/WordCooccurrence/input/CC if you want to run those scripts.


