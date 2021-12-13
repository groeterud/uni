public class Speilløst extends Kamera{
    private int søkeroppløsning;

    public Speilløst(int serienummer, String fabrikat, String modell, int megapixler, int søkeroppløsning) {
        super(serienummer, fabrikat, modell, megapixler);
        this.søkeroppløsning = søkeroppløsning;
    }

    public int getSøkeroppløsning() {
        return søkeroppløsning;
    }

    public void setSøkeroppløsning(int søkeroppløsning) {
        this.søkeroppløsning = søkeroppløsning;
    }
}
