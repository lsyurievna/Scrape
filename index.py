from bs4 import BeautifulSoup
import requests 
import pandas as pd

page_to_scrape = requests.get("https://www.mcgill.ca/chemistry/faculty")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

table = soup.find('table')

titles = table.find_all("th") #returns all titles as a list with htmls tags
text_titles = [title.text for title in titles] #gets rid of html tags

df = pd.DataFrame(columns = text_titles)

#Looking at the code for the table we can see that all the rows are codes as <tr> tags
#and all the data in the rows are in the <td> tags

rows = table.find_all("tr")
for row in rows [1:]:
    row_data = row.find_all("td")
    text_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = text_row_data #put the text in <td> into an appropriately titled column
print(df)