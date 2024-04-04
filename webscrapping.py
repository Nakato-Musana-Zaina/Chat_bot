import requests

import BeautifulSoup

 
results = requests.get('https://pubmed.ncbi.nlm.nih.gov/26729021/')
print(results)


soup = BeautifulSoup(results.content, 'html.parser')
print(soup.prettify())


