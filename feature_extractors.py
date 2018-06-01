import reader
import scrapper as sc

corpusText = []
posText = ""
negText = ""

class Feature_extractors:

    def GetText():
        global corpusText
        
        for i in sc.corpus:
            inputDat = {
                'text':i['text'].lower(),
                'PosNeg':i['PosNeg']
                }
            corpusText.append(inputDat)
    
    def ClassificationText():
        global posText
        global negText
        for i in corpusText:
            if i['PosNeg'] == 'pos':
                posText = posText+i['text']
            if i['PosNeg'] == 'neg':
                negText = negText+'\n'+i['text']
                
    
    def Features_neg(_negText):
        result_neg= {}
        text=_negText.split()
        
        for rijec, neg in reader.neg_dict.items():
            brRijeci = text.count(rijec)
            result_neg[rijec] = neg*brRijeci

        return result_neg

    def Features_pos(_posText):
        result_pos= {}
        text=_posText.split()
        
        for rijec, pos in reader.pos_dict.items():
            brRijeci = text.count(rijec)
            result_pos[rijec] = pos*brRijeci

        return result_pos
    
    def Features_all(_negDict,_posDict):

        result_all = {}

        for rijec, pol in _negDict.items():
            result_all[rijec+'_pos'] = pol
        for rijec, pol in _posDict.items():
            result_all[rijec+'_neg'] = pol
        #print(result_all)
        

    GetText()
    ClassificationText()
    negDict=Features_neg(negText)
    posDict=Features_pos(posText)
    Features_all(negDict,posDict)
    
