from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
web = "https://fbref.com/en/comps/9/Premier-League-Stats"
response = requests.get(web)
content = response.text

soup = BeautifulSoup(content, "html.parser")
links = list(soup.find("table", {"id": "stats_squads_standard_for"}).find_all("a"))

links = [l.get("href")for l in links]
team_urls = [f"https://fbref.com{l}" for l in links]

print(team_urls)
with open('PLStats.csv','w',newline="\n",encoding='UTF8') as f:
    writer = csv.writer(f)
    for row in team_urls:
        writer.writerow([row])







