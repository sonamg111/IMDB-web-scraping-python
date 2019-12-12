from first_task import*
from fourth_task import*

def scrape_movie_details(details):
    allMoviesList=[]
    for index in details:
        movie_link=index["url"]
        movieUrl = scrape_top_list(movie_link)
        mainMovie = movieUrl.copy()
        movieUrl.clear()
        allMoviesList.append(mainMovie)
    return allMoviesList
        
movies_detail_list = scrape_movie_details(top_movies)
# pprint (movies_detail_list) 

        