import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Parses through information on Netflix Tv Shows and extracts the title names

def disney():
    url = 'https://www.theverge.com/2019/10/14/20913417/disney-plus-launch-lineup-marvel-star-wars-pixar-tv-shows-movies-simpsons-national-geographic'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    soup = str(soup)
    newlist = soup.split("<")

    disneyList = []

    for i in range(len(newlist)):
        if ("em>") in newlist[i]:
            practise = str(newlist[i])
            practise = practise.replace("em>", "")
            practise = practise.replace("/", "")
            if "(" in practise:
                practise = practise.replace(")", "")
                practise = practise.replace("(", "")
            practise = practise.strip(" ")
            if not practise.isnumeric():
                disneyList.append(practise)


    disneyList = set(disneyList)
    disneyList = list(disneyList)

    return disneyList




