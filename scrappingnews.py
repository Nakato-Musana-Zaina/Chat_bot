from GoogleNews import GoogleNews  
from bs4 import BeautifulSoup
#googlenews = GoogleNews()
#googlenews.search("Uganda")
#result = googlenews.result()

#for results in result:
   # print(result)

#news = BeautifulSoup(result)
    

googlenews = GoogleNews()
googlenews.get_news('Python programming')
result = googlenews.results()

news = []

for results in result:
    soups = BeautifulSoup(result[''], 'html.parser')

    title = soups.find('title').text.strip()


    texts = soups.find('p').text.strip()

    dates = soups.find('date')

    reporter = soups.find('reporter')

    articles = {
        'title':title,
        'texts':texts,
        'date': dates,
        'reporter': reporter
    }
for new in news:
    print("Title:",new['title'])
    print("Text:",new['text'])
    print("Dates:", new['date'])
    print("Reporter:", new['reporter'])
    print()


    #print(results)











