import sys,os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
prueffilename = askopenfilename(initialdir = os.path.dirname(os.path.realpath(__file__)),title = "Eingabedatei auswählen",filetypes = (("Textdateien","*.txt"),("Alle Dateien","*.*")))

fileliste=open('kuerzelliste.txt','r',encoding="utf-8")
kuerzelliste=[]
for line in fileliste:
    kuerzelliste=kuerzelliste+[(line.rstrip())]
fileliste.close()                                                                           # Kürzelliste wird aus entsprechender Datei ausgelesen --> Python-Liste

filepruef=open(prueffilename,'r',encoding="utf-8")
for line in filepruef:
    pruef=line.rstrip()
filepruef.close()                                                                           # zu überprüfendes Wort wird aus entsprechender Datei ausgelesen --> String

if len(pruef)<=1 or "Ä" in pruef:
    print('-----------------------------------------------------------------')
    print('Wort:',pruef)
    print('Wortlänge:',len(pruef))
    print('')
    print('Es gibt keine Möglichkeit, das Wort mit Autokennzeichen zu schreiben.')
    print('-----------------------------------------------------------------')
    sys.exit()                                                                              # Ausnahme für Wort mit einem Buchstaben oder Ä im Wort

for x in range(0,len(pruef)):
    if 5*x>=len(pruef):
        minaz=x
        break

for x in range(0,len(pruef)):
    if 2*x>=len(pruef):
        maxaz=x
        break                                     # Ermittlung der theoretischen Minimal- und Maximalzahl an Kennzeichen (auf ein Kennzeichen passen zwischen zwei und fünf Buchstaben)

solutions=[]
for x in range(minaz,maxaz+1):
    summe=[]
    while x!=0:
        summe=summe+[2]
        x=x-1                                                                   # Bildung der Anfangskombination 2+2+2+...+2+2
    while 1==1:
        pruefstring=''
        for a in range(0,len(summe)):
            if summe[a]==5:
                pruefstring=pruefstring+'a'                                     # für jeden Summanden==5 wird pruefstring wird um ein Zeichen verlängert
        if len(pruefstring)!=len(summe):                                        # prüfe, ob Endkombination 5+5+5+...+5+5 erreicht ist; wenn nicht:
            s=0
            for y in range(0,len(summe)):
                s=s+int(summe[y])                                               # berechne momentane Summe an Buchstaben auf den Kennzeichen
            if s==len(pruef):
                summestring=''
                for i in summe:
                    summestring=summestring+str(i)
                solutions=solutions+[summestring]                               # wenn Summe der Länge des zu überprüfenden Wortes entspricht, speichere aktuelle Kombi
            z=1
            while z<=len(summe):
                if summe[len(summe)-z]!=5:
                    summe[len(summe)-z]=(summe[len(summe)-z])+1
                    break
                else:
                    summe[len(summe)-z]=2
                    z=z+1                                                 # setze nächte Kombination (hintere Stelle+1; falls hintere Stelle==5: hintere Stelle=2 und vorletzte Stelle+1)
        else:
            s=0
            for y in range(0,len(summe)):
                s=s+int(summe[y])
            if s==len(pruef):
                summestring=''
                for i in summe:
                    summestring=summestring+str(i)
                solutions=solutions+[summestring]
            break                                                               # überprüfe noch diese Kombination, danach Ende

azlsg=0
ergebnis=['newsolution']

