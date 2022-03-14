# Import package request dan BeautifulSoup
import requests 
from bs4 import BeautifulSoup

# Request ke website
page = requests.get("https://republika.co.id/")

# Extract konten menjadi objek BeautifulSoup
obj = BeautifulSoup(page.text, 'html.parser')

print ('Menampilkan objek html')
print ('======================')
print (obj)

print ('Menampilkan title browser dengan tag')
print ('====================================')
print (obj.title)

print ('\nMenampilkan title browser tanpa tag')
print ('====================================')
print (obj.title.text)

print ('\nMenampilkan semua tag h2')
print ('==========================')
print (obj.find_all('h2'))

print ('\nMenampilkan semua teks h2')
print ('===========================')
for headline in obj.find_all('h2'):
    print (headline.text)
    
print ('\nMenampilkan headline berdasarkan div class')
print ('============================================')
print (obj.find_all('div', class_='bungkus_txt_headline_center'))

print ('\nMenampilkan semua teks headline')
print ('=================================')
for headline in obj.find_all('div', class_='bungkus_txt_headline_center'):
    print (headline.find('h2').text)

print ('\nMenyimpan headline pada file text')
print ('===================================')
f = open('D:\Scrapping\headline.txt', 'w')
for headline in obj.find_all('div', class_='bungkus_txt_headline_center'):
    f.write(headline.find('h2').text)
    f.write('\n')
f.close()

print ('\nMenampilkan kategori berdasarkan div class')
print ('============================================')
for category in obj.find_all('div', class_='teaser_conten1_center'):
    print (category.find('p').text)
    
# Import package json
import json
from datetime import datetime
# Deklarasi list kosong
data=[]
now = datetime.now()
# Lokasi file json
f = open('D:\Scrapping\headline.json', 'w')
"""for headline in obj.find_all('div', class_='bungkus_txt_headline_center'):
    # append headline ke variabel data
   data.append({"judul":headline.find('h2').text})"""
# dump list dictionary menjadi json
for publish in obj.find_all('div',class_='conten1'):
    # append headline ke variable data
    data.append({"judul":publish.find('h2').text,
                 "kategori":publish.find('a').text,
                 "waktuPublish":publish.find('div',class_='date').text,
                 "waktuScrapping":now.strftime("%Y-%m-%d %H:%M:%S")})
# dump list dictionary menjadi json
jdumps=json.dumps(data)
f.writelines(jdumps)
f.close()
