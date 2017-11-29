package de.lukasrost.bwinf2017.zimmerbelegung;

import java.util.ArrayList;
import java.util.List;

public class Zimmer {

    private List<String> mitglieder;

    public Zimmer(){
        super();
        mitglieder = new ArrayList<>();
    }

    public List<String> getMitglieder() {
        return mitglieder;
    }

    public void addMitglied(String mitglied) {
        this.mitglieder.add(mitglied);
    }

    public boolean isInZimmer(String schueler){
        if (mitglieder.contains(schueler)){
            return true;
        }
        return false;
    }
}
