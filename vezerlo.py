from beker import Konyv;
import information;
from kiolvas import KonyvFile;

eldontottuk=False;
while(not eldontottuk):
	valaszt=input("[0] Új könyv hozzáadása [1] állományban lévő könyvek listázása [2] kilépés: ");
	if valaszt=="0":
		konyvek=Konyv.beker();
		information.writeToFile(konyvek);
	elif valaszt=="1":
		KonyvFile.readFile();
	elif valaszt=="2":
		eldontottuk=True;
