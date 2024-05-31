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

print(df) 
    





# for row in rows [1:]:
#     row_data = row.find_all("td")
#     text_row_data = [data.text.strip() for data in row_data]
#     length = len(df)
#     df.loc[length] = text_row_data #put the text in <td> into an appropriately titled column
# print(df)