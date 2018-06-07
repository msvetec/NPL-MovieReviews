import nltk
import GetTextFromFiles as gt
from nltk.classify import MaxentClassifier, accuracy



def Maxent():
    corpus = gt.GetText.GetCorpus('POS',0)
    tocnost= ""
    top = ""
    for k in corpus:
        classifier = nltk.MaxentClassifier.train(k[0]) 
        tocnost=nltk.classify.accuracy(classifier, k[1]) * 100
        classifier.show_most_informative_features(15)

    print("Tocnost MaxentClassifier: "+str(tocnost)+"%")
    print(top)


    with open('klasifikator_maxent_pos_rezultat.txt','w') as f:
        f.write("Tocnost MaxentClassifier: "+str(tocnost)+"%")
        f.close()
    

