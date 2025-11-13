#Esercizio 8 selezione
nome = input("inserisci il nome:")
l = len(nome)
d = l//2
r = l%2
if(r==0):
    n1 = nome[:d-1]
    n2 = nome[d+1:]
    if(n1==n2):
        print("la prima e l'ultima lettera sono uguali")
    else:
        print("la prima e l'ultima lettera non sono uguali")
else:
    n3 = nome[:d-1]
    n4 = nome[d+2:]
    if(n3==n4):
        print("la prima e l'ultima lettera sono uguali")
    else:
        print("la prima e l'ultima lettera non sono uguali")