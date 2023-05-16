from algo1 import *
from diccionary import *
from doublelinkedlist import *
from linkedlist import *
def existChar(stri, c):
    stri = String(stri)
    for n in range(len(stri)):
        if stri[n] == c:
            return True
    return False

def isPalindrome(stri):
    stri = String(stri)
    cont = 0
    striWithOutSpaces = String("")
    for i in range(len(stri)):
        if stri[i] != " ":
            striWithOutSpaces = concat(striWithOutSpaces,String(stri[i]))
    mid = len(striWithOutSpaces) // 2 
    for n in range(len(striWithOutSpaces)-1,mid,-1):
        if len(striWithOutSpaces) % 2 != 0:
            if n == mid:
                break
        if striWithOutSpaces[n] != striWithOutSpaces[cont]:
            return False
        cont = cont + 1
    return True

def mostRepeatedChar(stri):
    mostRepeated = ""
    cant = 0
    stri = String(stri) #Tomo la longitud mas larga
    D = Array(257,Diccionary())
    for n in range(len(stri)):
        dic_insert(D,ord(stri[n]),stri[n],ord(stri[n]))
    for i in range(len(D)):
        if D[i] != None:
            listlength = length(D[i])
            if listlength > cant:
                cant = listlength
                mostRepeated = D[i].head.value
    return mostRepeated



def stringCompresor(s):
    s = String(s)
    outstring = String("")
    contador = 1
    for n in range(len(s)):
        if n == len(s)-1:
            outstring = concat(outstring,String(s[n] + str(contador)))
        else:
            if s[n+1] == s[n]:
                contador = contador + 1
            else:
                outstring = concat(outstring,String(s[n] + str(contador)))
                contador = 1
    if len(outstring) > len(s):
        return s
    else:
        return outstring

def getBiggestIslandLen(s):
    s = String(s)
    outstring = String("")
    contador = 1
    maximo = 0
    for n in range(len(s)):
        if n == len(s)-1:
            outstring = concat(outstring,String(s[n] + str(contador)))
        else:
            if s[n+1] == s[n]:
                contador = contador + 1
            else:
                outstring = concat(outstring,String(s[n] + str(contador)))
                if contador > maximo:
                    maximo = contador
                contador = 1
    return maximo


#Ejercicio 5
def isAnagram(s,p):
    s = String(s) #Tomo la longitud mas larga
    p = String(p)
    if len(s) > len(p):
        size = len(s)
    else:
        size = len(p)
    if size % 2 == 0: #Evito que la longitud del hasttable sea par
        D = Array(size+1,Diccionary())
    else:
        D = Array(size,Diccionary())

    for n in range(len(s)): #Inserto ambos string letra por letra
        dic_insert(D,ord(s[n]),s[n],hashpermu(ord(s[n]),size))
    for i in range(len(p)):
        dic_insert(D,ord(p[i]),p[i],hashpermu(ord(p[i]),size))
    for j in range(size):  #Recorro el hastable y veo que todas las listas tengan longitud par
        if D[j] != None:
            if length(D[j]) % 2 != 0:
                return False
    return True #Si todas son pares, significa q es una permutacion

def hashpermu(k,size):
    return k % size


def verifyBalancedParentheses(stri):
    striOnlyParentheses = String("")
    for n in range(len(stri)):
        if stri[n] == "(" or stri[n] == ")":
            striOnlyParentheses = concat(striOnlyParentheses, String(stri[n]))
    DL = DoubleLinkedList()
    for i in range(len(striOnlyParentheses)-1,-1,-1):
        D_add(DL,striOnlyParentheses[i])
    currentnode = DL.tail
    while currentnode != None:
        if currentnode.value == "(":
            if currentnode.nextNode == None: #Hay uno abierto al final
                return False
            else:
                if currentnode.nextNode.value == ")":
                    if currentnode.previousNode != None:
                        currentnode = currentnode.previousNode
                        D_deleteNode(DL,currentnode.nextNode)
                        D_deleteNode(DL,currentnode.nextNode)
                        continue
                else:
                    return False
        currentnode = currentnode.previousNode
    return True
            
def reduceLen(stri):
    stri = String(stri)
    DL = DoubleLinkedList()
    for n in range(len(stri)-1,-1,-1):
        D_add(DL,stri[n])
    currentnode = DL.head
    while currentnode != None:
        if currentnode.nextNode != None:
            if currentnode.value == currentnode.nextNode.value:
                D_deleteNode(DL,currentnode.nextNode)
                D_deleteNode(DL,currentnode)
                currentnode = DL.head
                continue
        currentnode = currentnode.nextNode
    currentnode = DL.head
    strifinal = String("")
    while currentnode != None:
        strifinal = concat(strifinal,String(currentnode.value))
        currentnode = currentnode.nextNode
    return strifinal

