# Maggorenne o minorenne?
anno_di_nascita = int(input("inserisci il tuo anno di nascita:"))
anno_corrente = int(input("inserisci l'anno corrente:"))
operazione = anno_corrente - anno_di_nascita
if(operazione >= 18):
    print("l'utente è maggiorenne")
else:
    print("l'utente è minorenne")