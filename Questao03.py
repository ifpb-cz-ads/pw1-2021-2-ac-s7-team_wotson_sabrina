ListaI=[]
ListaII=[]
ListaIII=[]
x=0
y=0
count=0
aux=[]

for x in range(5):
	ListaI.append(int(input("Informe um numero, por gentileza %d:" % x)))
x=0
for x in range(5):
	ListaII.append(int(input("Informe um numero, por gentileza %d:" % x)))
x=0

for x in range(5):
    aux.append(ListaI[x])
    aux.append(ListaII[x])

x=0
ListaIII=list(set(aux))

print(ListaIII)