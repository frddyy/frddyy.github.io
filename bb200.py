from selenium import webdriver
import urllib.request
import json
from datetime import datetime

PATH = "D:\Scrapping\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.billboard.com/charts/billboard-global-200/")

songList = []
now = datetime.now()
i = 1

while i<=200:
    for song in driver.find_elements_by_class_name("o-chart-results-list-row-container"):
        print(song.text)
        for img in song.find_elements_by_tag_name("img"):
            print(img.get_attribute("src"))
            urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".jpg")
            i = i+1
            songList.append(
                {"Pos" :song.text.split("\n")[0],
                 "Title" : song.text.split("\n")[1],
                 "Artist": song.text.split("\n")[2],
                 "PeakPos" : song.text.split("\n")[3],
                 "WksonChart": song.text.split("\n")[4],
                 "ScrapingTime" : now.strftime("%d %B %Y %H:%M:%S"),
                 "Image" : img.get_attribute("src")
                    }
                )
            
hasil_scraping = open("hasilscraping.json", "w")
json.dump(songList, hasil_scraping, indent = 6)
hasil_scraping.close()

driver.quit()
