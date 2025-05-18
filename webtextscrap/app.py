import requests
from bs4 import BeautifulSoup
import re

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text,"html.parser")
#print(soup.prettify())
num_pages=soup.select(".s-pagination--item")
for num_page in num_pages:
    if not num_page  or num_page==None:
        print("Please enter a valid number")
    else:
        match = re.search(r'>(\d+)<\/a>', str(num_page))
        if match:
            number = match.group(1)
            l=0
            if l<int(number):
                l=number
print(l)
for r in range(1, int(l)+1):
    #print(r.text)
    questions=soup.select(".s-post-summary--content-title")
    for question in questions:
      print(question.text)