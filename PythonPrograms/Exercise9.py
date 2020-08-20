''' Exercise 10
Write a program to read a file from a folder, 
read from a url in write mode,
print first 3 lines of the file by iterating
save first 5 lines in a list,
write 2 lines into the file,
get current position of the file object pointer,
close the file '''


#Python program to scrape website  
#and save quotes from website 
import requests 
import pandas as pd
import re
from bs4 import BeautifulSoup 
URL = "https://www.ndtv.com/weather"
r = requests.get(URL) 
trim = re.compile(r'[^\d.,]+')
soup = BeautifulSoup(r.content, 'html5lib')
print(soup.find_all('td', valign_='top'))
#for a in soup.find_all('td', valign_='top'):
#    name=a.find('h1', attrs={'class':'headline-banner__title'})
    #price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    #products.append(name.text)
    #prices.append(trim.sub('', price.text))
#    print(name.text)  
#df = pd.DataFrame({'Product Name':products}) 
#df.to_csv('Cars.csv', index=False, encoding='utf-8')

#result = trim.sub('', mystring)