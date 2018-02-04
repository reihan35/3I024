def cesar(chaine,cle):#la fonction s'utilise a la fois pour chiffrer et dechiffrer
	s=""   
	alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	
	permut=alphabet.index(cle) #recuperation de la position de la cle dans l'alphabet

	for c in chaine: #pour chaque lettre du mot on rajoute a sa postion la position de la cle modulo 26
		ind = alphabet.index(c) 
		s = s + alphabet[(ind+permut)%26]
	
	return  s

string=cesar("ivirynpelcgbybtvr","n")
print(string)

def mono_alph_chif(chaine,newalph):#chaine:le message a coder et sub le codage
	
	alph = {1:'a',2:'a',3:'a',4:'a',5:'a',6:'a',7:'a',8:'a',9:'a',11:'a',12:'a',13:'a',14:'a',15:'a',16:'a',17:'a',18:'a',19:'a',20:'a',21:'a',22:'a',23:'a',24:'a',25:'a',26:'a',27:'a'}

	alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]	
	
	for i in range(1,len(newalph)): #On parcour newalph et on associe a chque lettre sa remplacente dans le dictionnaire (les cle dans le dictionnaire sont la position des lettre dans l'aphabet classique et les valurs sont le lettres de newalph)
		alph[i]=newalph[i]
	    
	string=""
	for i in chaine:
		ind = alphabet.index(i) #index de la lettre dans l'alphabet initial
		string = string + alph[ind] #On recupere la valeur associée à la lettre (de la chaine) dans le dictionaire
        
	return string
    
s=mono_alph_chif("hello","abcdwfgxijkamnzpqrstuvwxyz")
#s=mono_alph_chif("xwaaz","abcdefghijklmnopqrstuvwxyz")
#print(s)	
	
def vigenere_table():#fonction utilisée pour creer le tableau de vigenere 
	alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	
	table=[]
	p=0
	tmp=[]

	for i in range(0,len(alphabet)):	#Constructuin d'une matrice ou chaque ligne est les lettre d'alphabet decale de 1
		tmp=[]		
		for a in range(0,26):	
			tmp.append(alphabet[(i+a)%26])
		table.append(tmp)
	
	return table


def vigenere_chif(chaine,cle):#fonction de chiffrement vigenere
	
	table=vigenere_table()
	
	alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	s=""
	for c in chaine:
		ind=(chaine.index(c))%len(cle)
		key=cle[ind]
		s = s + table[alphabet.index(key)][alphabet.index(c)]
	return s

def vigenere_dechif(chaine,cle):#On verifie si dans la ligne de chaque lettre de la cle la lettre de la chaine et on renvoie la colonne correspondante

	table=vigenere_table()
	
	alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	s=""

	for a in range(0,len(chaine)):#pour chaque lettre dans la chaine
		ind=a%len(cle) #on retrouve l'indice de la lettre(sa position dans la cle) dans cle qui est associé a elle
		alph=alphabet.index(cle[ind]) #on retrouve ensuite la position de cette lettre dans l'alphabet
		tmp=table[alph] #On retrouve la ligne qui correspond a la lettre de la cle
		for i in tmp: #On parcours chaque element de cette liste et quand on retrouve la lettre de la chaine et recupere la colonne de cette lettre et on l'ajoute a s
			if i==chaine[a]:
				ind2=tmp.index(i)
				s = s + alphabet[ind2]
	print(s)

vigenere_dechif("xsmsrxirdvleiuvnumejrsanku","cesar")
vigenere_chif("lattaqueestprevuepourdemain","cipher")

