from bs4 import BeautifulSoup
import requests 
import pandas as pd

page_to_scrape = requests.get("https://www.mcgill.ca/chemistry/Node/19")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

#I will read all of the paragraphs on the page and make them into one string
ps = soup.findAll("p")
paragraphs = ""
for p in ps: 
    paragraphs = paragraphs + " " + p.get_text(strip=True, separator='\n')

print(paragraphs)

