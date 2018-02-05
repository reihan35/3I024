from exo2 import *
import sys

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
    tab=dict()
    for i in listfic:
        tmp=frequence(i)
        print(tmp)
        for c,v in tmp.items():
        	if c in tab.keys(): #parcours des cles et maj de l'occurence
        		tab[c]=tab[c]+tmp[c]
        	else:
        		tab[c]=tab[c]+tmp[c]

    for c,v in tab.items():
        v=v/len(listfic)

    return tab

l=["afic1.txt","afic2.txt","afic3.txt"]
freqFr(l)
    
'''def main(argv):
	l=[]
	for i in argv:
		l.append(i)
		
	tab=freqFr(l)

	for c,v in tab.items():
		print(str(c)+" "+str(v)+"\n")
		
main(sys.argv)
    '''
