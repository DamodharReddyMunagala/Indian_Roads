# Indian_Roads

#This block of code is used to get the data of National Highways and their embeded links

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
html = urlopen('https://en.wikipedia.org/wiki/List_of_National_Highways_in_India_by_highway_number')
bsObj = BeautifulSoup(html, 'lxml')
A = []
B = []
C = []
D = []
E = []
F = []
G = []
H = []
for data in bsObj.body.find('table', {'class' : 'wikitable sortable'}).findAll('tr'):
    cells = data.findAll('td')
    if data.find('td') is None:
        pass
    else:
        A.append('National Highway ' + cells[0].find(text = True) + ' (India)')
        B.append(cells[1].find(text = True))
        C.append(cells[2].find(text = True))
        D.append(cells[3].find(text = True))
        E.append(cells[4].find(text = True))
        F.append('https://en.wikipedia.org' + cells[0].find('a').attrs['href'])
        if cells[1].find('a') is None:
            G.append('None')
        else:
            G.append(cells[1].find('a').attrs['href'])
        #for url in data.findAll('a', href = re.compile('^(/wiki/National_Highway)')):
            #A.append(url.attrs['title'])
            #F.append(url.attrs['href'])
        #for url in data.findAll('a', href = re.compile('^(/wiki/)(?!National)')):
            #G.append(url.attrs['href'])
            #H.append(url.text)

#import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame(A,columns=['National Highways'])
df['OSMRI'] = B #OSMRI : Open Street Map Relation Identifier
df['States'] = C
df['length'] = D
df['routes'] = E
df['National Highway URLS'] = F
df['OSMRI_URL'] = G
#print (df)
df.to_csv('National_Highways.csv',index=True,header=True)
