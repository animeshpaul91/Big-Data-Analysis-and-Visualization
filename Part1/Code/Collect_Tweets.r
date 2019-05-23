## access token method: create token and save it as an environment variable

library(rtweet)
library(data.table)
library(dplyr)

create_token(
  app = "DIC_EDA_1",
  consumer_key = "pcEvrIV5zHuvoOaCHKOomk9FE",
  consumer_secret = "6c7M5OhGT32U7YfSADVYYhwvdfOcW8gA9ZQykJoTbZhhY16yaq",
  access_token = "130485979-Tj65oVh6VBlVKIN7Rli93ZpChUVdZXQTOhGScMov",
  access_secret = "yFUW8Nup7MYK0TQAecbVB9uBgbimSGkJpR5XRJ54YhvFS")

terms <- c("baseball", "basketball", "football", "rugby") #sub-topics

for (term in terms){

rt <- search_tweets(
  paste("#", term), n = 5000, geocode = lookup_coords("usa"), include_rts = FALSE, retryonratelimit = TRUE
) #rt will contain lot of Junk Tweets

#Data Processing
rt <-unique( rt[ , ] ) #Removes Duplicates
rt <- dplyr::filter(rt, grepl("baseball", text)) #Fetches Tweets containing relevant words
fwrite(rt, file = sprintf("~/DIC_Project2/Twitter_Data/%s.csv", term), row.names = FALSE, col.names = TRUE, sep = ",", append = TRUE)

}

# Extract Tweet Text and save it on Disk
for (term in terms)
{
  rt_matrix <- read.csv(file=sprintf("./CSVs/%s.csv", term), header=TRUE, sep=",")
  x <- rt_matrix[1:5000, 5, drop=FALSE]
  write.table(x, file = sprintf("./%s.txt", term), sep = "\t", row.names = FALSE)
}
