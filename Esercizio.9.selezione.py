#Esercizio 9 della selezione
n1 = input("inserisci il primo nome:")
n2 = input("inserisci il secondo nome:")
l1 = len(n1)
l2 = len(n2)
d1 = l1//2
d2 = l2//2
r1 = l1%2
r2 = l2%2
if(r1==0) and (r2==0):
    n3 = n1[:d1] + n2[d2:]
    print(n3)
else:
    if(r1!=0) and (r2==0):
        n4 = n1[:d1+1] + n2[d2:]
        print(n4)
    if(r1==0) and (r2!=0):
        n5 = n1[:d1] + n2[d2:]
        print(n5)