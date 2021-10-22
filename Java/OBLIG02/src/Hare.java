import java.util.ArrayList;

public class Hare extends Dyr{
    private String hareType;
    private String pelsFarge;

    public Hare(String identifikator, String kjønn, Double lengde, Double vekt, String tid, String sted, String hareType, String pelsFarge) {
        super(identifikator, kjønn, lengde, vekt, tid, sted);
        this.hareType = hareType;
        this.pelsFarge = pelsFarge;
        fangst(tid,sted,lengde,vekt,pelsFarge);
    }
    public void fangst(String tid,String sted,Double lengde,Double vekt, String pelsFarge) {
        // setter parametere
        super.setTid(tid);
        super.setSted(sted);
        super.setLengde(lengde);
        super.setVekt(vekt);
        this.pelsFarge=pelsFarge;
        // lager listen vår
        ArrayList<Object> temp = new ArrayList<Object>();
        temp.add(tid);
        temp.add(sted);
        temp.add(lengde);
        temp.add(vekt);
        temp.add(pelsFarge);
        // Legger listen til fangstHistorikken.
        fangstHistorikk.add(temp);
    }

    @Override
    public String toString() {
        return super.toString()+
                "Hare{" +
                "hareType='" + hareType + '\'' +
                ", pelsFarge='" + pelsFarge + '\'' +
                '}';
    }
}
