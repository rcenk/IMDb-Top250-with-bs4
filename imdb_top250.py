import requests
from bs4 import BeautifulSoup

imdbTop250 = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"

requestsTop250 = requests.get(imdbTop250)

soupTop250 = BeautifulSoup(requestsTop250.content,"html.parser")

fetch_data_for_top250 = soupTop250.find_all("table", {"class":"chart full-width"})

# print(fetch_data_for_top250[0].contents)
# print(len(fetch_data_for_top250[0].contents))

# print(len(fetch_data))
tvseries = (fetch_data_for_top250[0].contents)[len(fetch_data_for_top250[0].contents) -2]

# print(tvseries)
tvseries = tvseries.find_all("tr")

print("\n","******************************IMDb Top 250 TV Series*****************************************","\n")
for series in tvseries:
    seriesTitles = series.find_all("td", {"class":"titleColumn"})
    seriesName = seriesTitles[0].text
    seriesName = seriesName.replace("\n", "")
    print(seriesName)
