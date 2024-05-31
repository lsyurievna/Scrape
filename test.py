from bs4 import BeautifulSoup
import requests 
import pandas as pd

page_to_scrape = requests.get("https://www.mcgill.ca/chemistry/faculty")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

table = soup.find('table')

#Making a dataframe with two columns name and link
df = pd.DataFrame(columns=["name","link"])

#Looking at the code for the table we can see that all the rows are defined as <tr> tags
#and all the data in the rows are in the <td> tags
#We have to go through all the rows (<tr>s) and isolate the <td>s

rows = table.find_all("tr")

i = 0 #counter

for row in rows[1:]: #omiting the first one as it contains the titles of the table which are irrelevant
    row_data = row.find_all("td")
    first_column_data = row_data[0] #only need data in the first row
    #An example of first column data is <td><a href="https://www.mcgill.ca/chemistry/Node/19">Andrews, Mark</a></td>
    #It has to be split into Name and Website link
    name = first_column_data.string #getting the name
    link = first_column_data.find("a").get('href') #getting the link
    #Now as we go through names and links we should add them one by one to the dataframe
    #We can put name in the first coulumn and the link in the second column 
    df.loc[i] = pd.Series({"name":name, "link":link})
    i = i+1
    
#Now, I need to place the text found in each of the links in another column of the dataframe
#This turns out to be a scraping project inside of a scraping project

#We can go through all of the items in the links column
for link in df["link"]: 
    page_to_scrape = requests.get(link)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    #Now, all of the research description information is located in <p> tags under a header like this:
    #<h2 id="research-description">Research Description</h2> 


