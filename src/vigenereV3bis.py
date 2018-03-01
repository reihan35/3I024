import math
import statistics
import sys

tc="ABPWHIXKOCRPFQZVAGYBEKGYGVOLAAVCCEFHRGLNIIGNWVMTAAUPJWOZQWAYCBOAAKJCZBLZJAYVPQEEKBNLRIBVAYWFNOVCKGHHZJCJDLXKPDLRPORLIFASRRVLBLOGPEVMCNSRFVABEMQQIRFVRBZONAPFREDRIAWOBCBKHQVMWEFCXHAAVQTAVCBVWVKBPYBIBHQEZBWTNGOQLBJAGHNTZKZREQOWYXOGHRJJQPFTLPYVCFCJGJAGONWBOIRRQVAAUPSQRCNWQAWOCLCVXOWCFOVAPVPVPEFMDANLMQQEVQTAIIXKHRJJQPFJBPRBCBPPYVPGYEZQUNRJQGJGCBULEZQGOGWLTPZRFUHNTECEEVPVBNZYNAYRSKAAVPVLNJIQJTLBGHYVBUPYROIAWVPWEFRIJKCZQCHWRFGPRWOCLCVMCNYRCQQQIBUEGLOGCNIAGOYVPRWEFIGORCIGOAVPKCAZCKAAKMCOIIXKIREQINNEAEDBJB"
tabFr={'A':7.42,'B':1.14,'C':3.18,'D':3.67,'E':14.43,'F':1.11,'G':1.23,'H':1.11,'I':4.96,'J':0.34,'K':0.29,'L':5.34,'M':2.62,'N':6.39,'O':5.02,'P':2.49,'Q':0.65,'R':6.07,'S':6.51,'T':5.92,'U':4.49,'V':1.11,'W':0.17,'X':0.38,'Y':0.46,'Z':0.15}
tabFr2={'A':9.42,'B':1.02,'C':2.64,'D':3.39,'E':15.87,'F':0.95,'G':1.04,'H':0.77,'I':8.41,'J':0.89,'K':0.00,'L':5.34,'M':3.24,'N':7.15,'O':5.14,'P':2.86,'Q':1.06,'R':6.46,'S':7.09,'T':7.26,'U':6.24,'V':2.15,'W':0.00,'X':0.30,'Y':0.24,'Z':0.32}

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

def frequence(text):#fonction qui renvoi la frequence des lettre dans un fichier'''
   	#parcour du dictionnaire

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

def cesar_chif(chaine,cle):
	s=""
	alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

	permut=alphabet.index(cle) #recuperation de la position de la cle dans l'alphabet

	for c in chaine: #pour chaque lettre du mot on rajoute a sa postion la position de la cle modulo 26
		ind = alphabet.index(c)
		s = s + alphabet[(ind+permut)%26]

	return  s

def cesar_dechif(chaine,cle):
	s=""
	alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

	permut=alphabet.index(cle) #recuperation de la position de la cle dans l'alphabet

	for c in chaine:
		ind = alphabet.index(c)
		s = s + alphabet[(ind-permut)%26]
	return  s


def moy_alph(dic):
	somme=0
	for k in dic.keys(): #calcul du pourcentage
		somme = somme + dic[k]

	return somme/26

def freq_to_number(dic,lentext):

	for k,v in dic.items():
		v=v*lentext//100
		dic[k]=v

	return dic

dic = {'Y': 0.22328548644338117, 'R': 6.507177033492823, 'A': 8.484848484848484, 'X': 0.7017543859649122, 'G': 0.8293460925039873, 'L': 5.741626794258373, 'Z': 0.2551834130781499, 'I': 7.464114832535885, 'E': 16.45933014354067, 'J': 0.19138755980861244, 'Q': 1.1802232854864434, 'M': 2.583732057416268, 'S': 8.61244019138756, 'C': 3.1259968102073366, 'D': 3.54066985645933, 'P': 3.1578947368421053, 'O': 5.996810207336523, 'F': 1.0207336523125996, 'K': 0.06379585326953748, 'H': 0.8931419457735247, 'V': 1.2759170653907497, 'N': 7.1451355661881975, 'B': 0.8293460925039873, 'T': 7.240829346092504, 'U': 6.475279106858054}


tabFr={'A':9.42,'B':1.02,'C':2.64,'D':3.39,'E':15.87,'F':0.95,'G':1.04,'H':0.77,'I':8.41,'J':0.89,'K':0.00,'L':5.34,'M':3.24,'N':7.15,'O':5.14,'P':2.86,'Q':1.06,'R':6.46,'S':7.09,'T':7.26,'U':6.24,'V':2.15,'W':0.00,'X':0.30,'Y':0.24,'Z':0.32}

