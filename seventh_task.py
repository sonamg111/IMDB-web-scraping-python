from fifth_task import*

def moviesDirectors(directors):
    directorsList=[]
    for index in directors:
        movie_directors=index["Directior"]
        directorsList.extend(movie_directors)
    return directorsList
directorsName = moviesDirectors(movies_detail_list)


def duplicateName(nameList):
        new_list=[]
        i=0
        while i<len(nameList):
                if nameList[i] not in new_list:
                        new_list.append(nameList[i])
                i=i+1
        return new_list              
duplicateDirectorName = duplicateName(directorsName)


def analyse_movies_directors(duplicateDirector,names):
        allDirector={}
        for i in duplicateDirector:
                count=1
                for j in names:
                        if i==j:
                                allDirector[i]=count
                                count=count+1
        pprint (allDirector)

analyse_movies_directors(duplicateDirectorName,directorsName)