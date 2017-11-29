package de.lukasrost.bwinf2017.zimmerbelegung;

import javax.swing.*;
import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {

    private static List<Schueler> schuelerList;
    private static List<Zimmer> zimmerList;

    public static void main(String[] args) {
        schuelerList = new ArrayList<>();
        zimmerList = new ArrayList<>();
        readToObjects();
        if (getSolution() && schlussCheck()) {
            System.out.println("Zimmerbelegung moeglich! \nGebe Zimmerbelegung in Datei aus... \nBitte Speicherort waehlen!");
            writeToFile();
        } else {
            System.out.println("Zimmerbelegung nicht moeglich!");
        }
    }

    private static void writeToFile() { //Erstellung der Ausgabe nach von Bwinf empfohlener Syntax
        StringBuilder output = new StringBuilder();
        for (Zimmer zimmer: zimmerList){
            List<String> schuelerTemp = zimmer.getMitglieder();
            for (String schueler: schuelerTemp){
                if (schuelerTemp.indexOf(schueler) == schuelerTemp.size() -1){
                    output.append(schueler);
                } else {
                    output.append(schueler);
                    output.append(", ");
                }
            }
            output.append("\n");
        }
        saveFile(output.toString());
    }

    private static boolean getSolution() { //Hauptschleife zur Zimmeraufteilung
        for (Schueler schueler: schuelerList) {
            boolean jemandVonPlusListinZimmer = false;
            List<Zimmer> zimmerVonPlusListLeuten = new ArrayList<>();
            if (schueler.getPlusList().size() > 0){ //Plus-Liste vorhanden
                for (Zimmer z: zimmerList) {
                    if(z.isInZimmer(schueler.getName())){
                        jemandVonPlusListinZimmer = true;
                        zimmerVonPlusListLeuten.add(z);
                    }
                    for (String s:schueler.getPlusList()) {
                        if(z.isInZimmer(s)){
                            jemandVonPlusListinZimmer = true;
                            zimmerVonPlusListLeuten.add(z);
                        }
                    }
                }
                Zimmer currentZimmer = (jemandVonPlusListinZimmer) ? zimmerVonPlusListLeuten.get(0) : null;
                if (jemandVonPlusListinZimmer && zimmerVonPlusListLeuten.stream().distinct().count() != 1){ //Leute von Plus-Liste in untersch. Zimmern?
                    currentZimmer = mergeZimmer(zimmerVonPlusListLeuten.stream().distinct().collect(Collectors.toList()));
                }
                if (jemandVonPlusListinZimmer){ //in bestehendes Zimmer aufnehmen
                    if(!currentZimmer.isInZimmer(schueler.getName())) { //Schueler schon in diesem Zimmer?
                        currentZimmer.addMitglied(schueler.getName());
                    }
                    for (String s:schueler.getPlusList()) {
                        if(!currentZimmer.isInZimmer(s)) { //Schueler schon in diesem Zimmer?
                            currentZimmer.addMitglied(s);
                        }
                    }
                } else{ //neues Zimmer erstellen
                    currentZimmer = new Zimmer();
                    currentZimmer.addMitglied(schueler.getName());
                    for (String s:schueler.getPlusList()) {
                        currentZimmer.addMitglied(s);
                    }
                    zimmerList.add(currentZimmer);
                }
                if (hasKonflikte(currentZimmer)){ //Konflikte mit Minus-Listen ueberpruefen
                    return false;
                }
            }
        }
        for (Schueler schueler: schuelerList){
            boolean isInAZimmer = false;
            for (Zimmer z: zimmerList) {
                if (z.isInZimmer(schueler.getName())) {
                    isInAZimmer = true;
                }
            }
            if (schueler.getPlusList().size() == 0 && !isInAZimmer){
                Zimmer zi = new Zimmer();
                zi.addMitglied(schueler.getName());
                zimmerList.add(zi);
            }
            if (schueler.getMinusList().contains(schueler.getName())){ //Sonderfall: Schueler will mit sich selbst nicht auf Zimmer sein
                System.out.println("Eingabedatenfehler oder schizophrener Schueler!");
                return false;
            }
        }
        return true;
    }

    private static Schueler findSchuelerByName(String name) throws Exception{
        for (Schueler schueler: schuelerList) {
            if (schueler.getName().equals(name)){
                return schueler;
            }
        }
        throw new Exception("Schueler nicht gefunden!");
    }

    private static boolean hasKonflikte(Zimmer zimmer){
        for (String schueler : zimmer.getMitglieder()) {
            try {
                for (String minusListenSchueler: findSchuelerByName(schueler).getMinusList()) {
                    if (zimmer.isInZimmer(minusListenSchueler)){
                        return true;
                    }
                }
            } catch (Exception e) {
                System.out.println("Schwerer Fehler:" + e.getLocalizedMessage() + "Klassenfahrt muss ausfallen!");
            }
        }
        return false;
    }

    private static Zimmer mergeZimmer(List<Zimmer> zimmersToMerge){
        Zimmer mergedZimmer = new Zimmer();
        for (Zimmer z : zimmersToMerge) {
            for (String schueler: z.getMitglieder()) {
                mergedZimmer.addMitglied(schueler);
            }
        }
        zimmerList.add(mergedZimmer);
        zimmerList.removeAll(zimmersToMerge);
        return mergedZimmer;
    }


    private static void readToObjects() {
        File file = getFile();
        int lineNumber = 1;
        int index = 0;
        try(BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line = br.readLine();
            while (line != null) {
                if (lineNumber == 1){ //Einlesen des Schueler-Namens
                    schuelerList.add(new Schueler());
                    schuelerList.get(index).setName(line.trim());
                }
                if (lineNumber == 2){ //Einlesen der Plus-Liste des Schuelers
                    String[] temp = line.split(" ");
                    for (String a: temp) {
                       if(a.equals("+")) {continue;}
                       else {
                           schuelerList.get(index).addToPlusList(a);
                       }
                    }
                }
                if (lineNumber == 3){ //Einlesen der Minus-Liste des Schuelers
                    String[] temp = line.split(" ");
                    for (String a: temp) {
                        if(a.equals("-")) {continue;}
                        else {
                            schuelerList.get(index).addToMinusList(a);
                        }
                    }
                }
                if (lineNumber == 4){ //Einlesen der Trennzeile, Zurücksetzen der Zeilennummer,  Erhoehen des Indexes für die Schueler-Liste
                    lineNumber = 0;
                    index++;
                }
                lineNumber++;
                line = br.readLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    private static File getFile(){ //Benutzerauswahl der einzulesenden Datei und Umwandlung in ein File-Objekt
        JFileChooser chooser = new JFileChooser();
        File file = null;
        int rueckgabeWert = chooser.showOpenDialog(null);
        if (rueckgabeWert == JFileChooser.APPROVE_OPTION){
            file = chooser.getSelectedFile();
        } else {
            System.exit(0);
        }
        return file;
    }

    private static void saveFile(String content){ //Benutzerauswahl des Speicherorts der Ausgabedatei...
        String file = "";
        JFileChooser chooser = new JFileChooser();
        int rueckgabeWert = chooser.showSaveDialog(null);
        if (rueckgabeWert == JFileChooser.APPROVE_OPTION){
            file = chooser.getSelectedFile().getAbsolutePath();
        } else {
            System.exit(0);
        }
        try{
            PrintWriter out = new PrintWriter(file); //... und Schreiben der Ausgabe in diese
            out.println( content );
            out.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    private static boolean hasKonfliktePos(Zimmer zimmer){
        for (String schueler : zimmer.getMitglieder()) {
            try {
                for (String plusListenSchueler: findSchuelerByName(schueler).getPlusList()) {
                    if (!(zimmer.isInZimmer(plusListenSchueler))){
                        return true;
                    }
                }
            } catch (Exception e) {
                System.out.println("Schwerer Fehler:" + e.getLocalizedMessage() + "Klassenfahrt muss ausfallen!");
            }
        }
        return false;
    }

    private static boolean schlussCheck(){
        for (Zimmer z: zimmerList){
            if (hasKonflikte(z)){
                return false;
            }
            if(hasKonfliktePos(z)){
                return false;
            }
        }
        return true;
    }
}
