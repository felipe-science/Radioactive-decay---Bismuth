import numpy as np
import pylab as pl
import random as rd


#Quantidade iniciais de átomos
NBi1 = 10000
NBi2 = 0
NTl  = 0
NPb  = 0

h = 1.0

h = 1.0
TauBi = 46*60.0
TauTl = 2.2*60.0
TauPb = 3.3*60.0
tmax = 20000

pBi = 1 - 2**(-h/TauBi)
pTl = 1 - 2**(-h/TauTl)
pPb = 1 - 2**(-h/TauPb)

#Listas dos pontos
tpoints = np.arange(0.0,tmax,h)
Bi1points = []
Bi2points = []
Tlpoints = []
Pbpoints = []

decaimento_Bi_Pb = 0
decaimento_Bi_Tl = 0
decaimento_Tl_Pb = 0
decaimento_Pb_Bi = 0


#Evolução do tempo
for t in tpoints:

	Bi1points.append(NBi1)
	Bi2points.append(NBi2)
	Tlpoints.append(NTl)
	Pbpoints.append(NPb)


	#Decaimento do chumbo para o bismuto
	decaimento_Pb_Bi = 0
	for i in range(0,NPb):
		if rd.random() < pPb:
			decaimento_Pb_Bi += 1

	NBi2 = NBi2 + decaimento_Pb_Bi		
	NPb  = NPb  - decaimento_Pb_Bi

	#Decaimento do telúrio para o chumbo
	decaimento_Tl_Pb = 0
	for i in range(0,NTl):
		if rd.random() < pTl:
			decaimento_Tl_Pb += 1
	NPb = NPb + decaimento_Tl_Pb
	NTl = NTl - decaimento_Tl_Pb



	#Decaimento do bismuto 1
	decaimento_Bi_Tl = 0
	decaimento_Bi_Pb = 0
	for i in range(0,NBi1):

		if rd.random() < 0.9791:
			#Bismuto -> chumbo
			if rd.random() < pBi:
				decaimento_Bi_Pb += 1

		else:
			if rd.random() < pBi:
				decaimento_Bi_Tl += 1				

	NPb = NPb + decaimento_Bi_Pb
	NTl = NTl + decaimento_Bi_Tl
	NBi1 = NBi1 - decaimento_Bi_Pb - decaimento_Bi_Tl



pl.plot(tpoints,Bi1points, label = "Bi 213")
pl.legend(loc='best')
pl.plot(tpoints,Tlpoints, label = "Tl 209")
pl.legend(loc='best')
pl.plot(tpoints,Pbpoints, label = "Pb 209")
pl.legend(loc='best')
pl.plot(tpoints,Bi2points, label = "Bi 209")
pl.legend(loc='best')
pl.title("Decaimento Radioativo")
pl.xlabel("Tempo (s)")
pl.ylabel("Nº de átomos")

pl.show()



















