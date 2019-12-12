from fifth_task import*

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
        allLanguagecount={}
        for i in duplicateLanguage:
                count=1
                for j in language:
                        if i==j:
                                allLanguagecount[i]=count
                                count=count+1
        return (allLanguagecount)        
analyse_movies_language(movies,allLanguage)