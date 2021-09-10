import com.sun.org.apache.xpath.internal.operations.Or;

import javax.swing.*;

public class Grensesnitt {
    Kontroller kontroller = new Kontroller();
    private final String[] ALTERNATIV = {"enkelt dikt", "avansert dikt","avslutt"};
    private final String[] ALTERNATIV_ENKEL = {"Registrer ord", "Skriv dikt","Avslutt"};
    private final String[] ALTERNATIV_AVANSERT = {"Registrer artikkel","Registrer adjektiv","Registrer substantiv","Registrer verb", "Skriv dikt","Avslutt"};
    public void meny() {
        /*
        Brukt til testing, beholder det her for å vise testing.

        String[] ord = {"kake", "bil","sjåfør","uber","kakespade","oransje","Karen","covid","håper","kjører","sakte","fort","rart","kjapt","treigt","sidelengs","dalen","svingen","er","kanskje","dette","nok"};
        String[] artikkel = {"den", "dette"};
        String[] adjektiv = {"grønne","vimsete","klønete","ville"};
        String[] substantiv = {"boken","gulroten","trekanten","læreren"};
        String[] verb = {"danser","sover","vokser","snorker"};

        System.out.println(kontroller.dikt_enkel(ord));

        System.out.println(kontroller.dikt_avansert(artikkel,adjektiv,substantiv,verb));
         */
        // løkke for hovedmeny
        boolean fortsett = true;
        while (fortsett) {
            int valg = velgDikt();
            switch (valg) {
                case 0:
                    enkelt_dikt();
                    break;
                case 1:
                    avansert_dikt();
                    break;
                default: fortsett = false;
            }
        }

    }
    public int velgDikt() {
        int valg = JOptionPane.showOptionDialog(
                null,
                "Gjør et valg",
                "DiktGenerator",
                JOptionPane.DEFAULT_OPTION,
                JOptionPane.PLAIN_MESSAGE,
                null,
                ALTERNATIV,
                ALTERNATIV[0]
        );
        return valg;
    }
    public void enkelt_dikt() {
        // lager ordlisten
        Ordliste ordliste = new Ordliste(new String[1]);
        // menyløkke for enkelt dikt
        boolean fortsett=true;
        while (fortsett) {
            int valg = enkelt_dikt_valg();
            switch (valg) {
                case 0: // legg inn nytt ord
                    String ord = JOptionPane.showInputDialog("Skriv inn ord:");
                    ordliste.addOrd(ord);
                    break;
                case 1: // skriv ut dikt
                    JOptionPane.showMessageDialog(null,kontroller.dikt_enkel(ordliste.getOrd()));
                    break;
                default: fortsett = false;
            }
        }
    }
    public int enkelt_dikt_valg() {
        int valg = JOptionPane.showOptionDialog(
                null,
                "Gjør et valg",
                "Enkelt dikt",
                JOptionPane.DEFAULT_OPTION,
                JOptionPane.PLAIN_MESSAGE,
                null,
                ALTERNATIV_ENKEL,
                ALTERNATIV_ENKEL[0]
        );
        return valg;
    }


    public void avansert_dikt() {
        String ord; // brukes av flere caser
        // egne objekt for kategoriene, slik at vi kan ta vare på de individuelt.
        Ordliste artikkel = new Ordliste(new String[1]);
        Ordliste adjektiv  = new Ordliste(new String[1]);
        Ordliste substantiv = new Ordliste(new String[1]);
        Ordliste verb = new Ordliste(new String[1]);
        // meny-løkke
        boolean fortsett=true;
        while (fortsett) {
            int valg = avansert_dikt_valg();
            switch (valg) {
                case 0: // legg til artikkel
                    ord = JOptionPane.showInputDialog("Skriv inn artikkel");
                    artikkel.addOrd(ord);
                    break;
                case 1: // legg til adjektiv
                    ord = JOptionPane.showInputDialog("Skriv inn adjektiv");
                    adjektiv.addOrd(ord);
                    break;
                case 2: // legg til substantiv
                    ord = JOptionPane.showInputDialog("Skriv inn substantiv");
                    substantiv.addOrd(ord);
                    break;
                case 3: // legg til verb
                    ord = JOptionPane.showInputDialog("Skriv inn verb");
                    verb.addOrd(ord);
                    break;
                case 4: // skriv ut dikt
                    // Har her valgt å bruke getOrd() metoden til Ordliste, siden den returnerer String[]. Kunne gjort det mer semantisk ved å ha meldingen i en variabel evt.
                    JOptionPane.showMessageDialog(null,(kontroller.dikt_avansert(artikkel.getOrd(), adjektiv.getOrd(), substantiv.getOrd(), verb.getOrd())));
                    break;
                default: fortsett =false;
            }
        }
    }
    public int avansert_dikt_valg() {
        int valg = JOptionPane.showOptionDialog(
                null,
                "Gjør et valg",
                "Avansert Dikt",
                JOptionPane.DEFAULT_OPTION,
                JOptionPane.PLAIN_MESSAGE,
                null,
                ALTERNATIV_AVANSERT,
                ALTERNATIV_AVANSERT[0]
        );
        return valg;
    }
}