from exo2 import *
import sys
import operator

def frequence(fic):#fonction qui renvoi la frequence des lettre dans un fichier'''
    fic1=open(fic,'r')
    car = dict();
    total=0;
    for line in fic1: #parcour du dictionnaire 
        for s in line: #parcour de chaque carcter dans le dictionnaire
            total=total+1; #nbr total des caracters
            if s in car.keys(): #parcours des cles et maj de l'occurence
                car[s]=car[s]+1
            else:
                car[s]=1
    
    for k in car.keys(): #calcul du pourcentage
        car[k] = car[k]*100/total

    return car

def freqFr(listfic):#fonction qui renvoie le tableau des frequances de la langues francaise'''
    tab={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
    for i in listfic:# On parcours la liste des fichiers
    	tmp=frequence(i)
    	for c,v in tmp.items(): #On fait la moyenne des frequences pour les fichiers donc cette boucle fait la somme
    		tab[c]=tab[c]+tmp[c]

    for c,v in tab.items(): #et cette boucle divise par le nombre de fichiers pour trouver la moyenne
        v=v/len(listfic)

    return tab

def cryptanalyse(tabFr,fic,fic2):#fonction de la cryptanalyse elle prend le fichier fic chiffré et renvoie fichier fic2 dechiffre'''
	tab1=frequence(fic); #On construit le tableau des frequances du fichier chiffrés
	tab_trie=sorted(tab1.items(), reverse=True, key=operator.itemgetter(1)) #On va ordonner les elements de manier decroissantes (la lettre ayant la frequnce la plus elevee au debut)
	print(tab_trie)
	freqFr_trie=sorted(tabFr.items(), reverse=True, key=operator.itemgetter(1)) #On va ordonner les elements de manier decroissantes (la lettre ayant la frequnce la plus elevee au debut) 
	print(freqFr_trie)
	l1=[] #liste des frequences des lettres dans l'alphabet
	l2=[] #liste des frequences des lettre dans le text chiffre
	crypt=dict()
	for c1,v2 in freqFr_trie:  #On parcours le tableau et on rajoute chaque lettre rencontrées (donc la liste des lettre croissante)
		l1.append(c1)
	print(l1)
	
	for c,v in tab_trie: #On fait de meme pour le fichier chiffre
		l2.append(c)
	print(l2)
	 	
	size=len(l2)# On parcours les listes 
	for i in range(0,size):
		print("la lettre "+l1[i]+" dans le text chiffre pourrait etre "+l2[i]+" dans l'alphabet")
		crypt[l1[i]]=l2[i]
	 	
	fic1=open(fic,'r')
	fic2=open(fic2,'w')
	 
	#for line in fic1: #On parcour le dictionnaire 
#		for s in line:
#			fic2.write(crypt[s])
#	
	return 1


l=["afic1.txt","afic2.txt","afic3.txt"]
tab=freqFr(l)
dicti=cryptanalyse(tab,"afic2.txt","dechiffre")
print(dicti)

'''def main(argv):
	l=[]
	for i in argv:
		l.append(i)
		
	tab=freqFr(l)

	for c,v in tab.items():
		print(str(c)+" "+str(v)+"\n")
		
main(sys.argv)'''
