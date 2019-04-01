import java.util.HashMap;
import java.util.Map;

public final class PistasAeropuerto {
	
	public static final int PISTAS_NUM = 6; // Número de pistas en esta simulación
	
	public static final int AVIONES_NUM = 7; // Número de aviones en esta simulación.
	
	public static final int PETICIONES = 6; //Número máximo de solicitudes de aterrizaje simultáneas
	
	public static final int PISTA_A = 0;
	public static final int PISTA_B = 1;
	public static final int PISTA_C = 2;
	public static final int PISTA_D = 3;
	public static final int PISTA_E = 4;
	public static final int PISTA_F = 5;


	

	private static int[] pistaEnUso = new int[PISTAS_NUM]; // realiza un seguimiento de cuántos aviones están intentando aterrizar en una pista dada
	private static int numSolicitudes = 0; //Realiza un seguimiento del número de solicitudes de aterrizaje simultáneas
   	
	public static final Map<Integer, String> mapPista = createRunwayHashmap();

	private static Map<Integer, String> createRunwayHashmap() {
		Map<Integer, String> map = new HashMap<Integer, String>();

		map.put(PISTA_A, "A");
		map.put(PISTA_B, "B");
		map.put(PISTA_C, "C");
		map.put(PISTA_D, "D");
		map.put(PISTA_E, "E");
		map.put(PISTA_F, "F");

		return map;
	} 
	public static String nombPista(int numPist) {
		if (mapPista.containsKey(numPist)) {
			return mapPista.get(numPist);
		} else {
			return "Pista desconocida " + numPist;
		}
	} 

	public synchronized static void solicitudP(int numPist) {
		pistaEnUso[numPist]++;
		numSolicitudes++;
	} 

	public synchronized static void desocupoP(int numPist) {
		pistaEnUso[numPist]--;
		numSolicitudes--;
	} 

// Comprobar el estado del aeropuerto 

	public synchronized static void checkAirportStatus(int pistaSolicitada) {
		boolean crash = false; 
		System.out.println("\nComprobando el estado del aeropuerto y la pista: " + nombPista(pistaSolicitada) + "...");
      	System.out.println("");
		solicitudP(pistaSolicitada);
		System.out.println("Numero de solicitudes de aterrizaje simultaneas == " + numSolicitudes);
     	 System.out.println("");
		if (numSolicitudes > PETICIONES) {
			System.out.println("***** El numero de solicitudes de aterrizaje simultaneas excede el limite de Control de trafico aereo de "
					+ PETICIONES + "!");
			crash = true;
		}
		for (int i = 0; i < PISTAS_NUM; i++) {
			System.out.println("Numero de aviones que aterrizan en la pista." + nombPista(i) + " == " + pistaEnUso[i]);
			if (pistaEnUso[i] > 1) {
				System.out.println(
						"***** El numero de aviones que aterrizan en la pista. " + nombPista(i) + " es mayor que 1!");
				crash = true;
			}
		}
		if (crash) {
			System.out.println(
					"*****¡CHOQUE! Una o más reglas han sido violadas. Debido al accidente, el aeropuerto está cerrado!");
			System.exit(-1); 
		}
		System.out.println("Verificacion de estado completa, sin violacion de reglas (:D)\n");

	} 

} 
