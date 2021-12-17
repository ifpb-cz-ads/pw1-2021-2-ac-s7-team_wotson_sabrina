ListaI=[]
ListaII=[]
ListaIII=[]
x=0

for x in range(5):
	ListaI.append(int(input("Informe um numero, por gentileza %d:" % x)))
x=0
for x in range(5):
	ListaII.append(int(input("Informe um numero, por gentileza %d:" % x)))
x=0

for x in range(5):
    ListaIII.append(ListaI[x])
x=0

for x in range(5):
    ListaIII.append(ListaII[x])

print(ListaIII)