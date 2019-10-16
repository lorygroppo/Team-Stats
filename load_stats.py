f = open("ex.txt","r")
info = f.readline() #legge la prima riga contenente le informazioni della partita
fields = f.readline().strip().split(",") #prelevo i nomi dei campi dalla seconda riga
team = {}

#leggo righe restanti, relative ad ogni giocatore
for line in f.readlines():
    print(line)
    value = line.strip().split(",")
    giocatore = {}
    for x in fields:
        giocatore[x] = 0
    if (len(value) == len(fields)):
        for i in range(len(value)):
            giocatore[fields[i]] = value[i]
        try giocatore.pop("NOME")
        else:
            print "ERRORE: campo NOME non corretto"
        print(giocatore)
    else:
        print("ERRORE NEL NUMERO DI CAMPI")
print(team)
f.close()