import java.util.ArrayList;
import java.util.Collections;

public class Kontroll {
    private ArrayList<Kunde> kunder;
    private ArrayList<Kamera> kameraer;

    // 2b
    public boolean nyttKamera(Kamera kamera) {
        if (kamera != null) {
            kameraer.add(kamera);
            return true;
        }
        return false;
    }
    // 2c
    public Kamera finnKamera(int serienummer) {
        for (Kamera kamera : kameraer) {
            if (kamera.getSerienummer()==serienummer) return kamera;
        }
        return null;
    }
    //2d
    public Kamera finnKameraBIN(int serienummer) {
        Collections.sort(kameraer);
        Kamera dummy = new Kamera(serienummer,null,null,null);
        int indeks = Collections.binarySearch(kameraer, dummy);
        if (indeks>=0) return kameraer.get(indeks); // om vi fant et kamera som matcher, returner det.
        return null; // ellers returner null
    }
    //2e
    public boolean nyttUtleie (int serienummer, int kundenummer, String utdato, String inndato) {
        // finner først kamera med serienummer
        Kamera kamera = finnKameraBIN(serienummer);
        if (kamera==null) return false; // avslutter her om vi ikke fant kamera
        // finner kunden
        Kunde kunde = finnKunde(kundenummer);
        if (kunde==null) return false; // avslutter her om vi ikke fant kunden
        Utleie utleie = new Utleie(utdato,inndato, null,kamera,kunde);
        return kunde.nyttUtleie(utleie); //nyttUtleie returner true om alt gikk som det skulle eller false om det ikke gjorde det.
    }
    //2f
    public ArrayList<Kunde> alleKunder() {
        return kunder;
    }
    //2g  - jeg ønsker ikke å ha en utleieliste i kontroll, da vi har det vi trenger i kunder, så jeg gjør det litt innviklet med vilje.
    // Avveiningen er minnebruk vs CPU bruk ved nøstede for-løkker, men også referanseintegriteten.
    // Vi risikerer å ha unøyaktig data om vi lagrer utleie mer enn en plass.
    public ArrayList<Utleie> alleUtleier() {
        ArrayList<Utleie> utleier = new ArrayList<>();
        for (Kunde kunde : kunder) { //går gjennom hver kunde
            ArrayList<Utleie> kundeUtleie = kunde.getUtleie(); // henter utleielisten
            for (Utleie kundeEnkeltUtleie : kundeUtleie) { //går gjennom hvert enkeltutleie til hver kunde.
                utleier.add(kundeEnkeltUtleie); //og legger til i listen over alle utleier
            }
        }
        return utleier;
    }
}
