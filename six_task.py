from five_task import*

def moviesLanguage(MovieDetails):
    languageList=[]
    for index in MovieDetails:
        movie_language=index["Language"]
        languageList.extend(movie_language)
    return languageList
allLanguage = moviesLanguage(movies_detail_list)
# print allLanguage


def duplicateList(list1):
        new_list=[]
        i=0
        while i<len(list1):
                if list1[i] not in new_list:
                        new_list.append(list1[i])
                i=i+1
        return new_list                                      
movies=duplicateList(allLanguage) 

def analyse_movies_language(duplicateLanguage,language):
        allLanguageCount={}
        for i in duplicateLanguage:
                count=1
                for j in language:
                        if i==j:
                                allLanguageCount[i]=count
                                count=count+1
        pprint (allLanguageCount)        
analyse_movies_language(movies,allLanguage)