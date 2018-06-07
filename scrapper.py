import bs4
import requests
import datetime
import re
import os
import glob
import time
import glob
import time
import os.path


corpus = []
corpusName = ""

fuTime = 0
linkStruct = []
brComentara = 0


class Scapper:

    def GetReview(_movieName,_rang):
        print("======>Preuzimanje komentara<======")
        global corpus
        global corpusName
        global fuTime
        global brComentara
        global linkStruct
        _url = "https://letterboxd.com/film/"+_movieName+"/reviews/by/activity/"
        lista = []
        posNeg = ""
        provjera = 1
        outPutDateFormat = "%m-%d-%y"
        DateFormat2 = "%d %b, %Y"
        brojac = 2
        inputNum = 0
        corpusName = _url.split('/')[4]
        start = time.time()
        
        for x in range (0,_rang):#test for loop
            
            if provjera==1:
                url = _url
            if provjera == 0:
                url = _url+"page/"+str(brojac)+"/"
                brojac = brojac +1
            linkStruct.append(url)
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
                        
                        date0 = datetime.datetime.strptime(dat , DateFormat2 )
                        date=(datetime.date.strftime(date0, outPutDateFormat))
                        inputNum = inputNum + 1
                        brComentara = inputNum
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
        end = time.time()
        fuTime=end-start
        fuTime=str(datetime.timedelta(seconds=fuTime))
        

    def DeleteFiles():
        mypath = "Corpus"
        for root, dirs, files in os.walk(mypath):
            for file in files:
                os.remove(os.path.join(root, file))


    def CreateFile():
        
        print("======>Kreiranje korpusa<======")
        global corpusName
        global linkStruct
        global brComentara
        global fuTime
        savePathTexts = 'Corpus'
        commendText = ""
        fileName=""
        brojac = 0
        for i in corpus:
            brojac=brojac+len(i['text'].split())
            fileName =i['PosNeg']+"_"+corpusName+"_"+i['date']+"_"+str(i['brKomp'])+".txt"           
            with open(os.path.join(savePathTexts, fileName), 'w',encoding='utf-8') as f:
                f.write(i['text'])
                f.close()
                
        with open ('opis_korpusa.txt', 'w', encoding='utf-8') as f:
            f.write ("Letterboxd: letterboxd.com\n"+"Ime filma: "+corpusName.replace("-"," ")+"\n"+"Vrijeme skidanja korpusa: "+str(fuTime)+"\n"+"Broja clanaka: "+str(brComentara)+"\n"+"Broj pojavnica: "+str(brojac)+"\n"+"Izori korpusa:"+"\n\n")
            for i in linkStruct:
                f.write(i+"\n")
            f.close()

  
            
     
         


 
    
  
