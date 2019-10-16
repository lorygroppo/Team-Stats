f = open("ex.txt","r")
info = f.readline() #legge la prima riga contenente le informazioni della partita
fields = f.readline().strip().split(",") #prelevo i nomi dei campi dalla seconda riga
team = []
for line in f.readlines():
    print(line)
    value = line.strip().split(",")
    giocatore = {}
    for x in fields:
        giocatore[x] = 0
    if (len(value) == len(fields)):
        for i in range(len(value)):
            giocatore[fields[i]] = value[i]
        team.append(giocatore)
    else:
        print("ERRORE NEL NUMERO DI CAMPI")
print(team)
f.close()