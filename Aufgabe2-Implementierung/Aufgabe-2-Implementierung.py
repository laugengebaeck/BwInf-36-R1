def PreisB(AnzErw,AnzKin,AnzGut,Wochenende,Ferien):
    Preis = 0
    AnzGruppe=0
    AnzFam=0
    GutFürProzent=0
    GutFürEinzel = 0
    if Ferien==1 or AnzGut < 1:
        GutFürProzent=0
        GutFürEinzel=0
        if Wochenende==1:
            if AnzErw==0:
                AnzGruppe=0
                AnzFam=0
                Preis=Preis+AnzKin*2.5
                
            elif AnzKin==0:
                AnzGruppe=0
                AnzFam=0
                Preis=Preis+AnzErw*3.5
                
            else:
                AnzGruppe=0
                ü=Familie(AnzErw,AnzKin,Preis)
                AnzErw=ü[0]
                AnzKin=ü[1]
                Preis=ü[2]
                AnzFam=ü[3]
                Preis=Preis + AnzKin*2.5+AnzErw*3.5

        else:
            if AnzErw==0:
                ü=Gruppe(AnzErw,AnzKin,Preis)
                AnzErw=ü[0]
                AnzKin=ü[1]
                Preis=ü[2]
                AnzGruppe=ü[3]
                AnzFam=0
                Preis=Preis+AnzKin*2
                

            elif AnzKin==0:
                ü=Gruppe(AnzErw,AnzKin,Preis)
                AnzErw=ü[0]
                AnzKin=ü[1]
                Preis=ü[2]
                AnzGruppe=ü[3]
                AnzFam=0
                Preis=Preis+AnzErw*2.8
                
            else:
                ü=Gruppe(AnzErw,AnzKin,Preis)
                AnzErw=ü[0]
                AnzKin=ü[1]
                Preis=ü[2]
                AnzGruppe=ü[3]
                
                ü=Familie(AnzErw,AnzKin,Preis)
                AnzErw=ü[0]
                AnzKin=ü[1]
                Preis=ü[2]
                AnzFam=ü[3]
                Preis=Preis+AnzKin*2+AnzErw*2.8
                
            
    elif Ferien==0 and AnzGut>0:
        if Wochenende==1:
            if AnzErw==0:
                AnzGruppe=0
                AnzFam=0
                
                if AnzGut>0 and AnzKin-AnzGut>=10:
                    AnzKin=AnzKin-(AnzGut-1)
                    GutFürProzent=1
                    GutFürEinzel=AnzGut-1
                    Preis=Preis+AnzKin*2.5*9/10
                elif AnzGut>0 and AnzKin-AnzGut<10:
                    AnzKin=AnzKin-AnzGut
                    GutFürProzent=0
                    GutFürEinzel=AnzGut
                    Preis=Preis+AnzKin*2.5
                    

            elif AnzKin==0:
                AnzGruppe=0
                AnzFam=0

                if AnzGut>0 and AnzErw-AnzGut>=10:
                    AnzErw=AnzErw-(AnzGut-1)
                    GutFürProzent=1
                    GutFürEinzel=AnzGut-1
                    Preis=Preis+AnzErw*3.5*9/10
                elif AnzGut>0 and AnzErw-AnzGut<10:
                    AnzErw=AnzErw-AnzGut
                    GutFürProzent=0
                    GutFürEinzel=AnzGut
                    Preis=Preis+AnzErw*3.5

            else:
                AnzGruppe=0

                if AnzGut>0 and AnzKin+AnzErw-AnzGut>=1:
                    ü=Familie(AnzErw,AnzKin,Preis)
                    AnzErwT=ü[0]
                    AnzKinT=ü[1]
                    PreisT=ü[2]
                    AnzFamT=ü[3]
                    if AnzErwT>=1:
                        if PreisT+AnzErwT*3.5+AnzKinT*2.5>=35:
                            while AnzErw>0 and AnzGut>1:
                                AnzErw=AnzErw-1
                                AnzGut=AnzGut-1
                            while AnzKin>0 and AnzGut>1:
                                AnzKin=AnzKin-1
                                AnzGut=AnzGut-1
                            GutFürProzent=1
                            GutFürEinzel=AnzGut-1
                            ü=Familie(AnzErw,AnzKin,Preis)
                            AnzErw=ü[0]
                            AnzKin=ü[1]
                            Preis=ü[2]
                            AnzFam=ü[3]
                            Preis=(Preis+AnzKin*2.5+AnzErw*3.5)*9/10
                        else:
                            while AnzErw>0 and AnzGut>0:
                                AnzErw=AnzErw-1
                                AnzGut=AnzGut-1
                            while AnzKin>0 and AnzGut>0:
                                AnzKin=AnzKin-1
                                AnzGut=AnzGut-1
                            GutFürProzent=0
                            GutFürEinzel=AnzGut
                            ü=Familie(AnzErw,AnzKin,Preis)
                            AnzErw=ü[0]
                            AnzKin=ü[1]
                            Preis=ü[2]
                            AnzFam=ü[3]
                            Preis=Preis+AnzKin*2.5+AnzErw*3.5
                    elif AnzErwT<1 and AnzKinT>=1:
                        if PreisT+AnzKinT*2.5>=25:
                            while AnzKin>0 and AnzGut>1:
                                AnzKin=AnzKin-1
                                AnzGut=AnzGut-1
                            GutFürProzent=1
                            GutFürEinzel=AnzGut-1
                            ü=Familie(AnzErw,AnzKin,Preis)
                            AnzErw=ü[0]
                            AnzKin=ü[1]
                            Preis=ü[2]
                            AnzFam=ü[3]
                            Preis=(Preis+AnzKin*2.5+AnzErw*3.5)*9/10
                        else:
                            while AnzKin>0 and AnzGut>0:
                                AnzKin=AnzKin-1
                                AnzGut=AnzGut-1
                            GutFürProzent=0
                            GutFürEinzel=AnzGut
                            ü=Familie(AnzErw,AnzKin,Preis)
                            AnzErw=ü[0]
                            AnzKin=ü[1]
                            Preis=ü[2]
                            AnzFam=ü[3]
                            Preis=Preis+AnzKin*2.5+AnzErw*3.5
                    else:
                        Preis=PreisT
                elif AnzGut>0 and AnzKin+AnzErw-AnzGut<1:
                    Preis=0
                

        else:
            if AnzErw==0:
                ü=Gruppe(AnzErw,AnzKin,Preis)
                AnzErwT=ü[0]
                AnzKinT=ü[1]
                PreisT=ü[2]
                AnzGruppeT=ü[3]
                
                if PreisT+AnzErwT*2.8+AnzKinT*2>=20:
                    while AnzErw>0 and AnzGut>1:
                        AnzErw=AnzErw-1
                        AnzGut=AnzGut-1
                    while AnzKin>0 and AnzGut>1:
                        AnzKin=AnzKin-1
                        AnzGut=AnzGut-1
                    GutFürProzent=1
                    GutFürEinzel=AnzGut-1
                    ü=Gruppe(AnzErw,AnzKin,Preis)
                    AnzErw=ü[0]
                    AnzKin=ü[1]
                    Preis=ü[2]
                    AnzGruppe=ü[3]
                    Preis=(Preis+AnzKin*2+AnzErw*2.8)*9/10
                else:
                    while AnzErw>0 and AnzGut>0:
                        AnzErw=AnzErw-1
                        AnzGut=AnzGut-1
                    while AnzKin>0 and AnzGut>0:
                        AnzKin=AnzKin-1
                        AnzGut=AnzGut-1
                    GutFürProzent=0
                    GutFürEinzel=AnzGut
                    ü=Gruppe(AnzErw,AnzKin,Preis)
                    AnzErw=ü[0]
                    AnzKin=ü[1]
                    Preis=ü[2]
                    AnzGruppe=ü[3]
                    Preis=(Preis+AnzKin*2+AnzErw*2.8)*9/10

            elif AnzKin==0:

                ü=Gruppe(AnzErw,AnzKin,Preis)
                AnzErwT=ü[0]
                AnzKinT=ü[1]
                PreisT=ü[2]
                AnzGruppeT=ü[3]
                AnzFam=0
                if PreisT+AnzErwT*2.8+AnzKinT*2>=28:
                    
                    while AnzErw>0 and AnzGut>1:
                        AnzErw=AnzErw-1
                        AnzGut=AnzGut-1
                    while AnzKin>0 and AnzGut>1:
                        AnzKin=AnzKin-1
                        AnzGut=AnzGut-1
                    GutFürProzent=1
                    GutFürEinzel=AnzGut-1
                    ü=Gruppe(AnzErw,AnzKin,Preis)
                    AnzErw=ü[0]
                    AnzKin=ü[1]
                    Preis=ü[2]
                    AnzGruppe=ü[3]
                    Preis=(Preis+AnzKin*2+AnzErw*2.8)*9/10
                else:
                    while AnzErw>0 and AnzGut>0:
                        AnzErw=AnzErw-1
                        AnzGut=AnzGut-1
                    while AnzKin>0 and AnzGut>0:
                        AnzKin=AnzKin-1
                        AnzGut=AnzGut-1
                    GutFürProzent=0
                    GutFürEinzel=AnzGut
                    ü=Gruppe(AnzErw,AnzKin,Preis)
                    AnzErw=ü[0]
                    AnzKin=ü[1]
                    Preis=ü[2]
                    AnzGruppe=ü[3]
                    Preis=(Preis+AnzKin*2+AnzErw*2.8)*9/10

            else:
                ü=Gruppe(AnzErw,AnzKin,Preis)
                AnzErwT=ü[0]
                AnzKinT=ü[1]
                PreisT=ü[2]
                AnzGruppeT=ü[3]
                
                ü=Familie(AnzErwT,AnzKinT,PreisT)
                AnzErwT=ü[0]
                AnzKinT=ü[1]
                PreisT=ü[2]
                AnzFamT=ü[3]
                if AnzErwT>=1:
                    if PreisT+AnzErwT*2.8+AnzKinT*2>=28:
                        while AnzErw>0 and AnzGut>1:
                            AnzErw=AnzErw-1
                            AnzGut=AnzGut-1
                        while AnzKin>0 and AnzGut>1:
                            AnzKin=AnzKin-1
                            AnzGut=AnzGut-1
                        GutFürProzent=1
                        GutFürEinzel=AnzGut-1
                        ü=Gruppe(AnzErw,AnzKin,Preis)
                        AnzErw=ü[0]
                        AnzKin=ü[1]
                        Preis=ü[2]
                        AnzGruppe=ü[3]

                        ü=Familie(AnzErw,AnzKin,Preis)
                        AnzErw=ü[0]
                        AnzKin=ü[1]
                        Preis=ü[2]
                        AnzFam=ü[3]
                    
                        Preis=(Preis+AnzKin*2+AnzErw*2.8)*9/10
                    else:
                        while AnzErw>0 and AnzGut>0:
                            AnzErw=AnzErw-1
                            AnzGut=AnzGut-1
                        while AnzKin>0 and AnzGut>0:
                            AnzKin=AnzKin-1
                            AnzGut=AnzGut-1
                        GutFürProzent=0
                        GutFürEinzel=AnzGut
                        ü=Gruppe(AnzErw,AnzKin,Preis)
                        AnzErw=ü[0]
                        AnzKin=ü[1]
                        Preis=ü[2]
                        AnzGruppe=ü[3]

                        ü=Familie(AnzErw,AnzKin,Preis)
                        AnzErw=ü[0]
                        AnzKin=ü[1]
                        Preis=ü[2]
                        AnzFam=ü[3]
                    
                        Preis=(Preis+AnzKin*2+AnzErw*2.8)*9/10
                elif AnzErwT<1 and AnzKinT>=1:
                    if PreisT+AnzErwT*2.8+AnzKinT*2>=28:
                        while AnzErw>0 and AnzGut>1:
                            AnzErw=AnzErw-1
                            AnzGut=AnzGut-1
                        while AnzKin>0 and AnzGut>1:
                            AnzKin=AnzKin-1
                            AnzGut=AnzGut-1
                        GutFürProzent=1
                        GutFürEinzel=AnzGut-1
                        ü=Gruppe(AnzErw,AnzKin,Preis)
                        AnzErw=ü[0]
                        AnzKin=ü[1]
                        Preis=ü[2]
                        AnzGruppe=ü[3]

                        ü=Familie(AnzErw,AnzKin,Preis)
                        AnzErw=ü[0]
                        AnzKin=ü[1]
                        Preis=ü[2]
                        AnzFam=ü[3]
                    
                        Preis=(Preis+AnzKin*2+AnzErw*2.8)*9/10
                    else:
                        while AnzErw>0 and AnzGut>0:
                            AnzErw=AnzErw-1
                            AnzGut=AnzGut-1
                        while AnzKin>0 and AnzGut>0:
                            AnzKin=AnzKin-1
                            AnzGut=AnzGut-1
                        GutFürProzent=0
                        GutFürEinzel=AnzGut
                        ü=Gruppe(AnzErw,AnzKin,Preis)
                        AnzErw=ü[0]
                        AnzKin=ü[1]
                        Preis=ü[2]
                        AnzGruppe=ü[3]

                        ü=Familie(AnzErw,AnzKin,Preis)
                        AnzErw=ü[0]
                        AnzKin=ü[1]
                        Preis=ü[2]
                        AnzFam=ü[3]
                    
                        Preis=(Preis+AnzKin*2+AnzErw*2.8)*9/10
                else:
                    Preis=PreisT
                    ü=Gruppe(AnzErw,AnzKin,Preis)
                    AnzErw=ü[0]
                    AnzKin=ü[1]
                    Preis=ü[2]
                    AnzGruppe=ü[3]
                
                    ü=Familie(AnzErw,AnzKin,Preis)
                    AnzErw=ü[0]
                    AnzKin=ü[1]
                    Preis=ü[2]
                    AnzFam=ü[3]
                    if AnzGut>=1:
                        Preis=(Preis+AnzKin*2+AnzErw*2.8)*9/10
                        GutFürProzent=1
                    else:
                        GutFürProzent=0
                        Preis=Preis+AnzKin*2+AnzErw*2.8
    return round(Preis,2), AnzGruppe, AnzFam, GutFürProzent, GutFürEinzel,AnzErw,AnzKin
            


