
import scrapper as sc
import reader
             
    
def Features_neg(_negText):
    resultNeg= {}
            
    text=_negText.split()
    
    for rijec, neg in reader.neg_dict.items():
        brRijeci = text.count(rijec)
        resultNeg[rijec] = neg*brRijeci

    return resultNeg

def Features_pos(_posText):
    resultPos= {}
    text=_posText.split()
    
    for rijec, pos in reader.pos_dict.items():
        brRijeci = text.count(rijec)
        resultPos[rijec] = pos*brRijeci

    return resultPos

def Features_all(_allText):

    resultAll = {}
    posDict = Features_pos(_allText)
    negDict = Features_neg(_allText)

    for rijec, pol in negDict.items():
        resultAll[rijec+'_pos'] = pol
    for rijec, pol in posDict.items():
        resultAll[rijec+'_neg'] = pol
    return resultAll
        


