import javax.swing.*;

public class Grensesnitt {
    Kontroll kontroll = new Kontroll();
    private final String[] ALTERNATIV = {"Legg til ny gaupe", "Legg til ny hare","Gjennfangst gaupe","Gjennfangst hare","Søk på dyr","Alle dyr i register"};

    public void meny() {
        // Dummy data TODO: kommenter ut senere!!
        kontroll.nyGaupe("F",200.00,50.00, "20210515 20:33","Øvre havrevei 12",35.15);
        kontroll.nyGaupe("M",250.00,75.00,"20210610","Nydalssætra",42.00);
        kontroll.gjennFangstGaupe("G1","20210530","Hovdalssætra 14", 205.10,55.00,36.00);

        kontroll.nyHare("M",25.12,12.5,"20210101","S3","V","Lilla");
        kontroll.nyHare("F",23.12,09.5,"20212121","S4","S", "Brun");
        kontroll.gjennFangstHare("H1","20211001","S3",26.9,13.00,"Brun");

        boolean fortsett=true;
        while (fortsett) {
            int valg=velgFunc();
            switch (valg) {
                case 0:
                    nyGaupe();
                    break;
                case 1:
                    nyHare();
                    break;
                case 2:
                    gjennFangstGaupe();
                    break;
                case 3:
                    gjennFangstHare();
                    break;
                case 4:
                    søkDyr();
                    break;
                case 5:
                    printDyr();
                    break;
                default: fortsett=false;
            }
        }
    }
    public int velgFunc() {
        int valg = JOptionPane.showOptionDialog(
                null,
                "Gjør et valg",
                "Dyre register",
                JOptionPane.DEFAULT_OPTION,
                JOptionPane.PLAIN_MESSAGE,
                null,
                ALTERNATIV,
                ALTERNATIV[0]
        );
        return valg;
    }
    public void nyGaupe() {
        String kjønn=JOptionPane.showInputDialog("Skriv inn gaupas kjønn");
        Double lengde=Double.parseDouble(JOptionPane.showInputDialog("Skriv inn gaupas lengde"));
        Double vekt=Double.parseDouble(JOptionPane.showInputDialog("Skriv inn gaupas vekt"));
        String tid=JOptionPane.showInputDialog("Når ble gaupen fanget?");
        String sted=JOptionPane.showInputDialog("Hvor ble gaupen fanget?");
        Double øretustLengde=Double.parseDouble(JOptionPane.showInputDialog("Hvor lange er gaupens øretuster?"));
        //legger til
        kontroll.nyGaupe(kjønn,lengde,vekt,tid,sted,øretustLengde);
        //bekrefter
        JOptionPane.showMessageDialog(null,"La til gaupen");
    }
    public void nyHare() {
        String kjønn=JOptionPane.showInputDialog("Skriv inn harens kjønn");
        Double lengde=Double.parseDouble(JOptionPane.showInputDialog("Skriv inn harens lengde"));
        Double vekt=Double.parseDouble(JOptionPane.showInputDialog("Skriv inn harens vekt"));
        String tid=JOptionPane.showInputDialog("Når ble haren fanget?");
        String sted=JOptionPane.showInputDialog("Hvor ble haren fanget?");
        String hareType=JOptionPane.showInputDialog("Hvordan type hare er det?");
        String pelsFarge=JOptionPane.showInputDialog("Hvilken farge er det på pelsen til haren?");
        //legger til
        kontroll.nyHare(kjønn,lengde,vekt,tid,sted,hareType,pelsFarge);
        //bekrefter
        JOptionPane.showMessageDialog(null,"La til haren");
    }
    public void gjennFangstGaupe() {
        String id=JOptionPane.showInputDialog("Skriv inn gaupas ID");
        Double lengde=Double.parseDouble(JOptionPane.showInputDialog("Skriv inn gaupas lengde"));
        Double vekt=Double.parseDouble(JOptionPane.showInputDialog("Skriv inn gaupas vekt"));
        String tid=JOptionPane.showInputDialog("Når ble gaupen fanget?");
        String sted=JOptionPane.showInputDialog("Hvor ble gaupen fanget?");
        Double øretustLengde=Double.parseDouble(JOptionPane.showInputDialog("Hvor lange er gaupens øretuster?"));
        //legger til
        kontroll.gjennFangstGaupe(id,tid,sted,lengde,vekt,øretustLengde);
        //bekrefter
        JOptionPane.showMessageDialog(null,"Gjennfangst registrert");
    }
    public void gjennFangstHare() {
        String id=JOptionPane.showInputDialog("Skriv inn harens ID");
        Double lengde=Double.parseDouble(JOptionPane.showInputDialog("Skriv inn harens lengde"));
        Double vekt=Double.parseDouble(JOptionPane.showInputDialog("Skriv inn harens vekt"));
        String tid=JOptionPane.showInputDialog("Når ble haren fanget?");
        String sted=JOptionPane.showInputDialog("Hvor ble haren fanget?");
        String pelsFarge=JOptionPane.showInputDialog("Hvilken farge er det på pelsen til haren?");
        //legger til
        kontroll.gjennFangstHare(id,tid,sted,lengde,vekt,pelsFarge);
        //bekrefter
        JOptionPane.showMessageDialog(null,"Gjennfangst registrert");
    }
    public void søkDyr() {
        String id=JOptionPane.showInputDialog("Skriv inn dyrets ID");
        String print=kontroll.printDyr(id);
        JOptionPane.showMessageDialog(null,print);
    }
    public void printDyr() {
        String print= kontroll.printAlleDyr();
        JOptionPane.showMessageDialog(null,print);
    }
}
