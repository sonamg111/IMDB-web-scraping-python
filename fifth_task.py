from first_task import*
from fourth_task import*

def scrape_movie_details(details):
    allMoviesList=[]
    for index in details:
        movie_link=index["url"]
        movie_url = scrape_top_list(movie_link)
        mainMovie = movie_url.copy()
        movie_url.clear()
        allMoviesList.append(mainMovie)
    return allMoviesList
    
movies_detail_list = scrape_movie_details(top_movies)
        
# pprint (movies_detail_list) 

        