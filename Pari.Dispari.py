# scrivere un programma che chiede in ingresso un numero naturale e stampa se è pari o dispari
numero = int(input("inserisci un numero Naturale:"))
resto = numero%2
if(resto == 0):
    print("il numero è pari")
else:
    print("il numero è dispari")