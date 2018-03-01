import math
import statistics
import sys

tabFr={'A':9.42,'B':1.02,'C':2.64,'D':3.39,'E':15.87,'F':0.95,'G':1.04,'H':0.77,'I':8.41,'J':0.89,'K':0.00,'L':5.34,'M':3.24,'N':7.15,'O':5.14,'P':2.86,'Q':1.06,'R':6.46,'S':7.09,'T':7.26,'U':6.24,'V':2.15,'W':0.00,'X':0.30,'Y':0.24,'Z':0.32}

def file_to_text(fic):
	'''fonction qui transforme un fichier en une chaine de caracter'''
	fic1=open(fic,'r')
	text=""
	for line in fic1:
		for s in line:
			text=text+s
	return text

def vigenere_table():
	'''fonction utilisée pour creer le tableau de vigenere'''
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

def vigenere_dechif(chaine,cle):
	'''fonction qui dechiffre un texte chiffré en vigenre avec une clef'''

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

def frequence(text):
	'''fonction qui renvoi la frequence des lettre dans un fichier'''

	alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

	total=0
	car = dict();

	for s in text: #parcour de chaque carcter dans le dictionnaire
		total=total+1; #nbr total des caracters
		if s in car.keys(): #parcours des cles et maj de l'occurence
			car[s]=car[s]+1
		else:
			car[s]=1

	for k in car.keys(): #calcul du pourcentage
		car[k] = car[k]*100/total

	for i in alphabet:
		if i not in car.keys():
			car[i]=0

	return car

def string_to_matrice(string,i):
	'''fonction qui transforme un texte en une matrice ou chaque mot de longueur i est un element de cette matrice'''
	l=[]
	m=[]
	cpt=0

	for j in range(0,len(string),i):
		m.append(string[j:j+i])

	return m

def trouve_colonne(matrice,n):
	'''fonction qui construit la colonne i'''
	string=""
	l=[]

	for i in range (1,n+1):
		string=""
		for j in matrice:
			string=string+j[i-1:i]

		l.append(string)

	return l

def cesar_dechif(chaine,cle):
	'''fonction de dechiffrement de cesar'''
	s=""
	alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

	permut=alphabet.index(cle) #recuperation de la position de la cle dans l'alphabet

	for c in chaine:
		ind = alphabet.index(c)
		s = s + alphabet[(ind-permut)%26]
	return  s

tabFr={'A':9.42,'B':1.02,'C':2.64,'D':3.39,'E':15.87,'F':0.95,'G':1.04,'H':0.77,'I':8.41,'J':0.89,'K':0.00,'L':5.34,'M':3.24,'N':7.15,'O':5.14,'P':2.86,'Q':1.06,'R':6.46,'S':7.09,'T':7.26,'U':6.24,'V':2.15,'W':0.00,'X':0.30,'Y':0.24,'Z':0.32}

def average(x):
    assert len(x) > 0
    return float(sum(x)) / len(x)

def pearson_def(x, y):
    assert len(x) == len(y)
    n = len(x)
    assert n > 0
    avg_x = average(x)
    avg_y = average(y)
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    for idx in range(n):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff

    return diffprod / math.sqrt(xdiff2 * ydiff2)

def max_dic(dic):
	'''fonction qui renvoi le maximum des valeurs d'un dictionnair'''
	l=[]
	for k,v in dic.items():
		l.append(v)

	return max(l)

def correlation_colonne(textchiff,i):
	'''fonction qui applique la formule de correlation de pearson sur les colonnes declalées de i'''
	matrice=string_to_matrice(textchiff,i)
	s=trouve_colonne(matrice,i)
	m=0
	l2=[]
	alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	l={}
	for j in s: #pour chaque colonne ck
		for i in alphabet: #on fait un chiffrement de cesar
			d=frequence(cesar_dechif(j,i))
			m=pearson_def(sort_dicti(tabFr), sort_dicti(d)) #et on calcul la correlation de pearson
			l[i]=m
		l2.append(max_dic(l)) #On trouve la correlation maximale

	return average(l2) #et on renvoi la moyenne des correlations maximales

def correlation(textchiff):
	'''fonction qui renvoi la longeure de la clef'''
	l=[]
	key=0
	for i in range (4,21):
		tmp=correlation_colonne(textchiff,i)
		l.append(tmp)

	for i in l:
		if i>0.7:
			return l.index(i)+4


def key_of(textchiff):
	'''fonction qui renvoi la clef'''
	key=correlation(textchiff) #renvoie la longueur de la clef
	return find_key(textchiff,key)

def find_key(textchiff,i):
	'''fonction qui construit la clef une fois que l'on connait sa taille'''
	l=[]
	l2=[]
	matrice=string_to_matrice(textchiff,i)
	s=trouve_colonne(matrice,i)
	m=0
	string=""
	alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	l={}
	for j in s: #pour chaque colonne ck
		for i in alphabet:
			d=frequence(cesar_dechif(j,i))
			m=pearson_def(sort_dicti(tabFr), sort_dicti(d))
			l[i]=m
		string=string+list(l.keys())[list(l.values()).index(max_dic(l))]
		l2.append(max_dic(l))

	return string

def cryptanalyse_V_colonne_i(fic1):
	'''fonction qui ecrit la clef et le texte dechiffré dans 2 fichiers separés'''
	text=file_to_text(fic1+".cipher")
	fic2 = fic1 + ".key"
	fic3 = fic1 + ".plain"
	fi2=open(fic2,"w")
	fi3=open(fic3,"w")

	fi2.write(key_of(text))
	fi3.write(vigenere_dechif(text,key_of(text)))

def sort_dicti(dic):
	'''fonction qui ordonne un dictionnair en ordre alphabetique'''
	l=[]
	for key in sorted(dic.keys()):
		l.append(dic[key])
	return l

def main():
	if len(sys.argv)!=2:
		print("Il faut mettre exactement 1 argument")
		return 0
	else:
		cryptanalyse_V_colonne_i(sys.argv[1])
		print ("Votre fichier : "+sys.argv[1]+" a été cryptanalysé ! :)")
		print("la clé secrete se trouve dans le fichier "+sys.argv[1]+".key et le texte dechiffré dans le fichier "+sys.argv[1]+".plain")

main()
