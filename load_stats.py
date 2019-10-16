# Funzione 'LoadStats(fileToRead)':
# permette di prelevare i dati da un file di testo appositamente formattato.
# Il risultato di questa funzione è un dizionario contenente alcune info generali
# di una specifica partita e una serie di campi denominati come i nomi dei giocatori,
# aventi come valore un altro dizionario, contente tutte le statistiche.
# Un prototipo di tale struttura è il seguente
# match = {
#     data : gg/mm/aaaa,
#     partita : team A vs team B, ...
#     ROSSI : {
#         pt : 12,
#         ast: 2, ...
#     },
#     VERDI : {
#         pt: 7,
#         ast: 4, ...
#     }
# }
def LoadStats(fileToRead):
    try: f = open(fileToRead,"r")
    except:
        print("ERRORE. Impossibile aprire il file: "+fileToRead)
        return
    info = f.readline().strip().split(",") #legge la prima riga contenente le informazioni della partita
    match = {
        "INFO" : {
            "PARTITA" : info[0],
            "DATA" : info[3],
            "CAMPIONATO" : info[1],
            "STAGIONE" : info[2]
        }
    }
    fields = f.readline().strip().split(",") #prelevo i nomi dei campi dalla seconda riga

    #leggo righe restanti, relative ad ogni giocatore
    for line in f.readlines():
        value = line.strip().split(",")
        giocatore = {}
        for x in fields:
            giocatore[x] = 0
        if (len(value) == len(fields)):
            for i in range(len(value)):
                giocatore[fields[i]] = value[i]
            try: 
                giocatore.pop("NOME")
                nome = value[fields.index("NOME")]
                match[nome] = giocatore
            except:
                print("ERRORE: campo NOME non corretto")
                return
        else:
            print("ERRORE NEL NUMERO DI CAMPI")
            return
    f.close()
    return match