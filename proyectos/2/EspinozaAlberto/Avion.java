import java.util.Random;

public class Avion {
	private int AvionNum;
	private ControlDeTrafico controlDeTrafico;

	private int pistaSolicitada; 
	private static Random r = new Random(0);

	// constructor de  Avion 
	public Avion(int AvionNum, ControlDeTrafico controlDeTrafico) {
		this.AvionNum = AvionNum;
		this.controlDeTrafico = controlDeTrafico;

	} 

	// Método de colocación de la pista solicitada.
	public void  darPista (int pistaSolicitada) {
		this.pistaSolicitada = pistaSolicitada;
	}


	public void aterrizar() {
		while (true) {
			//listo para aterrizar
			pistaSolicitada = r.nextInt(PistasAeropuerto.PISTAS_NUM);
			controlDeTrafico.pistaResevada(AvionNum, pistaSolicitada);

			// aterrizaje completo
			controlDeTrafico.liberaPista(AvionNum, pistaSolicitada);

// Espere un momento en el suelo (para evitar la inanición de otros
// aviones)
			try {
				Thread.sleep(1000);
			} catch (InterruptedException ex) {
				System.out.println("avion #" + AvionNum + ": se interrumpió el sueño por prevencion de inanicion");
			}

		} 
	}
}  
