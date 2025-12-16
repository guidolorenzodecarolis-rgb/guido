#esercizio divisori
numero = int(input("inserisci il numero: "))
divisore = 1
while divisore < numero // 2 or divisore == numero // 2:
    if(numero%divisore==0):
        print(divisore)
    divisore += 1
print(numero)