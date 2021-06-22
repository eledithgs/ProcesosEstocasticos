import numpy as np
import math
import os
from sympy import *
from tabulate import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import simpledialog
import unicodedata
import scipy
from scipy.optimize import linprog

def limp():
    tex2.delete(0, END)
    tex3.delete(0, END)
    tex4.delete(0, END)
    tex6.delete(0, END)
    tex8.delete(0, END)
    tex9.delete(1.0, END)
    return

def nopal():
    tex9.delete(1.0, END)
    edo=int(lasdelaintuicion.get())
    dec=int(loba.get())
    r=[]
    if combo.get()=='Mejoramiento de Politicas con Descuento' or combo.get()=='Aproximaciones Sucesivas':
        alpha=float(estoyaqui.get())
    if combo.get()=='Aproximaciones Sucesivas':
        ciegasordomuda=int(diadeenero.get())
    if combo.get()=='Mejoramiento de Politicas con Descuento' or combo.get()== 'Mejoramiento de Politicas':
        ochoa=antologia.get()
        alaba=ochoa.split(",")
        for i in alaba:
            r.append(int(i))
    caras=dec
    mrd=[]

    hder=[]
    for i in range(edo):
        hder.append(i)
    
    for i in range(dec):
        amr=[]
        for j in range(edo):
            if simpledialog.askstring(title = "Decision valida", prompt = 'La Decision {} aplica en el Estado {} [s/n]:'.format(i+1, j))=="s":
                amr.append(j)
        mrd.append(amr)
    
    matriz = []

    for k in range(caras):
        matriz.append([])
        for i in range(len(mrd[k])):
            matriz[k].append([])
            for j in range (edo):
                valora = simpledialog.askstring(title = "Decision k="+str(k+1), prompt = 'Estado {}, Estado {}:'.format(mrd[k][i], j))
                valor = float(valora)
                matriz[k][i].append(valor)
    print()
    
    for k in range(caras):
        tex9.insert(INSERT,"K="+str(k+1)+"\n")
        tex9.insert(INSERT,tabulate(matriz[k], headers=hder, showindex=mrd[k],tablefmt='fancy_grid')+"\n")
    
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
        #print('Decision k=',k+1)
        for i in range(len(mrd[k])):
            valora = simpledialog.askstring(title = "Costo", prompt = 'C {} {}:'.format(mrd[k][i], k+1))
            valor = float(valora)
            costo[k][mrd[k][i]]=valor
    
    print()
    for k in range(caras):
        tex9.insert(INSERT,'Decision k='+str(k+1)+"\n")
        for i in range(len(mrd[k])):
            tex9.insert(INSERT,"C"+str(mrd[k][i])+str(k+1)+"="+str(costo[k][mrd[k][i]])+"\n")

    ##############################################################################################################################################33
    if combo.get()=='Enumeracion Exhaustiva':
        pol=[]
        cond=True
        cont=1
        tex9.insert(INSERT,"R1:\n")
        aux=[]
        tp=["R1"]
        
        for i in range(edo):
            aux.append(int(simpledialog.askstring(title = "Politica", prompt = "R1"+str(i)+":")))
        pol.append(aux)
               
        while cond:
            if simpledialog.askstring(title = "Politica", prompt = "Desea agregar otra politica [s/n]:")=="s":
                aux=[]
                for i in range(edo):
                    aux.append(int(simpledialog.askstring(title = "Politica", prompt ="R"+str(cont)+str(i)+":")))
                pol.append(aux)
                cont+=1
                tp.append("R"+str(cont))
            else:
                cond=False
        tex9.insert(INSERT,tabulate(pol, headers=hder, showindex=tp,tablefmt='fancy_grid')+"\n")
        
        pr=[]
        for i in range(cont):
            pr.append([])
        for i in range(cont):
            cc=0
            for j in pol[i]:
                pr[i].append(matriz[j-1][mrd[j-1].index(cc)])
                cc+=1
        for i in range(len(pol)):
            tex9.insert(INSERT,"PR"+str(i+1)+"\n")
            tex9.insert(INSERT,tabulate(pr[i], headers=hder, showindex=hder, tablefmt='fancy_grid')+"\n")
            
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
            tex9.insert(INSERT,tabulate(fr7[i], headers=encpi, tablefmt='fancy_grid')+"\n")
        
        e=0
        es=[]
        for i in range(len(pol)):
            for j in range(edo):
                e=e+costo[pol[i][j]-1][j]*fr7[i][0][j]
            es.append(e)
            e=0
        
        tex9.insert(INSERT,"MAX:"+str(pol[es.index(max(es))])+"\n")
        tex9.insert(INSERT,"min:"+str(pol[es.index(min(es))])+"\n")
    #######################################################################################################################################
    if combo.get()=='Programacion lineal':
        c=[]
        enc=[]
        
        opera=simpledialog.askstring(title = "Operacion", prompt="Que Desea hacer [Max/Min]:")
        for i in range(edo):
            for k in range(dec):
                if i in mrd[k]:
                    if opera=="Min":
                        c.append(costo[k][i])
                    else:
                        c.append(-1*costo[k][i])
                    enc.append("y"+str(i)+str(k+1))
        
        auxi=[c]
        tex9.insert(INSERT,"Z\n")
        tex9.insert(INSERT,tabulate(auxi, headers=enc,tablefmt='fancy_grid')+"\n")
        
        a=[]
        aux=[]
        for i in range(len(c)):
            aux.append(1)
        a.append(aux)
        
        aux=[]
        for j in range(edo-1):
            aux=[]
            for i in range(edo):
                for k in range(dec):
                    if i in mrd[k] and i==j:
                        aux.append(-1*matriz[k][i][j]+1)
                    elif i in mrd[k]:
                        aux.append(-1*matriz[k][i][j])
            auxi=[aux]
            tex9.insert(INSERT,tabulate(auxi, headers=enc,tablefmt='fancy_grid')+"\n")
            a.append(aux)
        
        ld=[1]
        for i in range(edo-1):
            ld.append(0)
        res = linprog(c, A_eq=a, b_eq=ld,method='revised simplex')
        auxi=[res.x]
        tex9.insert(INSERT,tabulate(auxi, headers=enc,tablefmt='fancy_grid')+"\n")
        
        mfs=[]
        for i in range(edo):
            mfs.append([])
            for j in range(dec):
                mfs[i].append(0)
                
        tex9.insert(INSERT,str(mfs)+"\n")
        
        j=0
        for k in range(edo):
            for i in range(dec):
                if k in mrd[i]:
                    mfs[k][i]=res.x[j]
                    j=j+1
        
        for k in range(edo):
            for i in range(dec):
                if k in mrd[i]:
                    tex9.insert(INSERT,"D"+str(k)+str(i+1)+" = "+str(mfs[k][i]/sum(mfs[k]))+"\n")
        
        for k in range(edo):
            for i in range(dec):
                if k in mrd[i]:
                    mfs[k][i]=mfs[k][i]/sum(mfs[k])
        
        optmeishon=[]
        
        for k in range(edo):
            for i in range(dec):
                if mfs[k][i]==1:
                    optmeishon.append(i+1)
        
        tex9.insert(INSERT,"Politica optima: "+str(optmeishon)+"\n")
    ######################################################################################################################################################    
    if combo.get()=='Mejoramiento de Politicas':
        tex9.insert(INSERT,"\nR0:\n")
        tex9.insert(INSERT,tabulate([r],tablefmt='fancy_grid')+"\n")
        
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
        
        tex9.insert(INSERT,tabulate([sol],headers=encr,tablefmt='fancy_grid')+"\n")
        
        mrf=[]
        dimitrescu=[]
        for i in range(edo):
            mrf.append([])
            dimitrescu.append([])
            tex9.insert(INSERT,"i="+str(i)+"\n")
            for j in range(len(mrd)):
                if i in mrd[j]:
                    tex9.insert(INSERT,"k="+str(j+1)+"\n")
                    pm=costo[j][i]
                    for k in range(len(sol)-1):
                        pm=pm+sol[k+1]*matriz[j][i][k]
                    if i<edo-1:
                        pm=pm-sol[i+1]
                    tex9.insert(INSERT,str(pm)+"\n")
                    mrf[i].append(pm)
                    dimitrescu[i].append(j)
        
        soldef=[]
        heisenberg=simpledialog.askstring(title = "Operacion", prompt="Que Desea hacer [Max/Min]:")
        cont=0
        for i in mrf:
            if heisenberg=="Min":
                soldef.append(dimitrescu[cont][i.index(min(i))]+1)
            else:
                soldef.append(dimitrescu[cont][i.index(max(i))]+1)
            cont+=1
        tex9.insert(INSERT,"Politica optima:\n")
        tex9.insert(INSERT,str(soldef)+"\n")
