f_latest=open("C:\\Users\\Sinju\\Desktop\\mypython\\fileoperations\\latest_news.txt",encoding="utf-8")

f_stop=open("C:\\Users\\Sinju\\Desktop\\mypython\\fileoperations\\stopwords.txt",encoding="utf-8")


news_words=set()

stop_words={line.rstrip("\n") for line in f_stop}
# print(stop_words)

for line in f_latest:
    words= line.split()
    for w in words:
        news_words.add(w)
        
        
print(news_words.difference(stop_words))        
        
