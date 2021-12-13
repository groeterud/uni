import java.util.ArrayList;

public class Kunde {
    private int kundenummer;
    private String navn;
    private String adresse;
    private String telefon;
    private ArrayList<Utleie> utleie = new ArrayList<Utleie>();

    public Kunde(int kundenummer, String navn, String adresse, String telefon) {
        this.kundenummer = kundenummer;
        this.navn = navn;
        this.adresse = adresse;
        this.telefon = telefon;
    }

    public ArrayList<Utleie> getUtleie() {
        return utleie;
    }
    //nødvendig for 2e
    public boolean nyttUtleie(Utleie ut) {
        if (ut!=null) {
            utleie.add(ut);
            return true;
        }
        return false;
    }

    public int getKundenummer() {
        return kundenummer;
    }

    public void setKundenummer(int kundenummer) {
        this.kundenummer = kundenummer;
    }

    public String getNavn() {
        return navn;
    }

    public void setNavn(String navn) {
        this.navn = navn;
    }

    public String getAdresse() {
        return adresse;
    }

    public void setAdresse(String adresse) {
        this.adresse = adresse;
    }

    public String getTelefon() {
        return telefon;
    }

    public void setTelefon(String telefon) {
        this.telefon = telefon;
    }

    @Override //3d og 3e
    public String toString() {
        return "Kunde{" +
                "kundenummer=" + kundenummer +
                ", navn='" + navn + '\'' +
                ", adresse='" + adresse + '\'' +
                ", telefon='" + telefon + '\'' +
                '}';
    }
}
