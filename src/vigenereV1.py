#from exo3 import *
import sys
import operator

def file_to_text(fic): #fonction qui transforme un fichier en une chaine de caracter
	fic1=open(fic,'r')	
	text=""
	for line in fic1:
		for s in line:
			text=text+s
	return text

def vigenere_table():#fonction utilisée pour creer le tableau de vigenere 
	alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	
	table=[]
	p=0
	tmp=[]

	for i in range(0,len(alphabet)):#Constructuin d'une matrice ou chaque ligne est les lettre d'alphabet decale de 1
		tmp=[]		
		for a in range(0,26):	
			tmp.append(alphabet[(i+a)%26])
			
		table.append(tmp)


	return table
	
def vigenere_dechif(chaine,cle):#fonction qui dechiffre un texte chiffré en vigenre avec une cle

	table=vigenere_table()
	
	alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	s=""

	for a in range(0,len(chaine)):#pour chaque lettre dans la chaine
		ind=a%len(cle) #on retrouve l'indice de la lettre(sa position dans la cle) dans cle qui est associé a elle
		alph=alphabet.index(cle[ind]) #on retrouve ensuite la position de cette lettre dans l'alphabet
		tmp=table[alph] #On retrouve la ligne qui correspond a la lettre de la cle
		for i in tmp: #On parcours chaque element de cette liste et quand on retrouve la lettre de la chaine et recupere la colonne de cette lettre et on l'ajoute a s
			if i==chaine[a]:
				ind2=tmp.index(i)
				s = s + alphabet[ind2]
	return s
	
def cesar_dechif(chaine,cle):#fonction de chiffrement de cesar 
	s=""   
	alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	
	permut=alphabet.index(cle) #recuperation de la position de la cle dans l'alphabet

	for c in chaine: #pour chaque lettre du mot on rajoute a sa postion la position de la cle modulo 26
		ind = alphabet.index(c) 
		s = s + alphabet[(ind-permut)%26]
	
	return  s

def frequence(str):#fonction qui renvoi la frequence des lettres dans un fichier

	car=dict()
	total=0; #parcour du dictionnaire 
	for s in str: #parcour de chaque carcter dans le dictionnair
		total=total+1; #nbr total des caracter
		if s in car.keys(): #parcours des cles et maj de l'occurence
			car[s]=car[s]+1
		else:
			car[s]=1
	for k in car.keys(): #calcul du pourcentage
		car[k] = car[k]*100/total
	return car

#le tableau des frequences des lettres en francais  

tabFr={'A':9.42,'B':1.02,'C':2.64,'D':3.39,'E':15.87,'F':0.95,'G':1.04,'H':0.77,'I':8.41,'J':0.89,'K':0.00,'L':5.34,'M':3.24,'N':7.15,'O':5.14,'P':2.86,'Q':1.06,'R':6.46,'S':7.09,'T':7.26,'U':6.24,'V':2.15,'W':0.00,'X':0.30,'Y':0.24,'Z':0.32}

def indic_co(fic,tabFr):
	fic1=open(fic,"r")
	long=0	
	for line in fic1:
		for s in line:	
			long=long+1
	s=0
	a=0
	for i,v in tabFr.items() :
		a=v*long/100		
		s=s+(a*(a-1))
	return s/(long*(long-1))



def indic_coi(string):#fonction qui renvoie l'indice de coincidance d'un texte
	s=0
	a=0
	long=len(string)
	tab=frequence(string)
	
	for i,v in tab.items() :
		a=v*long/100		
		s=s+(a*(a-1))
	
	return s/(long*(long-1))


def string_to_matrice(string,i):#fonction qui transforme un texte en une matrice ou chaque mot de longueur i est un element de cette matrice

	l=[]	
	m=[]
	cpt=0
	
	for j in range(0,len(string),i):		
		m.append(string[j:j+i])		
	
	return m

def trouve_colonne(matrice,n): #fonction qui construit la colonne i 
	string=""
	l=[]
	
	for i in range (1,n+1):
		string=""
		for j in matrice:
			string=string+j[i-1:i]

		l.append(string)
	
	return l
	
def indic_co_colonne(matrice,i): #fonction qui calcule l'indice de coincidance de la colonne i et l'indice moyenne de coincidance 
	
	string=""
	l=trouve_colonne(matrice,i)
	#print(l)
	s=0
	h=[]
	
	for i in range (0,len(l)):
		#print(l[i])
		#print(indic_coi(l[i]))
		h.append(indic_coi(l[i]))
		s=s+indic_coi(l[i])

	return s/len(l)



def long_cle(string):#fonction qui calcule la longeure de la cle en creant la matrice a partire du texte , construsant les colonnes et trouvant l'indice de coincidance des colonnes 
	
	l=[]	
	
	for i in range(4,20):#On teste differentes valeurs de i
		matrice=string_to_matrice(string,i)
		l.append(indic_co_colonne(matrice,i))
	for i in l:
		if i>0.07:
			return l.index(i)+4	 


