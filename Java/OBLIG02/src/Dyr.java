import java.util.ArrayList;

public abstract class Dyr implements Comparable<Dyr>{
    private String identifikator;
    private String kjønn;
    private Double lengde;
    private Double vekt;
    private String tid;
    private String sted;
    ArrayList<ArrayList<Object>> fangstHistorikk;

    // Generell konstruktør, instansierer
    public Dyr(String identifikator, String kjønn, Double lengde, Double vekt, String tid, String sted) {
        this.identifikator = identifikator;
        this.kjønn = kjønn;
        this.lengde = lengde;
        this.vekt = vekt;
        this.tid = tid;
        this.sted = sted;
        this.fangstHistorikk=new ArrayList<ArrayList<Object>>();
    }

    public String getIdentifikator() {
        return identifikator;
    }

    public String getKjønn() {
        return kjønn;
    }

    public Double getLengde() {
        return lengde;
    }

    public void setLengde(Double lengde) {
        this.lengde = lengde;
    }

    public Double getVekt() {
        return vekt;
    }

    public void setVekt(Double vekt) {
        this.vekt = vekt;
    }

    public String getTid() {
        return tid;
    }

    public void setTid(String tid) {
        this.tid = tid;
    }

    public String getSted() {
        return sted;
    }

    public void setSted(String sted) {
        this.sted = sted;
    }

    public ArrayList<ArrayList<Object>> getFangstHistorikk() {
        return fangstHistorikk;
    }

    @Override
    public int compareTo(Dyr o) {
        return this.identifikator.compareTo(o.getIdentifikator());
    }

    @Override
    public String toString() {
        return "Dyr{" +
                "identifikator='" + identifikator + '\'' +
                ", kjønn='" + kjønn + '\'' +
                ", lengde=" + lengde +
                ", vekt=" + vekt +
                ", tid='" + tid + '\'' +
                ", sted='" + sted + '\'' +
                ", fangstHistorikk=" + fangstHistorikk +
                '}';
    }
}
