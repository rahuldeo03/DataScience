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
URL = "https://www.flipkart.com/laptops/a~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq="
r = requests.get(URL) 
trim = re.compile(r'[^\d.,]+')
soup = BeautifulSoup(r.content, 'html5lib')
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    #rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    products.append(name.text)
    prices.append(trim.sub('', price.text))  
    print(a)
#df = pd.DataFrame({'Product Name':products,'Price':prices}) 
#df.to_csv('products.csv', index=False, encoding='utf-8')

#result = trim.sub('', mystring)