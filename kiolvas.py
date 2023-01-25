from information import Konyvek
class KonyvFile:
	def readFile():
		file=open("adatok.txt","r",encoding="utf-8");
		row=file.readline();
		polc = []
		i = 0
		while(row):
			if(len(row)!=0):
				rowSp=row.split(";")  
				polc.append(Konyvek())
				polc[i].cim = rowSp[0]
				polc[i].iro = rowSp[1]
				polc[i].kiadas = rowSp[2]
				polc[i].kategoria = rowSp[3]
				polc[i].nyelv = rowSp[4]
				i = i+1
				
				#print("A könyv címe: ",rowSp[0] , " Író: ",rowSp[1], " Kiadás éve: ",rowSp[2], " Kategoria: ",rowSp[3], " Nyelv: ",rowSp[4])   
			row=file.readline();	
		file.close();
		
		
		print("A könyv címe                    Író	                        Kiadás éve	Kategoria	Nyelv")
		for i in range(len(polc)):
			print("{:30}	{:30}	{:10}	{:10}	{:30}".format(polc[i].cim, polc[i].iro, polc[i].kiadas, polc[i].kategoria, polc[i].nyelv))




KonyvFile.readFile()
