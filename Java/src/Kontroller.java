/*
All programlogikk
 */
public class Kontroller {

    public String dikt_enkel(String[] ord) {
        String dikt="";
        // for løkke for hver linje
        for (int i = 0; i < 4; i++) {
            //for løkke for hvert ord i linjen
            for (int j = 0; j < 4; j++) {
                int tilfeldigtall = (int)(Math.random()*ord.length);
                dikt+=ord[tilfeldigtall]+" ";
            }
            dikt+="\n";
        }
        return dikt;
    }
    // Henter inn hver kategori som eget string-array
    public String dikt_avansert(String[] artikkel, String[] adjektiv,String[] substantiv, String[] verb) {
        String dikt="";
        int tilfeldigtall=0;
        //for løkke for linjene
        for (int i = 0; i < 4; i++) {
            //for løkke for ordene
            for (int j = 0; j < 4; j++) {
                if (i!=3) { // for de 3 første linjene
                    switch (j) {
                        case 0:
                                tilfeldigtall = (int) (Math.random() * artikkel.length);
                                dikt += artikkel[tilfeldigtall] + " ";
                            break;
                        case 1:
                                tilfeldigtall = (int) (Math.random() * adjektiv.length);
                                dikt += adjektiv[tilfeldigtall] + " ";
                            break;
                        case 2:
                                tilfeldigtall = (int) (Math.random() * substantiv.length);
                                dikt += substantiv[tilfeldigtall] + " ";
                            break;
                        case 3:
                                tilfeldigtall = (int) (Math.random() * verb.length);
                                dikt += verb[tilfeldigtall] + " ";
                            break;
                    } // slutt switch
                } // slutt if
                else { // siste linje
                    switch (j) {
                        case 0:
                            tilfeldigtall = (int)(Math.random()*verb.length);
                            dikt+=verb[tilfeldigtall]+" ";
                            break;
                        case 1:
                            tilfeldigtall = (int)(Math.random()*artikkel.length);
                            dikt+=artikkel[tilfeldigtall]+" ";
                            break;
                        case 2:
                            tilfeldigtall = (int)(Math.random()*adjektiv.length);
                            dikt+=adjektiv[tilfeldigtall]+" ";
                            break;
                        case 3:
                            tilfeldigtall = (int)(Math.random()*substantiv.length);
                            dikt+=substantiv[tilfeldigtall]+"?";
                            break;
                    }// slutt switch
                }// slutt else
            }// slutt indre for
            dikt+="\n"; // ikke glem linjeskift
        } // slutt ytre for
        return dikt;
    } // slutt dikt_avansert
}