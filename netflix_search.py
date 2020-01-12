import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Parses through information on Netflix Tv Shows and extracts the title names


def netflix():
    url_tv_shows = 'https://www.netflix.com/browse/genre/83'
    response = requests.get(url_tv_shows)

    soup_tv_shows = BeautifulSoup(response.text, 'html.parser')
    soup_tv_shows = str(soup_tv_shows)
    newlist_tv_shows = soup_tv_shows.split("<")

    netflixTVList = []

    for i in range(len(newlist_tv_shows)):
        if ("img alt") in newlist_tv_shows[i]:
            practise = str(newlist_tv_shows[i])
            practise = practise.split("=")
            practise = practise[1].replace("class", "")
            practise = practise.split("\"")
            practise = practise[1]
            netflixTVList.append(practise)

    netflixTVSet = set(netflixTVList)

    # Parses through information on Netflix Movies and extracts the title names

    urlmovies = 'https://www.netflix.com/browse/genre/34399'
    response = requests.get(urlmovies)

    soup_movies = BeautifulSoup(response.text, 'html.parser')
    soup_movies = str(soup_movies)
    newlist_movies = soup_movies.split("<")

    netflixMovieList = []

    for i in range(len(newlist_movies)):
        if ("img alt") in newlist_movies[i]:
            practise = str(newlist_movies[i])
            practise = practise.split("=")
            practise = practise[1].replace("class", "")
            practise = practise.split("\"")
            practise = practise[1]
            netflixMovieList.append(practise)

    netflixMovieset = set(netflixMovieList)
    netflixMovieList = list(netflixMovieset)
    return netflixMovieList



