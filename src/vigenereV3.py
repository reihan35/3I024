import math
import statistics
tc="ABPWHIXKOCRPFQZVAGYBEKGYGVOLAAVCCEFHRGLNIIGNWVMTAAUPJWOZQWAYCBOAAKJCZBLZJAYVPQEEKBNLRIBVAYWFNOVCKGHHZJCJDLXKPDLRPORLIFASRRVLBLOGPEVMCNSRFVABEMQQIRFVRBZONAPFREDRIAWOBCBKHQVMWEFCXHAAVQTAVCBVWVKBPYBIBHQEZBWTNGOQLBJAGHNTZKZREQOWYXOGHRJJQPFTLPYVCFCJGJAGONWBOIRRQVAAUPSQRCNWQAWOCLCVXOWCFOVAPVPVPEFMDANLMQQEVQTAIIXKHRJJQPFJBPRBCBPPYVPGYEZQUNRJQGJGCBULEZQGOGWLTPZRFUHNTECEEVPVBNZYNAYRSKAAVPVLNJIQJTLBGHYVBUPYROIAWVPWEFRIJKCZQCHWRFGPRWOCLCVMCNYRCQQQIBUEGLOGCNIAGOYVPRWEFIGORCIGOAVPKCAZCKAAKMCOIIXKIREQINNEAEDBJB"


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


def correlation_colonne(textchiff,i):
	l=[]
	l2=[]
	matrice=string_to_matrice(textchiff,i)
	s=trouve_colonne(matrice,i)
	#s2=text_to_xi(textFr) #les xi (concernant le texte en francais)
	#les yi de la colonne
	m=0
	for j in s: #pour chaque colonne ck
		l=[]
		for k in text_to_xi(j): # la colonne decalé de i
			tmp=dict_to_list(k)
			m=pearson_def(dict_to_list(tabFr), tmp)
			l.append(m)
		l2.append(max(l))
	return average(l2)

def correlation(textchiff):
	l=[]
	key=0
	for i in range (4,20):
		tmp=correlation_colonne(textchiff,i)
		l.append(tmp)
	print(l)

	for i in l:
		if i>0.7:
			return l.index(i)+4


tc="GFGRJCGUVCGIECNPFITTFNLJVUUPCIETSTLRXTZNYATKEHDBRCJSUDDOHBKETQLHJNRYWIUICFNPUBIKEBPNCEDGBVFVYYZJXCVGBCFJADKMTSOAIDQIKXUOGZNCUWPJMDKNEQIAFLWUBJYJBBLVUNTJAPJXRKGTDWPONFZJBUJPWUVJDCUXGBHQUYTKISFZNYATTVHFLEUDGIVCDFNIBTUKSFNEUATFIXNUATNYUETTUVIYPIUPOMRHDCFRHEYFQUHQRJDOAULDBZTSHRINEBRXONWQVPYJSBPBYABQCPVFBRNUHFCUUYTNAXVBJMCXNGUXPVWUU"
#correlation_colonne(tc,3)
print(correlation(tc))
