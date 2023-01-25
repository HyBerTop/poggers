class Konyv():
	def __init__(self):
		self.cim="";
		self.iro="";
		self.kiadas="";
		self.kategoria="";
		self.nyelv="";

	def beker():
		konyvespolc=[];
		beolvasunk=True;
		i=0;
		while(beolvasunk):
			konyvespolc.append(Konyv());
			konyvespolc[i].cim=      input("A könyv címe:        ")
			konyvespolc[i].iro=      input("A könyv írója:       ")
			konyvespolc[i].kiadas=   input("A könyv kiadása:     ")
			konyvespolc[i].kategoria=input("A könyv kategóriája: ")
			konyvespolc[i].nyelv=    input("A könyv nyelve:      ")
			i=i+1;
			meg=input("Szeretnél még hozzáadni könyvet?: [1] igen [0] nem ");
			eldontottuk=False;
			while(not eldontottuk):
				if meg=="0":
					beolvasunk=False;
					eldontottuk=True;
				elif meg=="1":
					beolvasunk=True;
					eldontottuk=True;
				else:
					meg=input("Hibás adat\nSzeretnél még hozzáadni könyvet?: [1] igen [0] nem ");
		return(konyvespolc)
