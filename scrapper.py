import bs4
import requests
import datetime
import re
import os


corpus = []
corpusName = ""


class Scapper:

##    corpusName = ""
##    corpusText = ""
##    rating = 0
##    date = ""
##    brComment = ""

    def GetReview(_url):
        global corpus
        global corpusName
        lista = []
        posNeg = ""
        provjera = 1
        outPutDateFormat = "%m-%d-%y"
        DateFormat2 = "%d %b, %Y"
        brojac = 2
        inputNum = 0
        corpusName = _url.split('/')[4]
        
        for x in range (0,1):#test for loop
            
            if provjera==1:
                url = _url
            if provjera == 0:
                url = _url+"page/"+str(brojac)+"/"
                brojac = brojac +1
            #url = "https://letterboxd.com/film/tomb-raider/reviews/by/activity/page/4/"
            res = requests.get(url)
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            movie_con = soup.find_all('div', {"class" : "film-detail-content"})
            provjera = 0
            while True:
                try:
                    for i in range (0,12):
                        rating = movie_con[i].div.span.find(itemprop='ratingValue').get("content")
                        if int(rating) <=6:
                            posNeg = "neg"
                        if int(rating) >6:
                            posNeg = "pos"
                        dat = movie_con[i].div.find('span', class_='_nobr').get_text()
                        text = movie_con[i].find('div',class_ = 'body-text -prose collapsible-text')
                        s = text.p.text
                        s = re.sub(r'[^\w\s]','',s)
                        corpusText = s
                        brComment = str(brojac + 1)
                        date0 = datetime.datetime.strptime(dat , DateFormat2 )
                        date=(datetime.date.strftime(date0, outPutDateFormat))
                        inputNum = inputNum + 1 
                        #print(inputNum)
                        inputDat = {
                            'text':corpusText,
                            'date':date,
                            'rating':rating,
                            'brKomp':inputNum,
                            'PosNeg':posNeg
                            
                            }
                        lista.append(inputDat)
                    
                    break
                except:
                    break
            
            
            
        corpus=lista

    

    def CreateFile():
        global corpusName
        savePathTexts = ""
        savePathCorpusDate = "Corpus" #promjena kad se izradi klasa za izradu direktorija
        commendText = ""
        #corpusDate = "" to do
        fileName=""
        for i in corpus:
            if i['PosNeg']=="pos":
                savePathTexts = 'Corpus\\pos'
            if i['PosNeg']=="neg":
                savePathTexts = 'Corpus\\neg'
                
            fileName =i['PosNeg']+"_"+corpusName+"_"+i['date']+"_"+str(i['brKomp'])+".txt"           
            with open(os.path.join(savePathTexts, fileName), 'w',encoding='utf-8') as f:
                f.write(i['text'])
                f.close()

##to do
##        with open (os.path.join(savePathCorpusDate,'opis_korpusa.txt'), 'w',encoding='utf-8') as f:
##            f.write()
                
            
     
         


    url = "https://letterboxd.com/film/tomb-raider/reviews/by/activity/"
    GetReview(url)
    
    #CreateFile()
    
  
