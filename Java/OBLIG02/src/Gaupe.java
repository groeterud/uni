import java.util.ArrayList;

public class Gaupe extends Dyr{
    private Double øretustLengde;

    public Gaupe(String identifikator, String kjønn, Double lengde, Double vekt, String tid, String sted, Double øretustLengde) {
        super(identifikator, kjønn, lengde, vekt, tid, sted);
        this.øretustLengde = øretustLengde;
        fangst(tid,sted,lengde,vekt,øretustLengde);

    }
    public void fangst(String tid,String sted,Double lengde,Double vekt, Double øretustLengde) {
        // setter parametere
        super.setTid(tid);
        super.setSted(sted);
        super.setLengde(lengde);
        super.setVekt(vekt);
        this.øretustLengde=øretustLengde;
        // lager listen vår
        ArrayList<Object> temp = new ArrayList<Object>();
        temp.add(tid);
        temp.add(sted);
        temp.add(lengde);
        temp.add(vekt);
        temp.add(øretustLengde);
        // Legger listen til fangstHistorikken.
        fangstHistorikk.add(temp);
    }

    @Override
    public String toString() {
        return super.toString() +
                "Gaupe{" +
                "øretustLengde=" + øretustLengde +
                '}';
    }
}
