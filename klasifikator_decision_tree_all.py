import nltk
import GetTextFromFiles as gt



def Decision():
    corpus = gt.GetText.GetCorpus('ALL',1)
    tocnost= ""
    top = ""
    for k in corpus:
        classifier = nltk.DecisionTreeClassifier.train(k[0]) 
        tocnost=nltk.classify.accuracy(classifier, k[1]) * 100

    print("Tocnost DecisionTreeClassifier: "+str(tocnost)+"%")


    with open('klasifikator_decision_tree_all_rezultat.txt','w') as f:
        f.write("Tocnost DecisionTreeClassifier: "+str(tocnost))
        
        f.close()
    

