import feature_extractors as fe
from string import punctuation
from random import shuffle
from os import listdir




class GetText:
    def GetCorpus(_posNeg,_all):
        posText = []
        negText = []
        textFiles = []
        files = listdir("corpus/")
        
        for f in files:
            if f[-4:] == ".txt":
                    textFiles.append(f)

        for f in textFiles:
            if f[:3] == "pos":
                with open("corpus/" + f, "r", encoding = 'utf-8') as infile:
                        posText.append(infile.read().lower())
            elif f[:3] == "neg":
                with open("corpus/" + f, "r", encoding = 'utf-8') as infile:
                        negText.append(infile.read().lower())
        if _all ==0:
            corpusAll = [(fe.Features_pos(p), 'POS') for p in posText] + [(fe.Features_pos(n), 'NEG') for n in negText]
        elif _all==1:
            corpusAll = [(fe.Features_all(p), 'POS') for p in posText] + [(fe.Features_all(n), 'NEG') for n in negText]
            
        shuffle(corpusAll)

        finalCorpus = []
        for k in [corpusAll]:
            limit = int(len(k) * 0.9)
            train_set, test_set = k[:limit], k[limit:]
            finalCorpus.append([train_set, test_set])

        finalCorpus[0].append(_posNeg)

        return finalCorpus
  
   




