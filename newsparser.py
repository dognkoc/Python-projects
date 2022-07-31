import feedparser


url ="https://www.sozcu.com.tr/feed/rss"
haberler = feedparser.parse(url)

i =0
for haber in haberler.entries:
    i += 1
    print(i)
    print(haber.title)
    print(haber.summary)
    print(haber.link)
    print("*"*15)



    
