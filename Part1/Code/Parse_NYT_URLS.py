import requests
from bs4 import BeautifulSoup
from os import path

subTopics = ["baseball", "basketball", "football", "rugby"]
for subTopic in subTopics:
    url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q=" + subTopic + "&begin_date=20190101&api-key=yuzZdXGon9jJ5ukJvYpfV8IpBK9eEXJA"
    r = requests.get(url)
    data = r.json()
    a = data["response"]["docs"]
    urlFileName = subTopic + "_web_url.txt"
    contentFileName = subTopic + "_content.txt"
    with open(urlFileName, "a+") as write_file:
        for b in a:
            write_file.write(b["web_url"] + "\n")
    urlList = []
    with open(urlFileName, "r") as read_file:
        while(read_file.readline() != ''):
            c = read_file.readline()
            c = c[:-1]
            if(c != ''):
                urlList.append(c)
    urlSet = set(urlList)
    with open(urlFileName, "w") as write_file:  # , open(contentFileName,"a+") as write_file1:
        for url in urlSet:
            write_file.write(url + "\n")
    content = ''
    totalContent = ''
    if(path.exists(contentFileName)):
        cfile = open(contentFileName, "r+")
        content = cfile.read().split("\n")
        cfile.seek(0)
        cfile.truncate()
    with open(contentFileName, "a+") as write_file1:
        for url in urlSet:
            content = str(requests.get(url).content)
            soup = BeautifulSoup(content, features="html5lib")
            origText = ''
            for p in soup.find_all('p', {'class': 'css-1ygdjhk evys1bk0'}):
                text = p.get_text()
                origText += text + "\n"
            write_file1.write(origText + "\n")
