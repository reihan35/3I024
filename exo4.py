from exo2 import *
import sys
import operator

def frequence(fic):
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

def freqFr(listfic):
    tab={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
    for i in listfic:
    	tmp=frequence(i)
    	for c,v in tmp.items():
    		tab[c]=tab[c]+tmp[c]

    for c,v in tab.items():
        v=v/len(listfic)

    return tab

def cryptanalyse(tabFr,fic,fic2):
	 
	 tab1=frequence(fic);
	 tab_tire=sorted(tab1.items(), reverse=True, key=operator.itemgetter(1))
	 freqFr_tire=sorted(tabFr.items(), reverse=True, key=operator.itemgetter(1))
	 l1=[]
	 l2=[]
	 
	 crypt=dict()
	 
	 for c1,v2 in freqFr_tire: 
	 	l1.append(c1)
	 	
	 for c,v in tab_tire:
	 	l2.append(c)
	 	
	 size=len(l1)
	 for i in range(0,size):
	 	print("la lettre "+l1[i]+" pourrait etre "+l2[i])
	 	crypt[l1[i]]=l2[i]
	 	
	 fic1=open(fic,'r')
	 fic2=open(fic2,'w')
	 
	 for line in fic1: #parcour du dictionnaire 
	 	for s in line:
	 		fic2.write(crypt[s])
	 		 
	 return crypt


l=["afic1.txt","afic2.txt","afic3.txt"]
tab=freqFr(l)
dicti=cryptanalyse(tab,"texte_a_dechiffrer_Vigenere","dechiffre")
print(dicti)

'''def main(argv):
	l=[]
	for i in argv:
		l.append(i)
		
	tab=freqFr(l)

	for c,v in tab.items():
		print(str(c)+" "+str(v)+"\n")
		
main(sys.argv)'''