def Gruppe(AnzErw,AnzKin,Preis):
    AnzGruppe=0
    while AnzErw+AnzKin>=6:
        m=0
        while AnzErw>0 and m<6:
            AnzErw=AnzErw-1
            m=m+1
        while AnzKin>0 and m<6:
            AnzKin=AnzKin-1
            m=m+1
        AnzGruppe=AnzGruppe+1
        Preis=Preis+11
    return AnzErw, AnzKin, Preis, AnzGruppe
        
def Familie(AnzErw,AnzKin,Preis):
    AnzFam=0
    while AnzErw>1 and AnzKin>1:
        AnzErw=AnzErw-2
        AnzKin=AnzKin-2
        AnzFam=AnzFam+1
        Preis=Preis+8
    if AnzErw>0 and AnzKin>2:
        while AnzErw/AnzKin<=1/3 and AnzErw>0 and AnzKin>2:
            AnzErw=AnzErw-1
            AnzKin=AnzKin-3
            AnzFam=AnzFam+1
            Preis=Preis+8
    return AnzErw, AnzKin, Preis, AnzFam
        

            


AnzKLKin=int(input("Bitte geben Sie die Anzahl der unter 4-Jährigen an: "))
AnzErw=int(input("Bitte geben Sie die Anzahl der über 16-Jährigen an: "))
AnzKin=int(input("Bitte geben Sie die Anzahl der 4- bis 16-Jährigen an: "))
AnzGut=int(input("Bitte geben Sie die Anzahl der Gutscheine an: "))
Wochenende=int(input("Bitte geben Sie 1 für Wochenende und 0 für Wochentag an: "))
Ferien=int(input("Bitte geben Sie 1 für Ferien und 0 für nicht Ferien an: "))
ü=0
Preis=0

if AnzErw == 0 and AnzKLKin > 0:
    print("")
    print(str(AnzKLKin) + " Kinder unter 4 Jahren dürfen das Freibad nicht betreten")

if AnzErw>=0 and AnzKin>=0 and AnzGut>=0:
    ü=PreisB(AnzErw,AnzKin,AnzGut,Wochenende,Ferien)

    print("")
    print("Es kostet %0.2f €, wenn man "% ü[0] +str(ü[1])+" Gruppentickets und "+str(ü[2])+" Familientickets kauft.")
    print("Dabei werden "+str(ü[3])+" Gutschein/e für 10% Ermäßigung und "+str(ü[4])+" Gutscheine zum freien Eintritt verwendet.")
    print("%s Erwachsenentickets und %s Kindertickets werden zusätzlich gekauft." % (str(ü[5]),str(ü[6])))
else:
    print("Eingabefehler!")

x=input()
