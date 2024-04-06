from GoogleNews import GoogleNews  
from bs4 import BeautifulSoup
googlenews = GoogleNews()
googlenews.search("Uganda")
result = googlenews.result()

print(result)

#news = BeautifulSoup(result)









