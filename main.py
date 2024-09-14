import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.espn.co.uk/football/team/squad/_/id/363/eng.chelsea'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')

tables = soup.find_all('table', class_='Table')

# data goalkeepers
first_table = tables[0]
first_table_headers = [header.text for header in first_table.find_all('th')]
first_table_rows = [[data.text.strip() for data in row.find_all('td')] for row in first_table.find_all('tr')[1:]]

# df untuk tabel goalkeeper
df_first_table = pd.DataFrame(first_table_rows, columns=first_table_headers)
print("Goalkeepers:")
print(df_first_table)

# data outfield players
second_table = tables[1]
second_table_headers = [header.text for header in second_table.find_all('th')]
second_table_rows = [[data.text.strip() for data in row.find_all('td')] for row in second_table.find_all('tr')[1:]]
    
# df untuk tabel outfield players
df_second_table = pd.DataFrame(second_table_rows, columns=second_table_headers)
print("\nOutfield Players:")
print(df_second_table)