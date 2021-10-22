import java.util.ArrayList;
import java.util.Collections;

public class Kontroll {
    ArrayList<Gaupe> gauper = new ArrayList<>();
    ArrayList<Hare> harer = new ArrayList<>();

    public void nyGaupe(String kjønn, Double lengde, Double vekt, String tid, String sted, Double øretustLengde) {
        String id = "G"+Integer.toString(gauper.size()+1);
        Gaupe g = new Gaupe(id,kjønn,lengde,vekt,tid,sted,øretustLengde);
        gauper.add(g);
    }
    public void gjennFangstGaupe(String id,String tid,String sted, Double lengde, Double vekt, Double øretustLengde) {
        Gaupe gaupe = (Gaupe) finnDyr(id);
        gaupe.fangst(tid,sted,lengde,vekt,øretustLengde);
    }
    public void nyHare(String kjønn, Double lengde, Double vekt, String tid, String sted, String hareType, String pelsFarge) {
        String id = "H"+Integer.toString(harer.size()+1);
        Hare h = new Hare(id,kjønn,lengde,vekt,tid,sted,hareType,pelsFarge);
        harer.add(h);
    }
    public void gjennFangstHare(String id,String tid,String sted, Double lengde, Double vekt, String pelsFarge) {
        Hare hare = (Hare) finnDyr(id);
        hare.fangst(tid,sted,lengde,vekt,pelsFarge);
    }


    public Dyr finnDyr(String id) {
        Collections.sort(gauper);
        int index = Collections.binarySearch(gauper, new Gaupe(id,null,null,null,null,null,null));
        if (index>=0) return gauper.get(index);

        //linneær søk på harer da...
        for (int i = 0; i < harer.size(); i++) {
            Hare h = harer.get(i);
            if (h.getIdentifikator().equals(id)) return h;
        }
        //Fant ikke
        return null;
    }

    public void printGauper() {
        for (int i = 0; i < gauper.size(); i++) {
            Gaupe g = gauper.get(i);
            System.out.println(g);
        }
    }
    public void printHarer() {
        for (int i = 0; i < harer.size(); i++) {
            Hare h = harer.get(i);
            System.out.println(h);
        }
    }
    public void printDyr(String id) {
        Dyr d = finnDyr(id);
        if (d != null) System.out.println(d.toString());
        else System.out.println("Fant ikke dyret");
    }

}
