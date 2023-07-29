#importing important  libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

#declaring data frame
data={"title":[],"price":[]}
data1={"title":[],"price":[]}

#defining a function that extract from first websites
def extract_from_flipkart(url,tag,tag1):
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')
    titles=soup.select(tag)
    prices=soup.select(tag1)
    for title in titles :
        data['title'].append(title.string)
    for price in prices:
        data['price'].append(price.get_text())
print("extracted from flipkart")

#defining a second function that extract data from second website
def extract_from_amazon(url,tag,tag1):
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')
    titles=soup.select(tag)
    prices=soup.select(tag1)
    for title in titles :
        data1['title'].append(title.string)
    for price in prices:
        data1['price'].append(price.get_text())
print("extracted from amazon")
           
    
#passing arguments
y="div._4rR01T"
z="div._30jeq3._1_WHN1"
p="span.a-size-medium.a-color-base.a-text-normal"
q="span.a-price-whole"
for i in range(2,11):
  extract_from_flipkart(f"https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}",y,z,)
for i in range(2,11):
     extract_from_amazon(f"https://www.amazon.in/s?k=laptops&page={i}&crid=6F783I44S1KI&qid=1689867251&sprefix=laptops%2Caps%2C214&ref=sr_pg_{i}",p,q)
     
     
#converting files to proper documents like csv or excel
print("converting files to proper documents")
df=pd.DataFrame.from_dict(data)
df.to_excel("flipkart.xlsx",index=False)

df1=pd.DataFrame.from_dict(data1)
df1.to_excel("amazon.xlsx",index=False)
 