##########################################################################################
    if combo.get()=='Mejoramiento de Politicas con Descuento':
        b=[]
        for i in range(edo):
            b.append(costo[r[i]-1][i])
        b=np.array(b)
        j=0
        a=[]
        for k in r:
            a.append([])
            for i in range(edo):
                a[j].append(-1*alpha*matriz[k-1][j][i])
            j+=1
        ajaxamsterdam=[]
        for i in range(edo):
            ajaxamsterdam.append([])
            for j in range(edo):
                if j==i:
                    ajaxamsterdam[i].append(1)
                else:
                    ajaxamsterdam[i].append(0)
        ajaxamsterdam=np.array(ajaxamsterdam)
        a=np.array(a)
        a=a+ajaxamsterdam
        sol=np.linalg.solve(a,b)
        encr=[]
        for i in range(edo):
            encr.append("V"+str(i))
        
        tex9.insert(INSERT,tabulate([sol],headers=encr,tablefmt='fancy_grid')+"\n")
        
        mrf=[]
        dimitrescu=[]
        for i in range(edo):
            mrf.append([])
            dimitrescu.append([])
            tex9.insert(INSERT,"i="+str(i)+"\n")
            for j in range(len(mrd)):
                if i in mrd[j]:
                    tex9.insert(INSERT,"k="+str(j+1)+"\n")
                    pm=costo[j][i]
                    for k in range(len(sol)):
                        pm=pm+alpha*sol[k]*matriz[j][i][k]
                    tex9.insert(INSERT,str(pm)+"\n")
                    mrf[i].append(pm)
                    dimitrescu[i].append(j)
        
        soldef=[]
        heisenberg=simpledialog.askstring(title = "Operacion", prompt="Que Desea hacer [Max/Min]:")
        cont=0
        for i in mrf:
            if heisenberg=="Min":
                soldef.append(dimitrescu[cont][i.index(min(i))]+1)
            else:
                soldef.append(dimitrescu[cont][i.index(max(i))]+1)
            cont+=1
        tex9.insert(INSERT,"Politica optima:\n")
        tex9.insert(INSERT,soldef)