for x in solutions:                                                             # für jede Kombination, die theoretisch eine korrekte Buchstabenverteilung auf dem Kennzeichen angibt
    pruefwort=pruef
    solution=str(x)
    true=1
    while len(pruefwort)!=0 and true!=0:
        while len(solution)!=0:
            true=0
            if solution[0]=='2':
                for b in range(0,len(kuerzelliste)):
                    if pruefwort[0]==kuerzelliste[b] and pruefwort[1]!='Ä' and pruefwort[1]!='Ö' and pruefwort[1]!='Ü':
                        ergebnis=ergebnis+[11]
                        ergebnis=ergebnis+[pruefwort[0]+pruefwort[1]]
                        true=1
                        pruefwort=pruefwort[2:]
                        break
                        
            elif solution[0]=='3':
                for b in range(0,len(kuerzelliste)):
                    if pruefwort[0]==kuerzelliste[b] and pruefwort[1]!='Ä' and pruefwort[1]!='Ö' and pruefwort[1]!='Ü' and pruefwort[2]!='Ä' and pruefwort[2]!='Ö' and pruefwort[2]!='Ü':
                        ergebnis=ergebnis+[12]
                        ergebnis=ergebnis+[pruefwort[0]+pruefwort[1:3]]
                        true=1
                        pruefwort=pruefwort[3:]
                        break
                if true==0:    
                    for b in range(0,len(kuerzelliste)):
                        if pruefwort[0:2]==kuerzelliste[b] and pruefwort[2]!='Ä' and pruefwort[2]!='Ö' and pruefwort[2]!='Ü':
                            ergebnis=ergebnis+[21]
                            ergebnis=ergebnis+[pruefwort[0:2]+pruefwort[2]]
                            true=1
                            pruefwort=pruefwort[3:]
                            break
            
            elif solution[0]=='4':
                for b in range(0,len(kuerzelliste)):
                    if pruefwort[0:2]==kuerzelliste[b] and pruefwort[2]!='Ä' and pruefwort[2]!='Ö' and pruefwort[2]!='Ü' and pruefwort[3]!='Ä' and pruefwort[3]!='Ö' and pruefwort[3]!='Ü':
                        ergebnis=ergebnis+[22]
                        ergebnis=ergebnis+[pruefwort[0:2]+pruefwort[2:4]]
                        true=1
                        pruefwort=pruefwort[4:]
                        break
                if true==0:
                    for b in range(0,len(kuerzelliste)):
                        if pruefwort[0:3]==kuerzelliste[b] and pruefwort[3]!='Ä' and pruefwort[3]!='Ö' and pruefwort[3]!='Ü':
                            ergebnis=ergebnis+[31]
                            ergebnis=ergebnis+[pruefwort[0:3]+pruefwort[3]]
                            true=1
                            pruefwort=pruefwort[4:]
                            break
            
            elif solution[0]=='5':
                for b in range(0,len(kuerzelliste)):
                    if pruefwort[0:3]==kuerzelliste[b] and pruefwort[3]!='Ä' and pruefwort[3]!='Ö' and pruefwort[3]!='Ü' and pruefwort[4]!='Ä' and pruefwort[4]!='Ö' and pruefwort[4]!='Ü':
                        ergebnis=ergebnis+[32]
                        ergebnis=ergebnis+[pruefwort[0:3]+pruefwort[3:5]]
                        true=1
                        pruefwort=pruefwort[5:]
                        break                                           # Überprüfe, ob die (je nach Länge bei der entsprechenden Mglk.) Ortskennung des ersten Kennzeichens vorhanden ist

            if true==0:
                while ergebnis[len(ergebnis)-1]!='newsolution':
                    ergebnis.pop(len(ergebnis)-1)                       # falls keine Lösung für diese Kennzeichenkombi, setze die Ergebnis-Liste entsprechend zurück
                break       
            else:
                solution=solution[1:]                                   # Lösche momentanes erstes Kennzeichen (abgehakt)
        if true==1:
            ergebnis=ergebnis+['newsolution']
            azlsg=azlsg+1

print('-----------------------------------------------------------------')
print('Wort:',pruef)
print('Wortlänge:',len(pruef))
print('')
if azlsg==0:
    print('Es gibt keine Möglichkeit, das Wort mit Autokennzeichen zu schreiben.')
    print('-----------------------------------------------------------------')
    sys.exit()
elif azlsg==1:
    print('Es gibt 1 Möglichkeit, das Wort mit Autokennzeichen zu schreiben.')
else:
    print('Es gibt',azlsg,'Möglichkeiten, das Wort mit Autokennzeichen zu schreiben.')
if azlsg!=0:
    print('Das Wort kann mit folgenden Kennzeichen geschrieben werden:')
    print('-----------------------------------------------------------------')

for x in ergebnis:
    if x==11:
        print('Kennzeichen 1-1')
        form='11'
    elif x==12:
        print('Kennzeichen 1-2')
        form='12'
    elif x==21:
        print('Kennzeichen 2-1')
        form='21'
    elif x==22:
        print('Kennzeichen 2-2')
        form='22'
    elif x==31:
        print('Kennzeichen 3-1')
        form='31'
    elif x==32:
        print('Kennzeichen 3-2')
        form='32'
    elif x=='newsolution':
        print('-----------------------------------------------------------------')
    else:
        if form=='11':
            print(x[0],'-',x[1])
        elif form=='12':
            print(x[0],'-',x[1:3])
        elif form=='21':
            print(x[0:2],'-',x[2])
        elif form=='22':
            print(x[0:2],'-',x[2:4])
        elif form=='31':
            print(x[0:3],'-',x[3])
        elif form=='32':
            print(x[0:3],'-',x[3:5])

if ergebnis==['newsolution']:
    print('')
    print('KEINE SCHREIBUNG MIT KENNZEICHEN MÖGLICH!!')
    print('')                                                                               # Interpretation des Ergebnis-Strings und benutzerfreundliche Ausgabe
