from exo4 import *
import sys
import operator

def indic_co(fic):
	tab = frequence(fic)
	print(tab)
	s=0
	o=0
	
	for i,v in tab.items() :
		s=s+(v*(v-1))
		o=o+s
		
	return s/(o*(o-1))

s=indic_co("afic1.txt")
print(s)


