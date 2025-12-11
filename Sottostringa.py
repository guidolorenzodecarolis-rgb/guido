#esercizio della sottostringa
s1 = input("inserisci la stringa: ")
s2 = input("inserisci la sottostringa: ")
conta_lettere = 0
conta = 0
uguaglianza = True
while conta_lettere < len(s1) and uguaglianza == True and len(s2) < len(s1):
    c2 = 0
    while c2 < len(s2):
        if(s2[c2] == s1[conta_lettere]):
            uguaglianza = True
        conta_lettere +=1
        c2 +=1
    if(c2 == len(s2)):
        conta +=1
        uguaglianza = False
if(conta != 0):
    print("la sottostringa è contenuta nella stringa")
else:
    print("la sottostringa non è contenuta nella stringa")