def text_to_xi(text):
	alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	l=[]
	lmoy=[]
	moy=0

	for i in alphabet:
		d=freq_to_number((frequence(cesar_dechif(text,i))),len(text))
		l.append(d)

	return l

def dict_to_list(dic):
	li=[]

	for k,v in dic.items():
		li.append(v)
	return li

def listofdict_to_listoflist(l):
	l2=[]
	for i in l:
		l2.append(dict_to_list(i))

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
	l=[]
	for k,v in dic.items():
		l.append(v)

	return max(l)

def correlation_colonne(textchiff,i):
	matrice=string_to_matrice(textchiff,i)
	s=trouve_colonne(matrice,i)
	#s2=text_to_xi(textFr) #les xi (concernant le texte en francais)
	#les yi de la colonne
	m=0
	alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	l={}
	for j in s: #pour chaque colonne ck
		l2=[]
		for i in alphabet:
			d=frequence(cesar_dechif(j,i))
			m=pearson_def(sort_dicti(tabFr), sort_dicti(d))
			l[i]=m
		#print(max_dic(l))
		#print(list(l.keys())[list(l.values()).index(max_dic(l))])
		l2.append(max_dic(l))

	#print(l2)
	return average(l2)

def correlation(textchiff):
	l=[]
	key=0
	for i in range (4,20):
		#print(i)
		tmp=correlation_colonne(textchiff,i)
		l.append(tmp)
	#print(l)

	for i in l:
		if i>0.7:
			return l.index(i)+4
	return 0

def key_of(textchiff):
	key=correlation(textchiff) #renvoie la longueur de la clef
	#print(key)
	return find_key(textchiff,key)

def find_key(textchiff,i):
	l=[]
	l2=[]
	matrice=string_to_matrice(textchiff,i)
	s=trouve_colonne(matrice,i)
	#s2=text_to_xi(textFr) #les xi (concernant le texte en francais)
	#les yi de la colonne
	m=0
	string=""
	alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	l={}
	for j in s: #pour chaque colonne ck
		print(j)
		for i in alphabet:
			l2=[]
			d=frequence(cesar_dechif(j,i))
			m=pearson_def(sort_dicti(tabFr), sort_dicti(d))
			l[i]=m
		print(list(l.keys())[list(l.values()).index(max_dic(l))])
		string=string+list(l.keys())[list(l.values()).index(max_dic(l))]
		l2.append(max_dic(l))

	#print(string)
	#print(l2)
	return string

def cryptanalyse_V_colonne_i(fic1):
	text=file_to_text(fic1+".cipher")
	fic2 = fic1 + ".key"
	fic3 = fic1 + ".plain"
	fi2=open(fic2,"w")
	fi3=open(fic3,"w")

	fi2.write(key_of(text))
	fi3.write(vigenere_dechif(text,key_of(text)))

def sort_dicti(dic):
	#keylist.sort()
	l=[]
	for key in sorted(dic.keys()):
		#print(key)
		l.append(dic[key])
	return l

#print(sort_dicti({"b":2,"c":1,"a":4}))

def main():
	if len(sys.argv)!=2:
		print("Il faut mettre exactement 1 argument")
		return 0
	else:
		cryptanalyse_V_colonne_i(sys.argv[1])
		print ("Votre fichier : "+sys.argv[1]+" a été cryptanalysé ! :)")
		print("la clé secrete se trouve dans le fichier "+sys.argv[1]+".key et le texte dechiffré dans le fichier "+sys.argv[1]+".plain")

main()


tc="GFGRJCGUVCGIECNPFITTFNLJVUUPCIETSTLRXTZNYATKEHDBRCJSUDDOHBKETQLHJNRYWIUICFNPUBIKEBPNCEDGBVFVYYZJXCVGBCFJADKMTSOAIDQIKXUOGZNCUWPJMDKNEQIAFLWUBJYJBBLVUNTJAPJXRKGTDWPONFZJBUJPWUVJDCUXGBHQUYTKISFZNYATTVHFLEUDGIVCDFNIBTUKSFNEUATFIXNUATNYUETTUVIYPIUPOMRHDCFRHEYFQUHQRJDOAULDBZTSHRINEBRXONWQVPYJSBPBYABQCPVFBRNUHFCUUYTNAXVBJMCXNGUXPVWUU"
#print(vigenere_dechif(tc,"PQJPQJPQJPQJ"))
#correlation_colonne(tc,3)
#print(key_of(tc))
#print(vigenere_dechif(tc,"QUZHBGMTLQUVFE"))
