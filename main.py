import scrapper as sc
import klasifikator_bayes_all as kbA
import klasifikator_bayes_neg as kbN
import klasifikator_bayes_pos as kbP
import klasifikator_decision_tree_all as kdA
import klasifikator_decision_tree_pos as kdP
import klasifikator_decision_tree_neg as kdN
import klasifikator_maxent_all as kmA
import klasifikator_maxent_pos as kmP
import klasifikator_maxent_neg as kmN


def MainKlasifikator():
        ans = 1
        while ans:
                print("=============================")
                print("1.Klasifikator BAYES ALL")
                print("2.Klasifikator BAYES POS")
                print("3.Klasifikator BAYES NEG")
                print("4.Klasifikator DECISION ALL")
                print("5.Klasifikator DECISION POS")
                print("6.Klasifikator DECISION NEG")
                print("7.Klasifikator MAXENT ALL")
                print("8.Klasifikator MAXENT POS")
                print("9.Klasifikator MAXENT NEG")
                print("0. Kraj!")
                print("=============================")
                unos2 = int(input("Vas Odabri: "))
                if unos2 ==1:
                    kbA.Bayes()
                elif unos2 ==2:
                    kbP.Bayes()
                elif unos2 ==3:
                    kbN.Bayes()
                elif unos2 ==4:
                    kdA.Decision()
                elif unos2 ==5:
                    kdP.Decision()
                elif unos2 ==6:
                    kdN.Decision()
                elif unos2 ==6:
                    kdN.Decision()
                elif unos2 ==7:
                    kmA.Maxent()
                elif unos2 ==8:
                    kmP.Maxent()
                elif unos2 ==9:
                    kmN.Maxent()
                elif unos2 == 0:
                    ans = 0

unos = 0
ans = 1
unosBroj = 0
brStranica = 0
imeFilma = ""
#while True:
       # try:
while ans:
    print("=====================")
    print("1. Preuzimanje novog korpusa")
    print("2. Koristenje postojeceg korpusa")
    print("9. Kraj!")
    print("=====================")
    unos = int(input("Vas odabir: "))
    if unos == 1:
        unos2 = 0
        sc.Scapper.DeleteFiles()
        print("Upozorenje!")
        print("===========================================================================================")
        print("Preporuca se skiganje oko 6000 komentara, na svakoj stranica foruma se nalazi 12 komentara")
        print("===========================================================================================")
        print("Unesite ime filma")
        imeFilma = input()
        film = imeFilma.lower().replace(" ","-")
        print("Unesite broj stranica foruma!")
        brStranica = int(input("Broj strana Foruma(>=500): "))
        sc.Scapper.GetReview(film,brStranica)
        sc.Scapper.CreateFile()
        MainKlasifikator()
    elif unos==2:
        MainKlasifikator()
    elif unos == 9:
        ans = 0
                #break
        #except:
               # print("Doslo je do greske!")
                #break
                
        
        
        

        

        
            
        
        
        
