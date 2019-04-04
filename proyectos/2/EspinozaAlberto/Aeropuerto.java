public class Aeropuerto {

	public static void main(String[] args) {
   
		ControlDeTrafico controlDeTrafico = new ControlDeTrafico();

		Avion arAviones[] = new Avion[PistasAeropuerto.AVIONES_NUM];
		CreaAvion cola[] = new CreaAvion[PistasAeropuerto.AVIONES_NUM];
		Thread avionThre[] = new Thread[PistasAeropuerto.AVIONES_NUM];

// Crear y lanzar los hilos 
		for (int avionNum = 0; avionNum < PistasAeropuerto.AVIONES_NUM; avionNum++) {
			arAviones[avionNum] = new Avion(avionNum, controlDeTrafico);
			cola[avionNum] = new CreaAvion(arAviones[avionNum]);
			avionThre[avionNum] = new Thread(cola[avionNum]);
			avionThre[avionNum].start();
		}

	} 

}
