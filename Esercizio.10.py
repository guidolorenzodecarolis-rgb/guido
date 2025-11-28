#Esercizio 10 selezione
nome1 = input("inserisci il primo nome:")
numero1 = int(input("inserisci il primo numero:"))
nome2 = input("inserisci il secondo nome:")
numero2 = int(input("inserisci il secondo numero:"))
l1 = len(nome1)
l2 = len(nome2)
if(l1>numero1) and (l1>0) and (l2>0) and (l2>numero2) and (l1>numero2) and (l2>numero1):
    nome3 = nome1[:numero1] + nome2[numero1-1:numero2-1] + nome1[numero2:]
    print(nome3)
else:
    print("errore, controlla che le variabili possano soddisfare le richieste sopra elencate")