package de.lukasrost.bwinf2017.zimmerbelegung;

import java.util.ArrayList;
import java.util.List;

public class Schueler {

    private String name;
    private List<String> plusList;
    private List<String> minusList;

    public Schueler() {
        super();
        minusList = new ArrayList<>();
        plusList = new ArrayList<>();
    }

    public List<String> getPlusList() {
        return plusList;
    }

    public void addToPlusList(String key) {
        plusList.add(key);
    }

    public List<String> getMinusList() {
        return minusList;
    }

    public void addToMinusList(String key) {
        minusList.add(key);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
