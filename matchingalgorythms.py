from linkedlist import *
from algo1 import *

def Rabin_Karp(T,P):
    T = String(T)
    P = String(P)
    n = len(T)
    m = len(P)
    h = (128**(m-1))
    hashpattern = hashRK(P)
    tInit = hashRK(substr(T,0,m))
    ts = tInit
    for s in range(n-m):
        tExtract = substr(T,s,s+m)
        if hashpattern == ts:
            if strcmp(tExtract,P):
                return True
        if s < n-m:
            ts = (ts - (ord(T[s])*h))*128+ord(T[s+m])
    return False
    
def hashRK(p):
    hashpattern = 0
    size = len(p)
    cont = 0
    for i in range(size-1,-1,-1):
        hashpattern = hashpattern + (128**i)*ord(p[cont])
        cont = cont + 1
    return hashpattern

#Ejercicio 14
def Compute_Prefix(P):
    P = String(P)
    size = len(P)
    pi = Array(size,0)
    pi[0] = 0
    k = 0
    for q in range(1,size):
        while k>0 and P[k] != P[q]:
            k = pi[k]
        if P[k] == P[q]:
            k = k + 1
        pi[q] = k
    return pi

def KMPMatcher(T,P):
    T = String(T)
    P = String(P)
    n = len(T)
    m = len(P)
    pi = Compute_Prefix(P)
    q = 0
    for i in range(1,n):
        while q > 0 and P[q] != T[i]:
            q = pi[q-1]
        if P[q] == T[i]:
            q = q + 1
        if q == m:
            A = Array(m,0)
            count = 0
            for j in range(i-m,i):
                A[count] = j + 1
                count = count + 1
            return A

def KMPMatcherSinSolap(T,P):
    T = String(T)
    P = String(P)
    n = len(T)
    m = len(P)
    pi = Compute_Prefix(P)
    q = 0
    L = LinkedList()
    for i in range(1,n):
        while q > 0 and P[q] != T[i]:
            q = pi[q-1]
        if P[q] == T[i]:
            q = q + 1
        if q == m:
            q = pi[q-1]
            
            for j in range(i-m,i):
                add(L,j + 1) 
    size = length(L)
    A = Array(size,0)
    currentnode = L.head
    while currentnode != None:
        A[size-1] = currentnode.value
        size = size -1
        currentnode = currentnode.nextNode
    return A