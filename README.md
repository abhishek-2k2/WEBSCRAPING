<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Web Scraping Project: Flipkart and Amazon Data Extraction</title>
</head>
<body>

<h1>Web Scraping Project: Flipkart and Amazon Data Extraction</h1>
<p>This project demonstrates web scraping techniques to extract laptop titles and prices from Flipkart and Amazon websites using Python. The extracted data is then converted into Excel (.xlsx) files for further analysis.</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#libraries">Importing Libraries</a></li>
    <li><a href="#functions">Functions</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#results">Results</a></li>
    <li><a href="#contributing">Contributing</a></li>
  
</ul>

<h2 id="introduction">Introduction</h2>
<p>This project showcases Python web scraping techniques using BeautifulSoup and requests libraries to fetch laptop titles and prices from Flipkart and Amazon websites. The data is then organized into structured Excel files for easy analysis.</p>

<h2 id="libraries">Importing Libraries</h2>
<p>Importing necessary libraries for web scraping and data handling:</p>
<pre><code>
import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
</code></pre>

<h2 id="functions">Functions</h2>
<p>Defining functions to extract data from Flipkart and Amazon:</p>
<pre><code>
# Function to extract data from Flipkart
def extract_from_flipkart(url, tag_title, tag_price):
    # Implementation code
    ...

# Function to extract data from Amazon
def extract_from_amazon(url, tag_title, tag_price):
    # Implementation code
    ...
</code></pre>

<h2 id="usage">Usage</h2>
<p>Running the web scraping functions to fetch laptop data:</p>
<pre><code>
# Run web scraping on Flipkart
for i in range(2, 11):
    extract_from_flipkart(f"https://www.flipkart.com/search?q=laptops&page={i}", 'div._4rR01T', 'div._30jeq3._1_WHN1')

# Run web scraping on Amazon
for i in range(2, 11):
    extract_from_amazon(f"https://www.amazon.in/s?k=laptops&page={i}", 'span.a-size-medium.a-color-base.a-text-normal', 'span.a-price-whole')
</code></pre>

<h2 id="results">Results</h2>
<p>Converted extracted data into Excel (.xlsx) files:</p>
<pre><code>
# Convert data to Excel files
df_flipkart = pd.DataFrame.from_dict(data)
df_flipkart.to_excel("flipkart.xlsx", index=False)

df_amazon = pd.DataFrame.from_dict(data1)
df_amazon.to_excel("amazon.xlsx", index=False)
</code></pre>

<h2 id="contributing">Contributing</h2>
<p>Contributions are welcome! Please feel free to submit a Pull Request.</p>



</body>
</html>

