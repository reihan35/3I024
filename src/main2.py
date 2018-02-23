import sys
from exo3 import *
from exo4 import *

def main():
	print("******************Bienvenue !********************")
	while True:
		print("*******************************************")
		print("Voici la liste des choix possibles :")
		print("0 : chiffrer un text avec chiffrement de cesar")
		print("1 : chiffrer un text avec chiffrement monoalphabetique")
		print("2 : chiffrer un text avec chiffrement polyalphabetique")
		print("3 : dechiffrer un text avec chiffrement de cesar")
		print("4 : dechiffrer un text avec chiffrement monoalphabetique")
		print("5 : dechiffrer un text avec chiffrement polyalphabetique")
		print("6 : cryptanalyser un text chiffré avec cesar")
		print("7 : cryptanalyser un text chiffré avec chiffrement mono alphabetique ")	
		print("8 : cryptanalyser un text chiffré avec chiffrement polyalphabetique ")	
		print("9 : sortir")	
		x = input("Que souhaitez vous faire ?")
		print("Vous avez choisi "+x)
		
		if(x=='0'):
			s=input("Saissiez votre texte (en MAJUSCULE) :")
			cle=input("Saissiez votre cle (en MAJUSCULE):")
			chiffre=cesar_chif(s,cle)
			print("Voici le resultat :")
			print(chiffre)

		if(x=='3'):
			s=input("Saissiez votre texte (en MAJUSCULE) :")
			cle=input("Saissiez votre cle (en MAJUSCULE):")
			chiffre=cesar_dechif(s,cle)
			print("Voici le resultat :")
			print(chiffre)
		
		if(x=='1'):
			s=input("Saissiez votre texte (en MAJUSCULE) :")
			cle=input("Saissiez votre cle (en MAJUSCULE):")
			chiffre=mono_alph_chif(s,cle)
			print("Voici votre texte en chiffre :")
			print(chiffre)
		
		if(x=='4'):
			s=input("Saissiez votre texte (en MAJUSCULE) :")
			cle=input("Saissiez votre cle (en MAJUSCULE):")
			chiffre=mono_alph_dechif(s,cle)
			print("Voici votre texte en chiffre :")
			print(chiffre)
		if(x=='2'):
			s=input("Saissiez votre texte (en MAJUSCULE) :")
			cle=input("Saissiez votre cle (en MAJUSCULE):")
			chiffre=vigenere_chif(s,cle)
			print("Voici votre texte en chiffre :")
			print(chiffre)

		if(x=='5'):
			s=input("Saissiez votre texte (en MAJUSCULE) :")
			cle=input("Saissiez votre cle (en MAJUSCULE):")
			dechiffre=vigenere_dechif(s,cle)
			print("Voici le resultat :")
			print(dechiffre)

		if(x=='6'):
			fic1=input("Saissiez le nom du fichier que vous souhaitez cryptanalyser:")
			fic2=input("Choissiez un nom pour votre fichier de cryptanalyse:")
			tabFr={'A':8.40,'B':1.06,'C':3.03,'D':4.18,'E':17.26,'F':1.12,'G':1.27,'H':0.92,'I':7.34,'J':0.31,'K':0.05,'L':6.01,'M':2.96,'N':7.13,'O':5.26,'P':3.01,'Q':0.99,'R':6.55,'S':8.08,'T':7.07,'U':5.74,'V':1.32,'W':0.04,'X':0.45,'Y':0.30,'Z':0.12}
			cryptanalyse_cesar(tabFr,fic1,fic2)
			print("Votre fichier 'dechiffré' qui s'appel "+fic2+" se trouve dans votre repartoir")

		if(x=='7'):
			fic1=input("Saissiez le nom du fichier que vous souhaitez cryptanalyser:")
			fic2=input("Choissiez un nom pour votre fichier de cryptanalyse:")
			tabFr={'A':8.40,'B':1.06,'C':3.03,'D':4.18,'E':17.26,'F':1.12,'G':1.27,'H':0.92,'I':7.34,'J':0.31,'K':0.05,'L':6.01,'M':2.96,'N':7.13,'O':5.26,'P':3.01,'Q':0.99,'R':6.55,'S':8.08,'T':7.07,'U':5.74,'V':1.32,'W':0.04,'X':0.45,'Y':0.30,'Z':0.12}
			cryptanalyse_monoalph(tabFr,fic1,fic2)
			print("Votre fichier 'dechiffré' qui s'appel "+fic2+" se trouve dans votre repartoir")

		if(x=='9'):
			print("Merci et a bien tot ! o/")
			print("*******************************************")		
			break
	
	return 0

main()
