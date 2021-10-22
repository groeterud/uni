import javax.swing.*;
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

    public String printGauper() {
        ArrayList<ArrayList<Object>> fangstHistorikk;
        String print="Alle gauper vi har fanget\n\n";
        //for hver gaupe
        for (int i = 0; i < gauper.size(); i++) {
            Gaupe g = gauper.get(i);
            fangstHistorikk=g.getFangstHistorikk();
            print+="Gaupe:"+g.getIdentifikator()+", kjønn:"+g.getKjønn()+":\n";
            print+="Fangsthistorikk:\n";
            //går gjennom fangsthistorikken
            for (int j = 0; j < fangstHistorikk.size(); j++) {
                ArrayList<Object> fangst=fangstHistorikk.get(j);
                print+="Dato:"+fangst.get(0)+"\t\t Sted:"+fangst.get(1)+"\t\t Lengde:"+fangst.get(2)+"\t\t Vekt:"+fangst.get(3)+"\t\t Øretust:"+fangst.get(4)+"\n";
            }
            print+="\n";
        }
        return print;
    }
    public String printHarer() {
        ArrayList<ArrayList<Object>> fangstHistorikk;
        String print="Alle harer vi har fanget\n\n";
        //for hver hare
        for (int i = 0; i < harer.size(); i++) {
            Hare h = harer.get(i);
            fangstHistorikk=h.getFangstHistorikk();
            print+="Hare:"+h.getIdentifikator()+", kjønn:"+h.getKjønn()+", type:"+h.getHareType()+"\n";
            print+="Fangsthistorikk:\n";
            //går gjennom fangsthistorikken
            for (int j = 0; j < fangstHistorikk.size(); j++) {
                ArrayList<Object> fangst=fangstHistorikk.get(j);
                print+="Dato:"+fangst.get(0)+"\t\t Sted:"+fangst.get(1)+"\t\t Lengde:"+fangst.get(2)+"\t\t Vekt:"+fangst.get(3)+"\t\t Pelsfarge:"+fangst.get(4)+"\n";
            }
            print+="\n";
        }
        return print;
    }
    public String printDyr(String id) {
        Dyr d = finnDyr(id);
        if (d != null) {
            ArrayList<ArrayList<Object>> fangstHistorikk = d.getFangstHistorikk();
            String print="";
            if (d instanceof Gaupe) {
                print+="Gaupe:"+d.getIdentifikator()+", kjønn:"+d.getKjønn()+":\n";
                print+="Fangsthistorikk:\n";
                //går gjennom fangsthistorikken
                for (int j = 0; j < fangstHistorikk.size(); j++) {
                    ArrayList<Object> fangst=fangstHistorikk.get(j);
                    print+="Dato:"+fangst.get(0)+"\t\t Sted:"+fangst.get(1)+"\t\t Lengde:"+fangst.get(2)+"\t\t Vekt:"+fangst.get(3)+"\t\t Øretust:"+fangst.get(4)+"\n";
                }
            }
            else if (d instanceof Hare){
                print+="Hare:"+d.getIdentifikator()+", kjønn:"+d.getKjønn()+", type:"+ ((Hare) d).getHareType()+"\n";
                print+="Fangsthistorikk:\n";
                for (int j = 0; j < fangstHistorikk.size(); j++) {
                    ArrayList<Object> fangst=fangstHistorikk.get(j);
                    print+="Dato:"+fangst.get(0)+"\t\t Sted:"+fangst.get(1)+"\t\t Lengde:"+fangst.get(2)+"\t\t Vekt:"+fangst.get(3)+"\t\t Pelsfarge:"+fangst.get(4)+"\n";
                }
            }
            return print;
        }
        else return "Fant ikke dyret";
    }
    public String printAlleDyr() {
        ArrayList<ArrayList<Object>> fangstHistorikk;
        String print="Alle dyr vi har fanget\n";
        //for hver gaupe
        for (int i = 0; i < gauper.size(); i++) {
            Gaupe g = gauper.get(i);
            fangstHistorikk=g.getFangstHistorikk();
            print+="Gaupe:"+g.getIdentifikator()+", kjønn:"+g.getKjønn()+":\n";
            print+="Fangsthistorikk:\n";
            //går gjennom fangsthistorikken
            for (int j = 0; j < fangstHistorikk.size(); j++) {
                ArrayList<Object> fangst=fangstHistorikk.get(j);
                print+="Dato:"+fangst.get(0)+"\t\t Sted:"+fangst.get(1)+"\t\t Lengde:"+fangst.get(2)+"\t\t Vekt:"+fangst.get(3)+"\t\t Øretust:"+fangst.get(4)+"\n";
            }
            print+="\n";
        }
        //for hver hare
        for (int i = 0; i < harer.size(); i++) {
            Hare h = harer.get(i);
            fangstHistorikk=h.getFangstHistorikk();
            print+="Hare:"+h.getIdentifikator()+", kjønn:"+h.getKjønn()+", type:"+h.getHareType()+"\n";
            print+="Fangsthistorikk:\n";
            //går gjennom fangsthistorikken
            for (int j = 0; j < fangstHistorikk.size(); j++) {
                ArrayList<Object> fangst=fangstHistorikk.get(j);
                print+="Dato:"+fangst.get(0)+"\t\t Sted:"+fangst.get(1)+"\t\t Lengde:"+fangst.get(2)+"\t\t Vekt:"+fangst.get(3)+"\t\t Pelsfarge:"+fangst.get(4)+"\n";
            }
            print+="\n";
        }
        return print;
    }

}
