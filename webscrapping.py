
from bs4 import BeautifulSoup
import requests

url =  " https://www.healthline.com/health/depression"
results = requests.get('url')
print(results)


soup = BeautifulSoup(results.text, "html")
print(soup)

print(soup.prettify())

soup.findAll("p", "ul")


