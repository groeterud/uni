import javax.swing.*;
import java.util.ArrayList;

public class Grensesnitt {
    Kontroll kontroll = new Kontroll();
    private final String[] ALTERNATIV = {"speilrefleks","speilløst"};

    // 3a
    public void nyttKamera() {
        int valg = lesValgKamera();
        switch (valg) {
            case 0:
                nyttSpeilrefleks();
                break;
            case 1:
                nyttSpeilløst();
                break;
        }
    }
    //3a
    public int lesValgKamera() {
        int valg = JOptionPane.showOptionDialog(
                null,
                "Velg type kamera",
                "Registrer Kamera",
                JOptionPane.DEFAULT_OPTION,
                JOptionPane.PLAIN_MESSAGE,
                null,
                ALTERNATIV,
                ALTERNATIV[0]
        );
        return valg;
    }
    //3a
    public void nyttSpeilrefleks() {
        int serienummer = Integer.parseInt(JOptionPane.showInputDialog("Hva er kameraets serienummer? "));
        String fabrikat = JOptionPane.showInputDialog("Fabrikat? ");
        String modell = JOptionPane.showInputDialog("Modell? ");
        int megapixler = Integer.parseInt(JOptionPane.showInputDialog("Hvor mange megapixler? "));
        Kamera kamera = new Kamera(serienummer,fabrikat,modell,megapixler);
        if (kontroll.nyttKamera(kamera)) JOptionPane.showMessageDialog(null, "Kamera registrert");
        else JOptionPane.showMessageDialog(null,"Noe gikk galt");
    }

    //3b
    public void finnKamera() {
        int serienummer = Integer.parseInt(JOptionPane.showInputDialog("Hva er kameraets serienummer? "));
        Kamera kamera = kontroll.finnKameraBIN(serienummer);
        if (kamera!=null) {
            System.out.println(kamera.toString()); //kunne brukt ShowMessageDialog her.
        }
        else System.out.println("Fant ikke noe kamera med det serienummeret");
    }
    //3c
    public void nyttUtleie() {
        int serienummer = Integer.parseInt(JOptionPane.showInputDialog("Hva er kameraets serienummer? "));
        int kundenummer= Integer.parseInt(JOptionPane.showInputDialog("Hva er kundens kundenummer? "));
        String utdato = JOptionPane.showInputDialog("Utleveringsdato?");
        String inndato = JOptionPane.showInputDialog("Innleveringsdato?");
        //kontroll.nyttUtleie returner true/false basert på kamera og kundeinformasjon
        if (kontroll.nyttUtleie(serienummer,kundenummer,utdato,inndato)) JOptionPane.showMessageDialog(null,"Utleie Registrert");
        else JOptionPane.showMessageDialog(null,"Noe gikk galt");
    }
    //3d
    public void alleKunder() {
        ArrayList<Kunde> kunder = kontroll.alleKunder();
        System.out.println("Informasjon om alle kunder, med utleie og kamerainformasjon");
        //går gjennom alle kunder:
        for (Kunde kunde : kunder) {
            //printer info om kunden.
            System.out.println(kunde.toString());
            //finner alle utleier til kunden.
            ArrayList<Utleie> utleie = kunde.getUtleie();
            for (Utleie enkeltUtleie : utleie) { //går gjennom alle utleier i lista
                Kamera kamera = enkeltUtleie.getKamera();
                System.out.println(enkeltUtleie.toString()); //printer ut informasjon om utleiet
                System.out.println(kamera.toString()); // printer ut informasjon om kameraet.
            }
        }
    }
    //3e
    public void alleUtleier() {
        ArrayList<Utleie> utleier = kontroll.alleUtleier();
        //går gjennom alle utleier. Har brukt foreach i alle for løkker, bruker itterativ her bare for å vise at jeg kan det. Liker bare å spare de to linjene.
        for (int i = 0; i < utleier.size(); i++) {
            Utleie utleie = utleier.get(i); // henter ut enkeltutleie
            Kamera kamera = utleie.getKamera(); //henter ut kameraet
            Kunde kunde = utleie.getKunde(); //henter ut kunden
            System.out.println(utleie.toString()); //printer info om utleiet.
            System.out.println(kamera.toString()); //printer info om kameraet til utleiet
            System.out.println(kunde.toString()); //printer info om kunden som har leid.
        }
    }
}
