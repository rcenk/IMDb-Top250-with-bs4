import requests
from bs4 import BeautifulSoup
# IMDb Top 250 dizilerini listeleme işlemi:

# URL tanımlama işleminin yaptık.
imdbTop250 = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"

# content alacağız ve sayfanın tüm kaynakları r değişkenine atacağız.
requestsTop250 = requests.get(imdbTop250)

# BeautifulSouptan bir nesne oluştururken hata ile karşılaşmamak adına html.parser kullanmamız gerekiyor.
soupTop250 = BeautifulSoup(requestsTop250.content,"html.parser")

# table etiketinden class'ı chart full-width olanı alıyoruz. Tüm table ı çekmiyoruz.
fetch_data_for_top250 = soupTop250.find_all("table", {"class":"chart full-width"})

# Bu kısımda boyutumuz 7 çıktı. Normalde tabel etiketi içerisinde 3 contents imiz var ancak \n i de almış bulunuyor.
# Dizilerimizin listesi tbody etiketi içerisinde yer alıyor biz de sadece tbody etiketini alarak bu sorunu çözebiliriz.
# print(fetch_data_for_top250[0].contents)
# print(len(fetch_data_for_top250[0].contents))

# print(len(fetch_data)) 1 boyutlu dizi olduğunu görüyoruz. Sadece film tablosunu almak için -2 yazıyoruz.
tvseries = (fetch_data_for_top250[0].contents)[len(fetch_data_for_top250[0].contents) -2]
# print(tvseries) Yalnızca tbody kısımları kaldı \n leri temizledik.
tvseries = tvseries.find_all("tr")
print("\n","******************************IMDb Top 250 TV Series*****************************************","\n")
for series in tvseries:
    seriesTitles = series.find_all("td", {"class":"titleColumn"})
    seriesName = seriesTitles[0].text
    seriesName = seriesName.replace("\n", "")
    print(seriesName)