from first_task import*

def group_by_year(movies):
    years=[]
    for index in movies:
        top_movies_year=index["year"]
        if top_movies_year not in years:
            years.append(top_movies_year)
    movieYears={}        
    for i in years:
        sameMovieYears=[]
        for j in top_movies:
            if i==j["year"]:
                sameMovieYears.append(j) 
        # pprint (sameMovieYears)
        movieYears[i]=sameMovieYears
    return (movieYears)       
         
same_group_year=(group_by_year(top_movies)) 
















        


