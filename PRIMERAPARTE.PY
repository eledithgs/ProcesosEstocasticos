#PRIMERA FORMA
#m = [[1,2,0],[3,4,0],[5,6,0]]
#for f in range(3): #recorre filas
#    for c in range(3): #recorre columnas
#        print (m[f][c],end='')
#    print()


#SEGUNDA FORMA
#a = [] #lista vacia
#m=3 #indice filas
#n=2 #indice columnas

#generar la matriz
#for f in range(m):
#    a.append([]) #en cada fila añade una lista
#    for c in range(n):
#        a[f].append(None) #añade celda
#        pass
#    pass

#imprimimos el contenido
#for f in range(m):
#    for c in range(n):
#        print(a[f][c], end='')
#        pass
#    print()
#    pass

#TERCERA FORMA
#from random import *
#fil= 3
#col=3
#a=[[randint(1 , 100) for i in range(fil)] for j in range(col)]
#for f in range(fil):
#    for c in range(col):
#        print(a[f][c], end='')
#    print()
#for f in a:
#       print(f)
#c = int(input('Digite columna a obterner'))
#b = []
#for f in range(len(a)):
#    b.append(a[f][c])
#print(b)


#datos = []
#for i in range(1,7):
#    nuevoDato = int( input( "Dime el dato numero {}: ".format(i) ))
#    datos.append(nuevoDato)
#print ("Los datos al reves son: ")
#for i in range(6,0,-1):
#    print ( datos[i-1] )
