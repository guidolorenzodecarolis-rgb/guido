# nome ed età
nome = input("inserisci il tuo nome:")
età = int(input("inserisci la tua erà:"))
if(età % 3 == 0) and (età % 2 != 0):
    n1 = nome[:2] + nome[-2:]
    print(n1)
else:
    n2 = nome[2:-2]
    print(n2)