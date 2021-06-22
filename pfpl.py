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

print()

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
        
pol=[]
cond=True
cont=1
print("R1:")
aux=[]
tp=["R1"]

for i in range(edo):
    aux.append(int(input("R1"+str(i)+":")))
pol.append(aux)
               
while cond:
    if input("Desea agregar otra politica [s/n]:")=="s":
        aux=[]
        for i in range(edo):
            aux.append(int(input("R"+str(cont)+str(i)+":")))
        pol.append(aux)
        cont+=1
        tp.append("R"+str(cont))
    else:
        cond=False
print(tabulate(pol, headers=hder, showindex=tp,tablefmt='fancy_grid'))

pr=[]
for i in range(cont):
    pr.append([])
for i in range(cont):
    cc=0
    for j in pol[i]:
        pr[i].append(matriz[j-1][mrd[j-1].index(cc)])
        cc+=1
        
for i in range(len(pol)):
     print("PR"+str(i+1))
     print(tabulate(pr[i], headers=hder, showindex=hder, tablefmt='fancy_grid'))

pi=[]

irm=[]
for i in range(edo):
    icdp=[]
    for j in range(edo):
        if i!=edo-1:
            if i==j:
                icdp.append(-1)
            else:
                icdp.append(0)
        else:
            icdp.append(0)
    irm.append(icdp)
irm=np.array(irm)

for i in pr:
    bm=np.transpose(i)
    aux=[]
    for j in range(edo-1):
        aux.append(bm[j])
    metallica=[]
    for k in range(edo):
        metallica.append(1)
    aux.append(metallica)
    aux=np.array(aux)
    pi.append(aux+irm)

b=[]
for i in range(edo-1):
    b.append(0)
b.append(1)


encpi=[]
for i in range(edo):
    encpi.append(unicodedata.lookup("GREEK SMALL LETTER PI")+str(i))

fr7=[]
for i in pi:
    fr8=np.linalg.solve(i,b)
    aux=[fr8.tolist()]
    fr7.append(aux)

for i in range(len(fr7)):
    print(tabulate(fr7[i], headers=encpi, tablefmt='fancy_grid'))

e=0
es=[]
for i in range(len(pol)):
    for j in range(edo):
        e=e+costo[pol[i][j]-1][j]*fr7[i][0][j]
    es.append(e)

print("MAX:"+str(max(es)))
print("min:"+str(min(es)))
    
    












