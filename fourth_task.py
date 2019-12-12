from first_task import*
from second_task import*
from third_task import*

def movieApi(movie_url):
        response = requests.get(movie_url)
        soup = BeautifulSoup(response.text,"html.parser")
        return soup
# print soup        

def scrape_top_list(url[:5]):
        details=movieApi(url)
 
        movieDetails={}
        for i in range(1):
                try:
                        sum_data=details.find("div",class_="article",id="titleDetails")
                        data=sum_data.find_all("div",class_="txt-block")
                        languageList=[]
                        for index in data[:5]:
                                h4_data=index.find("h4",class_="inline").get_text()
                                if h4_data == "Language:":
                                        language=index.findAll("a")
                                        for i in language:
                                                lANGUAGES=i.get_text()
                                                languageList.append(lANGUAGES)
                                if "Country:"==  h4_data:
                                        countryName = index.a.get_text() 
                except AttributeError: 
                        continue
        movieName = details.find('div',class_="title_wrapper").h1.get_text()
        movie_name=movieName.split()

        summary = details.find('div', class_= 'plot_summary')
        bio = summary.find('div', class_= 'summary_text').get_text().strip()

        director = summary.find('div', class_="credit_summary_item")
        directorList =   director.findAll('a')
        directorLists = [x.get_text()  for x in  directorList ] 

        gerne = details.find('div' , class_='subtext')
        gerneName = gerne.find_all('a')
        gerneList = [ i.get_text() for i in gerneName[:-1]]

        posterName = details.find('div', class_='poster').a['href']
        moviePoster = "https://www.imdb.com%26quot%3B/" + posterName

        runtime=details.find("div",class_="subtext").time["datetime"]
        runTime=""
        for i in runtime:
                if i.isdigit()==True:
                        runTime=runTime+i
        movieDetails['name']=movie_name[0]
        movieDetails['Directior'] = directorLists 
        movieDetails['Country'] = countryName
        movieDetails['Language'] = languageList
        movieDetails['poster_image_url'] = moviePoster
        movieDetails['bio'] = bio
        movieDetails['runtime'] = runTime
        movieDetails['genre'] = gerneList
        return (movieDetails) 
url="https://www.imdb.com/title/tt0986264/"        
MovieDetails=scrape_top_list(url)
# pprint (MovieDetails) 