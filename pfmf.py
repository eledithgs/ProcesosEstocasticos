from tabulate import tabulate
import numpy as np
import unicodedata

print('Ingrese sus datos')
edo = int(input('¿Cuantos estados tiene?: '))

hder=[]
for i in range(edo):
    hder.append(i)
    
dec = int(input('¿Cuantas decisiones?: '))
caras = dec
print('Estados: ',edo,'Decisiones: ',dec)
mrd=[]

for i in range(dec):
    amr=[]
    for j in range(edo):
        if input('La Decision {} aplica en el Estado {} [s/n]:'.format(i+1, j))=="s":
            amr.append(j)
    mrd.append(amr)

matriz = []

for k in range(caras):
    print('Decision k=',k+1)

    matriz.append([])
    for i in range(len(mrd[k])):
        matriz[k].append([])
        for j in range (edo):
            valor = float(input('Estado {}, Estado {}:'.format(mrd[k][i], j)))
            matriz[k][i].append(valor)
print()

for k in range(caras):
    print("K="+str(k+1))
    print(tabulate(matriz[k], headers=hder, showindex=mrd[k],tablefmt='fancy_grid'))

juarez=[]
for i in range(edo):
    juarez.append(0)

axm=[]
for k in range(caras):
    axm.append([])
    for i in range(edo):
        if i in mrd[k]:
            axm[k].append(matriz[k].pop(0))
        else:
            axm[k].append(juarez)
matriz=axm

costo=[]

for i in range(caras):
    aux=[]
    for j in range(edo):
        aux.append(0)
    costo.append(aux)

for k in range(caras):
    print('Decision k=',k+1)
    for i in range(len(mrd[k])):
        valor = float(input('C {} {}:'.format(mrd[k][i], k+1)))
        costo[k][mrd[k][i]]=valor

print()
for k in range(caras):
    print('Decision k=',k+1)
    for i in range(len(mrd[k])):
        print("C"+str(mrd[k][i])+str(k)+"="+str(costo[k][mrd[k][i]]))

r=[]

print("Politica de inicio")
for i in range(edo):
    r.append(int(input("R"+str(i)+":")))

print("\nR0:")
print(tabulate([r],tablefmt='fancy_grid'))

b=[]
for i in range(edo):
    b.append(costo[r[i]-1][i])
b=np.array(b)
j=0
a=[]
for k in r:
    a.append([])
    a[j].append(1)
    for i in range(edo-1):
        a[j].append(-1*matriz[k-1][j][i])
    j+=1
ajaxamsterdam=[]
for i in range(edo):
    ajaxamsterdam.append([])
    for j in range(edo):
        if j==i+1:
            ajaxamsterdam[i].append(1)
        else:
            ajaxamsterdam[i].append(0)
ajaxamsterdam=np.array(ajaxamsterdam)
a=np.array(a)
a=a+ajaxamsterdam
sol=np.linalg.solve(a,b)
encr=["g(R)"]
for i in range(edo-1):
    encr.append("V"+str(i))

print(tabulate([sol],headers=encr,tablefmt='fancy_grid'))

mrf=[]
dimitrescu=[]
for i in range(edo):
    mrf.append([])
    dimitrescu.append([])
    print("i="+str(i))
    for j in range(len(mrd)):
        if i in mrd[j]:
            print("k="+str(j+1))
            pm=costo[j][i]
            for k in range(len(sol)-1):
                pm=pm+sol[k+1]*matriz[j][i][k]
            if i<edo-1:
                pm=pm-sol[i+1]
            print(pm)
            mrf[i].append(pm)
            dimitrescu[i].append(j)

soldef=[]
heisenberg=input("Que Desea hacer [Max/Min]:")
cont=0
for i in mrf:
    if heisenberg=="Min":
        soldef.append(dimitrescu[cont][i.index(min(i))]+1)
    else:
        soldef.append(dimitrescu[cont][i.index(max(i))]+1)
    cont+=1
print("Politica optima:")
print(soldef)


    

    

