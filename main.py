import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.espn.co.uk/football/team/squad/_/id/363/eng.chelsea'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find('table',class_ = 'Table')

world_titles = table.find_all('th')

world_table_titles = [title.text for title in world_titles]
print(world_table_titles)

df = pd.DataFrame(columns = world_table_titles)

column_data = table.find_all('tr')

for row in column_data[1:]:
  row_data = row.find_all('td')
  individual_row_data = [data.text.strip() for data in row_data]
  
  length = len(df)
  df.loc[length] = individual_row_data

print(df)
