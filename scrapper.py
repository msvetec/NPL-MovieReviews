import bs4
import requests
import datetime
import re


corpus = []
class Scapper:

##    corpusName = ""
##    corpusText = ""
##    rating = 0
##    date = ""
##    brComment = ""
    pos = "pos"
    neg = "neg"

    

    
    def GetReview(_url):
        global corpus
        lista = []
        outPutDateFormat = "%m-%d-%y"
        DateFormat2 = "%d %b, %Y"
        brojac = 2
        
        corpusName = _url.split('/')[4]
        

        
        
        for x in range (0,10):
                url = _url+"page/"+str(brojac)+"/"
                res = requests.get(url)
                soup = bs4.BeautifulSoup(res.text, 'html.parser')
                movie_con = soup.find_all('div', {"class" : "film-detail-content"})

                while True:
                    try:
                        for i in range (0,12):
                            rating = movie_con[i].div.span.find(itemprop='ratingValue').get("content")
                            dat = movie_con[i].div.find('span', class_='_nobr').get_text()
                            text = movie_con[i].find('div',class_ = 'body-text -prose collapsible-text')
                    
                            s = text.p.text
                            s = re.sub(r'[^\w\s]','',s)
                            corpusText = s
                            brComment = str(brojac + 1)
                            date0 = datetime.datetime.strptime(dat , DateFormat2 )
                            date=(datetime.date.strftime(date0, outPutDateFormat))
                            inputDat = {
                                'text':corpusText,
                                'date':date,
                                'rating':rating,
                                'brKomp':i+1
                                }
                            lista.append(inputDat)
                        
                        break
                    except:
                        break
                brojac = brojac +1
                print(url)
            
        corpus=lista
        
        
        

        
        
        
        

    url = "https://letterboxd.com/film/tomb-raider/reviews/by/activity/"
    GetReview(url)
    print(corpus)
    
  
