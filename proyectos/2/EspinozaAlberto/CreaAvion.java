public class CreaAvion implements Runnable {
	private Avion avion;

	public CreaAvion(Avion avion) {
		this.avion = avion;
	}

	@Override
	public void run() {
		this.avion.aterrizar();

	} 

} 