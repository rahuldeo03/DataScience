import requests 
import pandas as pd
import pickle
import re
from bs4 import BeautifulSoup 
URL = "https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=clp_metro_expandable_2_5.metroExpandable.METRO_EXPANDABLE_mobile-phones-store_ZHYC957RFL_wp3&fm=neo%2Fmerchandising&iid=M_84a0d040-1732-4bc1-91e5-1db3d3179f71_5.ZHYC957RFL&ssid=s1a8uehom80000001598163916586"
r = requests.get(URL) 
trim = re.compile(r'[^\d.,]+')
soup = BeautifulSoup(r.content, 'html5lib')
products=[] #List to store name of the product
prices=[] #List to store price of the product
specifications=[] #List to store rating of the product
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE'})
    specs=soup.findAll('li', attrs={'class':'tVe95H'})
    for i, spec in enumerate(specs):
        specs.append(spec)
        print(spec)
    print('--------------')    
    products.append(name.text)
    prices.append(trim.sub('', price.text)) 
    specifications.append(specs.text)
    #df = pd.DataFrame({i:specs})
#print(products)    
#print(prices)  
#print(specifications)  
#df = pd.DataFrame({'Product Name':products,'Price':prices, 'Specifications':specifications}) 
#df.to_csv('products.csv', index=False, encoding='utf-8')    
              

              

