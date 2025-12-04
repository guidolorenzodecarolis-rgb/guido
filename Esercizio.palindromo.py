#esercizio palindromo
nome = input("inserisci il nome: ")
conta_lettere = 0
palindromo = True
while conta_lettere < len(nome)//2 and palindromo == True:
    conta_lettere +=1
    lettera1 = nome[conta_lettere]
    lettera2 = nome[-conta_lettere-1]
    if(lettera1 != lettera2):
        palindromo = False
    else:
        palindromo = True
print(palindromo)