#Retorna True si el stri2 esta contenido en el stri1
def isContained(stri1,stri2):
    cont = 0
    stri1 = String(stri1)
    stri2 = String(stri2)
    strifinal = String("")
    DL = DoubleLinkedList()
    for n in range(len(stri1)-1,-1,-1):
        D_add(DL,stri1[n])
    currentnode = DL.head
    while currentnode != None:
        if cont == len(stri2):
            break
        if currentnode.value == stri2[cont]:
            cont = cont + 1
            strifinal = concat(strifinal,String(currentnode.value))
        else:
            currentnode = currentnode.nextNode
            if currentnode.nextNode != None:
                D_deleteNode(DL,currentnode.previousNode)
            else:
                D_deleteNode(DL,currentnode)
                break
            continue
        currentnode = currentnode.nextNode
    if len(stri2) != len(strifinal):
        return False
    else:
        return strcmp(stri2,strifinal)

def isPatternContained(stri1,stri2,c):
    cont = 0
    stri1 = String(stri1)
    stri2 = String(stri2)
    strifinal = String("")
    DL = DoubleLinkedList()
    for n in range(len(stri1)-1,-1,-1):
        D_add(DL,stri1[n])
    currentnode = DL.head
    while currentnode != None:
        if cont == len(stri2):
            break
        if stri2[cont] == c:
            if currentnode.value == stri2[cont + 1]:
                cont = cont + 1
            else:
                currentnode = currentnode.nextNode
                D_deleteNode(DL,currentnode.previousNode)
            continue
        if currentnode.value == stri2[cont]:
            cont = cont + 1
            strifinal = concat(strifinal,String(currentnode.value))
        else:
            currentnode = currentnode.nextNode
            if currentnode.nextNode != None:
                D_deleteNode(DL,currentnode.previousNode)
            else:
                D_deleteNode(DL,currentnode)
                break
            continue
        currentnode = currentnode.nextNode
    cantComodines = 0
    for i in range(len(stri2)):
        if stri2[i] == c:
            cantComodines = cantComodines + 1
    striWithOutComodines = Array(len(stri2)-cantComodines,"")
    cont = 0
    for j in range(len(stri2)):
        if stri2[j] != c:
            striWithOutComodines[cont] = stri2[j]
            cont = cont + 1
    if len(striWithOutComodines) != len(strifinal):
        return False
    else:
        return strcmp(striWithOutComodines,strifinal)

def TransitionFunction(P,T):
    D = Array(128,Diccionary())

    for i in range(len(D)):
        D[i] = Diccionary()

    T = String(T)
    for i in range(len(T)):
        dic_insert(D,ord(T[i]),T[i],abs(ord(T[i]))%257)

    cont = 0
    for i in range(len(D)):
        if D[i].head != None:
            cont = cont + 1
    letters = Array(cont,"")
    cont = 0
    for i in range(len(D)):
        if D[i].head != None:
            letters[cont] = D[i].head.value
            cont = cont + 1
    
 
    TF = Array(len(P)+1,Array(cont,0))
    numberOfChars = cont
    lps = 0
    for x in range(numberOfChars):
        TF[0][x] = 0
    TF[0][indexer(0,letters,P)] = 1; 

    for k in range(1,len(P)):
        for y in range(numberOfChars):
            TF[k][y] = TF[lps][y]
        TF[k][indexer(k,letters,P)] = k + 1

        if(k < len(P)):
            lps = TF[lps][indexer(k,letters,P)]
    TF[len(P)] = letters
    return TF

def indexer(index,letters,P,):
    cont = 0
    for j in range(len(letters)):
        if P[index] == letters[j]:
            return cont
        else:
            cont = cont + 1

def AEFMatcher(T,P):
    TF = TransitionFunction(P,T)
    return finite_Automation_Matcher(T,TF,P)

def finite_Automation_Matcher(T,TF,P):
    P = String(P)
    T = String(T)
    M = len(P)
    N = len(T)
    q = 0
    for i in range(N):
        q = TF[q][indexer(i,TF[len(P)],T)]
        if q == M:
            A = Array(M,0)
            count = 0
            for j in range(i-M,i):
                A[count] = j + 1
                count = count + 1
            return A

def Imprimirmatriz(A):
    sizerows = len(A)
    sizecolumns = len(A[0])
    for i in range(sizerows):
        for j in range(sizecolumns):
            print(A[i][j],end=" ")
        print("")
    print("\n\n\n")
