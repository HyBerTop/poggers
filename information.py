from beker import Konyv

def writeToFile(konyvek):
    file = open("adatok.txt", "a", encoding="utf-8");
    for i in range(len(konyvek)):
        file.write("{};{};{};{};{}\n".format(konyvek[i].cim, konyvek[i].iro, konyvek[i].kiadas, konyvek[i].kategoria, konyvek[i].nyelv)); 
    file.close();

class Konyvek:

    def __init__(self):
        self.cim = ""
        self.iro = ""
        self.kiadas = ""
        self.kategoria = ""
        self.nyelv = ""

