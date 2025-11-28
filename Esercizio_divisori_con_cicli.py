#esercizio divisori
numero = int(input("inserisci il numweo: "))
divisore = 2
while divisore < numero // 2 or divisore == numero // 2:
    if(numero%divisore==0):
        print(divisore)
    divisore += 1
print(numero)