############################33333#####################################################
    if combo.get()=='Aproximaciones Sucesivas':
        v=[]
        v.append([])
        sm=[]
        db=[]
        ld=[]
        vp=[]
        vp.append([])
        sm.append([])
        db.append([])
        
        
        tex9.insert(INSERT,"n=1\n")
        for i in range(edo):
            sm[0].append([])
            db[0].append([])
            for j in range(len(mrd)):
                if i in mrd[j]:
                    sm[0][i].append(costo[j][i])
                    db[0][i].append(j+1)
        for i in range(len(sm[0])):
            tex9.insert(INSERT,"v"+str(i)+"1=min"+str(sm[0][i])+"\n")
                       
        for k in range(len(sm[0])):
            v[0].append(db[0][k][sm[0][k].index(min(sm[0][k]))])
            vp[0].append(sm[0][k][sm[0][k].index(min(sm[0][k]))])
        tex9.insert(INSERT,"Aproximaciona la politica optima R1: "+str(v[0])+"\n")
        
        for skysports in range(1,ciegasordomuda):
            tex9.insert(INSERT,"\n")
            tex9.insert(INSERT,"n="+str(skysports+1)+"\n")
            sm.append([])
            db.append([])
            for i in range(edo):
                sm[skysports].append([])
                db[skysports].append([])
                for j in range(dec):
                    if i in mrd[j]:
                        aguilar=costo[j][i]
                        for cocaine in range(edo):
                            aguilar+=alpha*matriz[j][i][cocaine]*vp[skysports-1][cocaine]
                        sm[skysports][i].append(aguilar)
                        db[skysports][i].append(j+1)
            
            for i in range(len(sm[skysports])):
                tex9.insert(INSERT,"v"+str(i)+str(skysports+1)+"=min"+str(sm[skysports][i])+"\n")
                
            v.append([])
            vp.append([])
            for k in range(len(sm[skysports])):
                v[skysports].append(db[skysports][k][sm[skysports][k].index(min(sm[skysports][k]))])
                vp[skysports].append(sm[skysports][k][sm[skysports][k].index(min(sm[skysports][k]))])
            tex9.insert(INSERT,"Aproximaciona la politica optima R"+str(skysports+1)+": "+str(v[skysports]))
        
    
    
    
    
