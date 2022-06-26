from bs4 import BeautifulSoup
import requests
import time
import csv
import pandas as pd

start_url='https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
webpage=requests.get(start_url)
soup=BeautifulSoup(webpage.text,"html.parser")
temparray=[]

for tr in soup.find("table").find_all("tr"):
    td=tr.find_all("td")
    row=[i.text.rstrip() for i in td]
    temparray.append(row)

name=[]
distance=[]
mass=[]
radius=[]

for i in range(1,len(temparray)):
    name.append(temparray[i][1])
    distance.append(temparray[i][3])
    mass.append(temparray[i][5])
    radius.append(temparray[i][6])

dataframe = pd.DataFrame(
    list(zip(name, distance, mass, radius)),
    columns=["Star_name", "Distance(in light years)", "Mass", "Radius"],
)
dataframe.to_csv("data.csv")
