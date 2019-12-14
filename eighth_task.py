import os.path
from fifth_task import*
from first_task import*
from fourth_task import*
import json


def cashingMovieDetails(data,details):
    moviesData = []
    for index in details:
        moviesUrl = index["url"]
        # print (moviesUrl)
        movieId=moviesUrl.split("/")
        # print movieId
        movieUrlId=movieId[4]
        # print movieUrlId
        moviesFileName="WebScrapinCashing/"+movieUrlId+".json"
        # print moviesFileName 
        if os.path.exists(moviesFileName):
            idFiles = open(moviesFileName,"r") 
            idData = idFiles.read() 
            dictData = json.loads(idData)
            # print dictData
            # moviesData.append(dictData)
        else:
            dataMovies = scrape_top_list(moviesUrl)
            openidFileWrite = open(moviesFileName,"w")
            # print "-----------"
            stringData = json.dumps(dataMovies)
            writeFile=openidFileWrite.write(stringData)
            # print stringData
            openidFileWrite.close()
        # return  moviesData    
cashingMoviesData = cashingMovieDetails(movies_detail_list,top_movies)