raiz= Tk()#ventana raiz
menu1=Menu(raiz)
raiz.config(bg="#002B7A")
raiz.title("Metodo Simplex")
raiz.geometry("800x550")
frm= Frame()#widgeth
frm.pack(expand="True")
frm.config(width="750", height="500")
frm.config(width="750", height="500",bg="#D59F0F")

lasdelaintuicion = StringVar()
loba = StringVar()
antologia = StringVar()
estoyaqui = StringVar()
diadeenero = StringVar()

combo=ttk.Combobox(frm)
combo.place(x=50,y=200)
combo['values']=['Enumeracion Exhaustiva','Programacion lineal','Mejoramiento de Politicas','Mejoramiento de Politicas con Descuento','Aproximaciones Sucesivas']
combo.current(0)



inf1=Label(frm, text="Metodo: ",bg="#D59F0F")#etiqueta
inf1.grid(row=0, column=0, padx=10, pady=10)#posicion de la etiqueta
combo.grid(row=0, column=1, padx=10, pady=10)

inf2=Label(frm, text="Estados: ",bg="#D59F0F")#etiqueta
inf2.grid(row=1, column=0, padx=5, pady=5)#posicion de la etiqueta

tex2=Entry(frm, textvariable=lasdelaintuicion, width=10)#campo de texto
tex2.grid(row=1, column=1, padx=5, pady=5)#posicion del campo de texto

inf3=Label(frm, text="Decisiones: ",bg="#D59F0F")#etiqueta
inf3.grid(row=2, column=0, padx=5, pady=5)#posicion de la etiqueta

tex3=Entry(frm, textvariable=loba, width=10)#campo de texto
tex3.grid(row=2, column=1, padx=5, pady=5)#posicion del campo de texto

inf4=Label(frm, text="Politica de inicio: ",bg="#D59F0F")#etiqueta
inf4.grid(row=3, column=0, padx=5, pady=5)#posicion de la etiqueta

tex4=Entry(frm, textvariable=antologia, width=50)#campo de texto
tex4.grid(row=3, column=1, padx=5, pady=5)#posicion del campo de texto

inf5=Label(frm, text="Descuento: ",bg="#D59F0F")#etiqueta
inf5.grid(row=4, column=0, padx=5, pady=5)#posicion de la etiqueta

tex6=Entry(frm, textvariable=estoyaqui, width=10)#campo de texto
tex6.grid(row=4, column=1, padx=5, pady=5)#posicion del campo de texto

inf7=Label(frm, text="N ",bg="#D59F0F")#etiqueta
inf7.grid(row=5, column=0, padx=5, pady=5)#posicion de la etiqueta

tex8=Entry(frm, textvariable=diadeenero, width=10)#campo de texto
tex8.grid(row=5, column=1, padx=5, pady=5)#posicion del campo de texto

inf3c=Label(frm, text="Resultados: ",bg="#D59F0F")#etiqueta
inf3c.grid(row=6, column=0, padx=10, pady=10)#posicion de la etiqueta
tex9=Text(frm, width=50, height=12,wrap = NONE)#campo de texto
tex9.grid(row=6, column=1, padx=10, pady=10)

barrapabajar=Scrollbar(frm,command=tex9.yview)
tex9.config(yscrollcommand=barrapabajar.set)
barrapabajar.grid(row=6,column=2,sticky="nsew")

barrapaladerecha=Scrollbar(frm,command=tex9.xview,orient='horizontal')
tex9.config(xscrollcommand=barrapaladerecha.set)
barrapaladerecha.grid(row=7,column=1,sticky="nsew")

btnp=Button(frm, text="Aceptar", command=nopal)#Boton
btnp.grid(row=8,column=1)

btnp2=Button(frm, text="Limpiar", command=limp)#Boton
btnp2.grid(row=8,column=0)
raiz.mainloop()
