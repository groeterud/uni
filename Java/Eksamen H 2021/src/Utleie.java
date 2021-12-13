public class Utleie {
    private String utleiedato;
    private String tilbakeleveringsdato;
    private double pris;
    private Kamera kamera;
    private Kunde kunde;

    //double gjøres om til Double for å kunne instansieres som null i oppgave 2e
    public Utleie(String utleiedato, String tilbakeleveringsdato, Double pris, Kamera kamera, Kunde kunde) {
        this.utleiedato = utleiedato;
        this.tilbakeleveringsdato = tilbakeleveringsdato;
        this.pris = pris;
        this.kamera = kamera;
        this.kunde = kunde;
    }

    public String getUtleiedato() {
        return utleiedato;
    }

    public void setUtleiedato(String utleiedato) {
        this.utleiedato = utleiedato;
    }

    public String getTilbakeleveringsdato() {
        return tilbakeleveringsdato;
    }

    public void setTilbakeleveringsdato(String tilbakeleveringsdato) {
        this.tilbakeleveringsdato = tilbakeleveringsdato;
    }

    public double getPris() {
        return pris;
    }

    public void setPris(double pris) {
        this.pris = pris;
    }

    public Kamera getKamera() {
        return kamera;
    }

    public void setKamera(Kamera kamera) {
        this.kamera = kamera;
    }

    public Kunde getKunde() {
        return kunde;
    }

    public void setKunde(Kunde kunde) {
        this.kunde = kunde;
    }

    @Override //3d og 3e
    public String toString() {
        return "Utleie{" +
                "utleiedato='" + utleiedato + '\'' +
                ", tilbakeleveringsdato='" + tilbakeleveringsdato + '\'' +
                ", pris=" + pris +
                '}';
    }
}
