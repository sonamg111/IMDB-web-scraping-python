from bs4 import BeautifulSoup
import requests
from pprint import pprint

movie_url = " https://www.imdb.com/india/top-rated-indian-movies/"
response = requests.get(movie_url)
soup = BeautifulSoup(response.text,"html.parser")
title=soup.find('tbody',class_='lister-list')
trs=title.findAll('tr')

def scrape_top_list():
    movie_list = []
    position=1
    for index in trs:
        movie_details={}
        movie_name=index.find('td',class_='titleColumn').a.get_text()
        year_name=index.find('span',class_='secondaryInfo').get_text()
        rating=index.find('td',class_='ratingColumn imdbRating').get_text()
        url = index.find("a")
        movieUrl = "https://www.imdb.com"+url["href"]
        movie_details["name"]=movie_name
        movie_details["year"]=int(year_name[1:5])
        movie_details["rating"]=float(rating)
        movie_details["position"]=position
        movie_details["url"]=movieUrl
        position=position+1
        movie_list.append(movie_details)
    return movie_list
top_movies = scrape_top_list()    
# pprint (top_movies)

