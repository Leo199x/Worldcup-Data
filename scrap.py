from bs4 import BeautifulSoup
import requests
import pandas as pd

years = [1930,1934,1938,1950,1954,
         1958,1962,1966,1970,1974,
         1978,1982,1986,1998,2002,
         2006,2010,2014,2018,2022]

web = 'https://en.wikipedia.org/wiki/2022_FIFA_World_Cup'

response = requests.get(web)
content = response.text

soup = BeautifulSoup(content, 'lxml')

matches = soup.find_all('div', class_='footballbox')

home = []
score = []
away = []

for match in matches:
    home.append(match.find('th', class_='fhome').get_text())
    score.append(match.find('th', class_='fscore').get_text())
    away.append(match.find('th', class_='faway').get_text())

dict_football = {'Home Nation': home, 'Final Scoreline': score, 'Away Nation': away}
df_football = pd.DataFrame(dict_football)
df_football['Year'] = '2022'
print(df_football)