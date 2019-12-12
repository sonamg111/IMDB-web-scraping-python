# from bs4 import BeautifulSoup
# import requests
from pprint import pprint
from first_task import*
from second_task import*

def without_duplicate_years(movies):
        years=[]
        for index in movies:
                top_movies_year=index["year"]
                if top_movies_year not in years:
                         years.append(top_movies_year)
        return years 
duplicate_years= without_duplicate_years(top_movies)
# print duplicate_years       
                

def group_by_decade(movies):
    yearDecade={}
    for index in duplicate_years:
        movieYears=[]    
        module = index % 10
        decade= index-module
        rangeYear=(decade)+10                
        for index2 in range(decade,rangeYear):
                if index2 in same_group_year:
                        movieYears.append(same_group_year[index2])       
        yearDecade[decade]= movieYears
    return (yearDecade)     

year_by_decade = group_by_decade(top_movies) 
# pprint (year_by_decade)


