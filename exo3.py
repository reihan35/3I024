def cesar_chif(chaine,x):
    return chaine[x:] + chaine[:x] #[x:]= de x (exclu en comptant de 1) jusqua a la fin de la chaine et [:x]=du debut de la chaine jusqu a x (inclus)
 
def cesar_dechif(chaine,x):
    return chaine[x:] + chaine[:x] # on change et de ne pas faire la rotation

string=cesar_chif("ABCDEF",3)   #DEFABC
string2=cesar_dechif(string,3)
print("avant le chiffre : ABCDEF")
print("apres le chiffre:"+string)
print("avant le dechiffre "+string)
print("apres le dechiffre:"+string2)

def mono_alph_chif(chaine,sub):#chaine:le message a coder et sub le codage
    string=""
    for i in chaine:
        string = string + sub.get(i) # get(i) obtenir la cle
        
    return string
    
dc = {"h":"x","e":"w","o":"z","l":"a"}
s=mono_alph_chif("hello",dc)
print(s)

def mono_alph_dechif(chaine,sub):#chaine:le message a coder et sub le codage
    string=""
    for i in chaine:
        for c,v in sub.items(): #On parcours le dictionnaire 
            if v==i:#si la valeur est la meme que le caracter i dans la chaine 
                string = string + c #On recupere la cle (On transforme i en c)
    
    return string


s2=mono_alph_dechif("xwaaz",dc)
print(s2)
