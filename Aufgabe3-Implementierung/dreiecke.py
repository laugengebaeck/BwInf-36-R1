#############################################Funktionen#################################################################

#berechnet den Schnittpunkt der a-ten und b-ten Gerade der Liste Strecken; gibt Liste des Formats [Schnittpunkt existiert, x-Koordinate, y-Koordinate] aus
def Schnittpunkt(strecken, a, b):
    x = 0
#   Überprüfung ob eine der beiden Geraden parallel zur y-Achse ist (es gibt keine Funktionsgleichungen in diesem Fall, deswegen muss anders gerechnet werden)
    if Var(strecken[a])[0] == Var(strecken[a])[2]:
#       Überprüfung ob beide Strecken parallel zur y-Achse sind (parallele Geraden können keinen einzelnen Schnittpunkt haben)
        if Var(strecken[b])[0] == Var(strecken[b])[2]:
            return [False]
#       Berechnung des Schnittpunkts und Überprüfung auf dessen Existenz
        SPabx = round(Var(strecken[a])[0],2)
        SPaby = round((Funktion(strecken[b])[0] * SPabx) + Funktion(strecken[b])[1],2)
        if limit(strecken[a], strecken[b], SPabx, SPaby):
            return [True, str(SPabx), str(SPaby)]
        else:
            return [False]
    elif Var(strecken[b])[0] == Var(strecken[b])[2]:
        SPabx = round(Var(strecken[b])[0],2)
        SPaby = round((Funktion(strecken[a])[0] * SPabx) + Funktion(strecken[a])[1],2)
        if limit(strecken[a], strecken[b], SPabx, SPaby):
            return [True, str(SPabx), str(SPaby)]
        else:
            return [False]
    else:       # Überprüfung ob beide Strecken parallel zueinander sind (parallele Geraden können keinen einzelnen Schnittpunkt haben)
        if Funktion(strecken[b])[0] == Funktion(strecken[a])[0]:
            return [False]
#       normale Berechnung des Schnittpunkts sowie Überprüfung auf dessen Existenz
        else:
            SPabx = round((Funktion(strecken[a])[1] - Funktion(strecken[b])[1]) / (Funktion(strecken[b])[0] - Funktion(strecken[a])[0]),2)
            SPaby = round((Funktion(strecken[a])[0] * SPabx) + Funktion(strecken[a])[1],2)
            if limit(strecken[a], strecken[b], SPabx, SPaby):
                return [True, str(SPabx), str(SPaby)]
            else:
                return [False]

#aus den Punkten einer Strecke Funktionsgleichung berechnen; Ausgabe in Form [m, n] (y=mx+n)
def Funktion(strecke):
    ret = [(Var(strecke)[3] - Var(strecke)[1])/(Var(strecke)[2] - Var(strecke)[0])]
    ret = ret + [Var(strecke)[1] - (Var(strecke)[0] * ret[0])]
    return ret

#aus den in einem String vorliegenden Punkten eine Liste mit 4 Koordinaten (Float) erstellen; Ausgabe in der Form [x1, y1, x2, y2]
def Var(strecke):
    var = []
    x = 0
#   sucht nach dem Punkt in den Koordinaten und wandelt die Zahl mit 6 Nachkommastellen in einen Float um
    for a in range(0, len(strecke)):
        if strecke[a] == '.':
            var = var + [float(strecke[x:(a+7)])]
            x = a + 7
    return var

#Test ob der Schnittpunkt zweier Geraden auf den zugehörigen Strecken liegt; Ausgabe erolgt in Form eines Booleschen Wertes
def limit(strecke1, strecke2, spx, spy):
    x = 0
    if Var(strecke1)[0] <= spx <= Var(strecke1)[2] or Var(strecke1)[0] >= spx >= Var(strecke1)[2]:
        x = x + 1
    if Var(strecke1)[1] <= spy <= Var(strecke1)[3] or Var(strecke1)[1] >= spy >= Var(strecke1)[3]:
        x = x + 1
    if Var(strecke2)[0] <= spx <= Var(strecke2)[2] or Var(strecke2)[0] >= spx >= Var(strecke2)[2]:
        x = x + 1
    if Var(strecke2)[1] <= spy <= Var(strecke2)[3] or Var(strecke2)[1] >= spy >= Var(strecke2)[3]:
        x = x + 1
    if x == 4:
        return True
    else:
        return False


#################################################Programm###############################################################

datei = input('Geben sie den Namen der zu bearbeitenden Datei ein: ')

streckentxt = open(datei)
streckentext = streckentxt.read()
streckentxt.close()

streckenp = []

#String in einzelne Zeilen (Strecken) zerlegen und sammeln dieser in der Liste streckenp
x = 0
for a in range(0,len(streckentext)):
    if streckentext[a:(a+1)] == '\n':
        streckenp = streckenp + [streckentext[x:a]]
        x = a + 1

streckenp = streckenp[1:]


loesung = ''

#die jeweiligen Schnittpunkte dreier Geraden berechnen und Überprüfung auf deren Existenz auf den Strecken (wenn es sie gibt, gibt es ein Dreieck)
for a in range(0,(len(streckenp)-2)):       #durch versetzte Parameter kann es nicht zu mehrfachen Betrachtungen kommen
    for b in range(a+1,(len(streckenp)-1)):
        for c in range(b+1,len(streckenp)):
            x = 0
            if Schnittpunkt(streckenp, a, b)[0]:
                x = x + 1
            if Schnittpunkt(streckenp, a, c)[0]:
                x = x + 1
            if Schnittpunkt(streckenp, b, c)[0]:
                x = x + 1
            if x == 3:      #Überprüfung ob es identische Punkte gibt
                if Schnittpunkt(streckenp, a, b) == Schnittpunkt(streckenp, a, c) or Schnittpunkt(streckenp, a, b) == Schnittpunkt(streckenp, b, c) or Schnittpunkt(streckenp, a, c) == Schnittpunkt(streckenp, b, c):        #Verhindern von Dreiecken aus nur einem Punkt, sowie doppelt auftretenden Dreiecken aufgrund von überlappenden Strecken
                    x= x - 3
                else:   
                    loesung = loesung + "(" + Schnittpunkt(streckenp, a, b)[1] + ' | ' + Schnittpunkt(streckenp, a, b)[2] + ') (' + Schnittpunkt(streckenp, a, c)[1] + ' | ' + Schnittpunkt(streckenp, a, c)[2] + ') (' + Schnittpunkt(streckenp, b, c)[1] + ' | ' + Schnittpunkt(streckenp, b, c)[2] + ') \n'

#Zählen der Dreiecke
zaehler = 0
for a in range(0, len(loesung)):
    if loesung[a:a+1] == '\n':
        zaehler = zaehler + 1

#Benutzerfreundliche Angabe der Anzahl der Dreiecke
if zaehler == 0:
    loesung = 'Es gibt kein Dreieck'
elif zaehler == 1:
    loesung = 'Es gibt ein Dreieck:\n' + loesung[:-1]
else:
    loesung = ('Es gibt %s Dreiecke:\n' %zaehler) + loesung[:-1]

#Ausgeben der Lösung(en) in der Konsole, sowie einer separaten Textdatei
print (loesung)

outdatei = datei.split(".")[0] + "-loes.txt"
loesungtxt = open(outdatei, mode='w')
loesungtxt.write(loesung)
loesungtxt.close()
