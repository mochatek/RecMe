import requests
from bs4 import BeautifulSoup

film = []
year = []
lang = []
genre = []

y = '2018'
l = 'Tamil'
link = "https://en.wikipedia.org/wiki/List_of_" + l + "_films_of_" + y

res = requests.get(link)

if res.status_code == 200:
    soup = BeautifulSoup(res.content, "lxml")
    for tbl in soup.findAll("table", {"class" : "wikitable"})[:3]:
        for tr in tbl.findAll("tr")[1:]:
            tds = tr.findAll("td")
            try:
                if l == "Malayalam":
                    f = tds[-5].text.strip()
                    g = ",".join(list(map(lambda x:x.lower().replace("film", "").strip(), tds[-2].text.split(","))))
                elif l == "Tamil":
                    f = tds[-6].text.strip()
                    g = ",".join(list(map(lambda x:x.lower().replace("film", "").strip(), tds[-3].text.split(","))))

                if f != "" and len(g) > 0:
                    film.append(f)
                    year.append(y)
                    lang.append(l)
                    genre.append(g)
            except:
                continue
            
    import pandas
    df = pandas.DataFrame(zip(film, year, lang, genre), columns = ["Film", "Year", "Language", "Genre"])
    df.to_excel(l + y + ".xlsx")
else:
    print("Error in Link")

    
