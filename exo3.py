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

	for c in chaine: #pour chaque lettre du mot on rajoute a sa postion la position de la cle modulo 26
		ind = alphabet.index(c) 
		s = s + alphabet[(ind-permut)%26]
	
	return  s

def mono_alph_chif(chaine,newalph):#chaine:le message a coder et sub le codage
	
	alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	
	string=""
	for i in chaine:
		ind = alphabet.index(i) #index de la lettre dans l'alphabet initial
		string = string + newalph[ind] #On recupere la valeur associée à la lettre (de la chaine) dans le dictionaire
        
	return string


def mono_alph_dechif(chaine,newalph):#chaine:le message a coder et sub le codage 
	alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	
	string=""
	for i in chaine:
		ind = newalph.index(i) #index de la lettre dans l'alphabet initial
		string = string + alphabet[ind] #On recupere la valeur associée à la lettre (de la chaine) dans le dictionaire
        
	return string

#s1=mono_alph_chif("ALPHA","POIUZTREWQLKJHGFDSAMNBVCXY")
#s=mono_alph_dechif("PKFEP","POIUZTREWQLKJHGFDSAMNBVCXY")
#print(s1 + s)

def vigenere_table():#fonction utilisée pour creer le tableau de vigenere 
	alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	
	table=[]
	p=0
	tmp=[]

	for i in range(0,len(alphabet)):	#Constructuin d'une matrice ou chaque ligne est les lettre d'alphabet decale de 1
		tmp=[]		
		for a in range(0,25):	
			tmp.append(alphabet[(i+a)%26])
			
		table.append(tmp)
	
	#print(table)

	return table

def vigenere_chif(chaine,cle):#fonction de chiffrement vigenere
	
	table=vigenere_table()
	
	alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	s=""
	for i in range(0,len(chaine)):
		lon=len(cle)
		ind=(i%lon)
		key=cle[ind]
		s = s + table[alphabet.index(key)][alphabet.index(chaine[i])]
	return s

def vigenere_dechif(chaine,cle):#On verifie si dans la ligne de chaque lettre de la cle la lettre de la chaine et on renvoie la colonne correspondante

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


