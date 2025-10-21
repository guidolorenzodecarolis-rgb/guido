# esercizio 1 sulla selezione
n1 = input("inserisci un numero:")
n2 = input("inserisci un numero:")
n3 = input("inserisci un numero:")
if (n1>n2>n3):
    print(n1)
    print(n2)
    print(n3)
else:
    if (n1<n2>n3>n1):
        print(n2)
        print(n3)
        print(n1)
    if (n1<n2>n3<n1):
        print(n2)
        print(n1)
        print(n3)
    if (n1>n2<n3>n1):
        print(n3)
        print(n1)
        print(n2)
    if (n3>n2>n1):
        print(n3)
        print(n2)
        print(n1)