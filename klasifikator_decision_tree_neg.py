import nltk
import GetTextFromFiles as gt



def Decision():
    corpus = gt.GetText.GetCorpus('NEG',0)
    tocnost= ""
    top = ""
    for k in corpus:
        classifier = nltk.DecisionTreeClassifier.train(k[0]) 
        tocnost=nltk.classify.accuracy(classifier, k[1]) * 100

    print("Tocnost DecisionTreeClassifier: "+str(tocnost)+"%")


    with open('klasifikator_decision_tree_neg_rezultat.txt','w') as f:
        f.write("Tocnost DecisionTreeClassifier: "+str(tocnost))
        
        f.close()
    

