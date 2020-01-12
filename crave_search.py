import requests
import urllib.request
import time
from bs4 import BeautifulSoup


def crave():
    urlLists = ["https://www.crave.ca/en/collections-section/comedies-664", "https://www.crave.ca/en/collections-section/new-arrivals-2665", "https://www.crave.ca/en/made-by-women-38112060", "https://www.crave.ca/en/tv-shows/dramas-47588237", "https://www.crave.ca/en/throwback-76912768", "https://www.crave.ca/en/music-docs-71121196", "https://www.crave.ca/en/tv-shows/leading-women-36796294", "https://www.crave.ca/en/tv-shows/true-crime-13861696", "https://www.crave.ca/en/tv-shows/sitcoms-81787111", "https://www.crave.ca/en/tv-shows/sci-fi-and-fantasy-81535117", "https://www.crave.ca/en/tv-shows/documentaries-60216979", "https://www.crave.ca/en/jfl-1857595", "https://www.crave.ca/en/comedy-central-roasts-48190577", "https://www.crave.ca/en/tv-shows/based-on-a-book-56483496", "https://www.crave.ca/en/tv-shows/star-trek-94594490", "https://www.crave.ca/en/tv-shows/crime-and-mystery-73623287", "https://www.crave.ca/en/tv-shows/superheroes-87897929", "https://www.crave.ca/en/tv-shows/cravetv-originals-81474178", "https://www.crave.ca/en/vice-84919204", "https://www.crave.ca/en/tv-shows/all-canadian-33986436", "https://www.crave.ca/en/tv-shows/stand-up-comedy-71017175", "https://www.crave.ca/en/millenials-16311205", "https://www.crave.ca/en/millenials-16311205"]

    craveTVList = []

    for link in urlLists:
        url = link
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        soup.findAll()
        soup = str(soup)

        showList = soup.split("-")

        for word in showList:
            if word.startswith('title=\"'):
                lst = word.split("\"")
                craveTVList.append(lst[1])

    craveTVGroup = set(craveTVList)
    craveTVGroup.remove("You Might Like")


    # Crave movies.

    urlLists2 = ["https://www.crave.ca/en/collections-section/new-arrivals-2864", "https://www.crave.ca/en/box-office-hits-34007964", "https://www.crave.ca/en/critically-acclaimed-movies-46633996", "https://www.crave.ca/en/movies/comedies-12999452", "https://www.crave.ca/en/movies/dramas-27117270", "https://www.crave.ca/en/movies/family-60004579", "https://www.crave.ca/en/oscar-winners-11008264", "https://www.crave.ca/en/made-by-women-74414417", "https://www.crave.ca/en/best-of-tiff-18350890", "https://www.crave.ca/en/clint-eastwood-70074343", "https://www.crave.ca/en/directed-by-stanley-kubrick-61887259", "https://www.crave.ca/en/biopics-39127964", "https://www.crave.ca/en/spider-man-movies-16905611", "https://www.crave.ca/en/spike-lee-joints-63505685", "https://www.crave.ca/en/movies/spies-like-us-60136218", "https://www.crave.ca/en/movies/romance-48918333", "https://www.crave.ca/en/movies/action-adventure-13258955", "https://www.crave.ca/en/movies/horror-76899079", "https://www.crave.ca/en/movies/sci-fi-fantasy-45535247", "https://www.crave.ca/en/movies/crime-mystery-60301337", "https://www.crave.ca/en/movies/based-on-a-book-31509449", "https://www.crave.ca/en/movies/leading-women-22783223", "https://www.crave.ca/en/movies/all-canadian-62871243", "https://www.crave.ca/en/hbo/hbo-films-75982135"]

    craveMovieList = []

    for link2 in urlLists2:
        url2 = link2
        response2 = requests.get(url2)

        soup2 = BeautifulSoup(response2.text, 'html.parser')
        soup2.findAll()
        soup2 = str(soup2)

        movieList = soup2.split("-")

        for word2 in movieList:
            if word2.startswith('title=\"'):
                lst2 = word2.split("\"")
                craveMovieList.append(lst2[1])

    craveMovieGroup = set(craveMovieList)
    craveTotalGroup = list(craveMovieGroup) + list(craveTVGroup)
    return craveTotalGroup