def cryptanalyse_cesar(tabFr,fic):#fonction de la cryptanalyse elle prend le fichier fic chiffré et renvoie la cle du chiffrement
	
	alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	tab1=frequence(fic); #On construit le tableau des frequances du fichier chiffrés
	#print(tab)
	tab_trie=sorted(tab1.items(), reverse=True, key=operator.itemgetter(1)) #On va ordonner les elements de manier decroissantes (la lettre ayant la frequnce la plus elevee au debut)
	#print(tab_trie)
	freqFr_trie=sorted(tabFr.items(), reverse=True, key=operator.itemgetter(1)) #On va ordonner les elements de manier decroissantes (la lettre ayant la frequnce la plus elevee au debut) 
	#print(freqFr_trie)
	l1=[] #liste des frequences des lettres dans l'alphabet
	l2=[] #liste des frequences des lettre dans le text chiffre
	crypt=dict()
	for c1,v2 in freqFr_trie:  #On parcours le tableau et on rajoute chaque lettre rencontrées (donc la liste des lettre croissante)
		l1.append(c1)
	
	#print("Voici la list (decroissante) des lettres les plus utilisée dans la langue francaise")	
	#print(l1)
	
	#print("Voici la liste (decroissante) des lettres les plus utilisée du text fournis ")
	for c,v in tab_trie: #On fait de meme pour le fichier chiffre
		l2.append(c)
	#print(l2)
	 	
	size=len(l2)# On parcours les listes 
	
	
	ind=l1.index("A")
	#print("la lettre "+l1[0]+" peut etre "+l2[0]+" en francais")
	#crypt[l1[i]]=l2[i]
	a=alphabet.index(l1[0])
	permut =( alphabet.index(l2[0])- a )% 26
	#print(permut)	
	

	cle = alphabet[permut]
	#print(cle)
	
	return cle


def cryptanalyse_V_colonne_i(tabFr,fic1): #fonction de la cryptanalyse de vigenere qui prend un fichier et renvoie un fichier ayant la cle et un autre ayant le texte dechiffre

	text=file_to_text(fic1+".cipher")
	fic2 = fic1 + ".key"
	fic3 = fic1 + ".plain"
	fi2=open(fic2,"w")
	fi3=open(fic3,"w")
	key=long_cle(text)
	#print(key)
	matrice=string_to_matrice(text,key)
	s=trouve_colonne(matrice,key)
	#print(s)
	key=""
	for i in s:
		key=key+cryptanalyse_cesar(tabFr,i)
	
	
	fi2.write(key)
		
	#print(vigenere_dechif(matn,key))
	fi3.write(vigenere_dechif(text,key))

def main():
	if len(sys.argv)!=2:
		print("Il faut mettre exactement 1 argument")
		return 0
	else:
		cryptanalyse_V_colonne_i(tabFr,sys.argv[1])
		print ("Votre fichier : "+sys.argv[1]+" a été cryptanalysé ! :)")
		print("la clé secrete se trouve dans le fichier "+sys.argv[1]+".key et le texte dechiffré dans le fichier "+sys.argv[1]+".plain")

main()	

matn="ABPWHIXKOCRPFQZVAGYBEKGYGVOLAAVCCEFHRGLNIIGNWVMTAAUPJWOZQWAYCBOAAKJCZBLZJAYVPQEEKBNLRIBVAYWFNOVCKGHHZJCJDLXKPDLRPORLIFASRRVLBLOGPEVMCNSRFVABEMQQIRFVRBZONAPFREDRIAWOBCBKHQVMWEFCXHAAVQTAVCBVWVKBPYBIBHQEZBWTNGOQLBJAGHNTZKZREQOWYXOGHRJJQPFTLPYVCFCJGJAGONWBOIRRQVAAUPSQRCNWQAWOCLCVXOWCFOVAPVPVPEFMDANLMQQEVQTAIIXKHRJJQPFJBPRBCBPPYVPGYEZQUNRJQGJGCBULEZQGOGWLTPZRFUHNTECEEVPVBNZYNAYRSKAAVPVLNJIQJTLBGHYVBUPYROIAWVPWEFRIJKCZQCHWRFGPRWOCLCVMCNYRCQQQIBUEGLOGCNIAGOYVPRWEFIGORCIGOAVPKCAZCKAAKMCOIIXKIREQINNEAEDBJB"
#mat=string_to_matrice(matn,3)
#print(mat)
#trouve_colonne(mat,3)
#print(indic_co_colonne(mat,3))
'''key=long_cle(matn)
print(key)
matrice=string_to_matrice(matn,key)
s=trouve_colonne(matrice,key)
print(s)
for i in s:
	cryptanalyse_cesar(tabFr,i)
cryptanalyse_V_colonne_i(tabFr,"text3")	
	
#print(vigenere_dechif(matn,"RXCWN"))	
#matrice=string_to_matrice(matn,5)
#print(trouve_colonne(matrice,0))
#print(indic_co_colonne(matrice))
#print(long_cle(matn))
#print(mat)
#trouve_colonne(mat,3)'''
