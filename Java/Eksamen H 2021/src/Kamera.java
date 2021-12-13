public class Kamera implements Comparable<Kamera> { //trengs for binærsøk i oppgave 2d{
    private int serienummer;
    private String fabrikat;
    private String modell;
    private int megapixler;

    // Megapixler må gjøres om til klassen Integer istedenfor datatypen int for å kunne initialiseres som 'null' i 2d
    public Kamera(int serienummer, String fabrikat, String modell, Integer megapixler) {
        this.serienummer = serienummer;
        this.fabrikat = fabrikat;
        this.modell = modell;
        this.megapixler = megapixler;
    }

    public int getSerienummer() {
        return serienummer;
    }

    public void setSerienummer(int serienummer) {
        this.serienummer = serienummer;
    }

    public String getFabrikat() {
        return fabrikat;
    }

    public void setFabrikat(String fabrikat) {
        this.fabrikat = fabrikat;
    }

    public String getModell() {
        return modell;
    }

    public void setModell(String modell) {
        this.modell = modell;
    }

    public int getMegapixler() {
        return megapixler;
    }

    public void setMegapixler(int megapixler) {
        this.megapixler = megapixler;
    }


    // nødvendig for å kunne sortere listen for å foreta binærsøk slik etterspurt i oppgave 2d
    @Override
    public int compareTo(Kamera o) {
        if (this.serienummer > o.getSerienummer()) return 1;
        if (this.serienummer < o.getSerienummer()) return -1;
        return 0;
    }

    @Override //toString nødvendig for 3b, 3d og 3e
    public String toString() {
        return "Kamera{" +
                "serienummer=" + serienummer +
                ", fabrikat='" + fabrikat + '\'' +
                ", modell='" + modell + '\'' +
                ", megapixler=" + megapixler +
                '}';
    }
}
