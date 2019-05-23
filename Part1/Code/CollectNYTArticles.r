library(nytimes)
library(jsonlite)
library(httr)
library(dplyr)

my_api_key = "yuzZdXGon9jJ5ukJvYpfV8IpBK9eEXJA"
terms <- list("rugby","cricket","basketball", "football")
begin_date <- "20190101" 
end_date <- "20190331"

for (term in terms)
  {
    baseurl <- paste0("http://api.nytimes.com/svc/search/v2/articlesearch.json?q=",term,
                      "&begin_date=",begin_date,"&end_date=",end_date,
                      "&facet_filter=true &api-key=",my_api_key, sep="")
    
    initialQuery <- fromJSON(baseurl)
    maxPages <- round((initialQuery$response$meta$hits[1] / 10)-1)

    pages <- list()
    for(i in 0:maxPages)
      {
          tryCatch(nytSearch <- fromJSON(paste0(baseurl, "&page=", i), flatten = TRUE) %>% data.frame(), error=function(e) Sys.sleep(10))
          message("Retrieving page ", i)
          pages[[i+1]] <- nytSearch
          #Sys.sleep(10)
      }
    
    allNYTsearch <- rbind_pages(pages)
    uniq_url <- unique(allNYTsearch$response.docs.web_url) #Eliminates Duplicates
    uniq_url <- uniq_url[grepl(term, uniq_url)] #Fetching Relevant Articles only
    write(uniq_url, file = sprintf("./%s_web_url.txt", term), append = TRUE, sep = "\n")
 }
