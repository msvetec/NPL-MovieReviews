import nltk
import GetTextFromFiles as gt



def Bayes():
    corpus = gt.GetText.GetCorpus('NEG',0)
    tocnost= ""
    top = ""
    for k in corpus:
        classifier = nltk.NaiveBayesClassifier.train(k[0]) 
        tocnost=nltk.classify.accuracy(classifier, k[1]) * 100
        top=classifier.most_informative_features(15)
        classifier.show_most_informative_features(15)

    print("Tocnost NaiveBayesClassifier: "+str(tocnost)+"%")


    with open('klasifikator_bayes_neg_rezultat.txt','w') as f:
        f.write("Tocnost NaiveBayesClassifier: "+str(tocnost)+"%"+'\n'+"15 najinformativnijih rijeci"+'\n')
        for i in top:
            f.write(str(i)+'\n')
        f.close()
    

