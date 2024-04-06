
#
import csv


from bs4 import BeautifulSoup
import requests


url = "https://www.samhsa.gov/mental-health/depression"

response= requests.get(url)

if response.status_code == 200:
    soups = BeautifulSoup(response.text, "html.parser")
    content = soups.find_all("ul")

for cons in content:
    print(cons.text.strip())

else:
    print("i can not seem to find that information")  


#storing the data in a cvs file

with open("scraped_data.csv", "w", newline="")as file:
    writer = csv.writer(file)

    writer.writerow(['Depression'])

    for cont in content:
        writer.writerow([content.text.strip()])

#storing it in a list
    scrapped_data = []

   # we are going to store it in a list    
    
    for cont in content:
        scrapped_data.append(cont.text.strip())

    for data in scrapped_data:
        print(data)

        






