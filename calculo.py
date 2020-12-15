from random import randrange, choice
import random

def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
def complemento(b):
    b=b+''
    n=len(b)
    for i in range(0,6-n):
        b='0'+b
    return b

#cruzar a y b son los padres, siendo ha y hb sus hijos, los retorna

def cruzar(a,b,r1,r2):
    #print(r1,r2,'         ******rangos cru a:',a,' b:',b)
    
    a=list(a)
    b=list(b)
    #print(b[r1:r2+1],"          ",a[r1:r2+1],r1,'/////',r2)
    aux=a[r1:r2+1]
    a[r1:r2+1]=b[r1:r2+1]
    b[r1:r2+1]=aux
    #print(b,"          ",a)
    #print(ha,hb,"           aaa")
    a=''.join(map(str,a))
    b=''.join(map(str,b))
    return a,b
#mutar
def mutar(a,x):
    #print(a,'   original')
    a=list(a)
    if a[x]==1:
        a[x]==0
    else:
        a[x]==1
    a=''.join(map(str,a))
    return a

#main
lista=[]

#ramdon de numeros
for i in range(30):
    lista.append(int(random.randrange(0, 30)))
print(lista,"\n")


#generaciones
for nro in range(20):
    
    print('\n Generacion: ',i+1,'\n')
    lista=sorted(lista,reverse=True)
    print('\n Lista ordenada\n',lista)
    
    evaluar=lista
    for i in range(len(evaluar)):
        evaluar[i]=evaluar[i]^3+evaluar[i]^2+evaluar[i]
    print('\nLista evaluada x^3+x^2+x\n',evaluar)
    #binario
    for i in range(len(lista)):
        lista[i]=binarizar(lista[i])
    print('\nBinarizar\n',lista)
    
    #complemento
    for i in range(len(lista)):
        lista[i]=complemento(lista[i])
    print('\nComplemento\n',lista)
    
    #cruzar
    r1=randrange(6)
    r2=randrange(6)
    while r1==r2:
        r1=randrange(6)
        r2=randrange(6)
    if r1>r2:
        f=r1
        r1=r2
        r2=f
    for i in range(int(len(lista)/2)):
        c1, c2=cruzar(lista[i*2], lista[(i*2)+1],r1,r2)
        lista[i*2]=c1
        lista[i*2+1]=c2
    print('\nCruzar\n',lista)
    
    #mutar
    x=randrange(6)
    
    for i in range(len(lista)):
        lista[i]=mutar(lista[i], x)
    
    print('\n Mutar\n',lista)
    
    #binario a decimal
    for i in range(len(lista)):
        lista[i]=int(lista[i], 2)
    
    print('\n Bin a Decimal\n',lista)
    