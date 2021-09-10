import java.util.Arrays;
/*
Egen klasse for ordlister. Eksisterer for å kunne ha ordlister av dynamisk lengde, og uten at vi trenger å
spørre brukeren hvor mange av hvert enkelt kategorie h'n måtte ønske å leggge til.
 */
public class Ordliste {
    private String[] ord;
    private int count;
    private int size;

    public Ordliste(String[] ord) {
        this.ord=ord;
        size=ord.length;
        count=0;
    }
    // returnerer ordlisten, ryddet for null-merker
    public String[] getOrd() {
        //litt cleanup først:
        int teller=0;
        for (int i = 0; i < size; i++) {
            if (ord[i]==null) {
                teller++;
            }
        }
        // nye listen skal være like lang som vårt faktiske innhold
        String[] temp = new String[size-teller];
        // legger til alle ord som ikke er null
        for (int i = 0; i < size; i++) {
            if (ord[i]!=null){
                temp[i]=ord[i];
            }
        }
        // resetter tellere og overkjører, slik at vi kan registrere fler ord etterpå uten å restarte programmet.
        this.ord=temp;
        this.size= ord.length;
        this.count=size;
        return ord;
    }

    // legg til flere ord i listen.
    public void addOrd(String nyttOrd) {
        // om listen er full så må vi øke den først
        if (count==size) {
            grow();
        }
        // legger til ordet på nåværende ledige indeks.
        ord[count]=nyttOrd;
        count++;
    }

    // dobler størrelsen på arrayet
    public void grow() {
        // lager temp array med 2x størrelse.
        String[] temp = new String[size*2];
        // overfører gammel data
        for (int i = 0; i < size; i++) {
            temp[i]=ord[i];
        }
        // overwriter gammelt array med ny array.
        ord=temp;
        size= ord.length;
    }

    @Override // lagde toString mest for debugging...
    public String toString() {
        return "Ordliste{" +
                "ord=" + Arrays.toString(ord) +
                '}';
    }
}