import csv

pos_dict = {}
neg_dict = {}
svi_dict = {}
class Reader:

    def OpenFile():
        global pos_dict
        brojac=0
        global neg_dict
        with open ("leksicki_resurs.csv", 'r',encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if int(row[1])<0:
                    neg_dict[row[0]] = abs(int(row[1]))
                elif int(row[1])>=0:
                    pos_dict[row[0]] = int(row[1])
            f.close()

    def MakeDict():
        global pos_dict
        global neg_dict
        global svi_dict
        
        for key, value in pos_dict.items():
            svi_dict[key] = ("pos",value)
        for key, value in neg_dict.items():
            svi_dict[key]=("neg",value)
        print(svi_dict)
           
        
        
        
        
            

    OpenFile()
    MakeDict()
#full done
