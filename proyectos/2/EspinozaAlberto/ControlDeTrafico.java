import java.util.Random;
import java.util.concurrent.*;
import java.util.concurrent.locks.*;

public class ControlDeTrafico {


	private final Lock pistaOcupada = new ReentrantLock(true);
// Se usa para imponer la exclusión mutua para adquirir y liberar pistas

	Condition pisDispo = pistaOcupada.newCondition();
	private final Semaphore listaDePistas[] = new Semaphore[PistasAeropuerto.PISTAS_NUM];

	private static final int MAX_TIEMPO = 50; 
   
	private static final int MAX_ESPERA = 250; 
 
	private static Random r = new Random(0);
   
	public ControlDeTrafico() {
		for (int i = 0; i < PistasAeropuerto.PISTAS_NUM; i++) {
			listaDePistas[i] = new Semaphore(1, true);
		}

	} 

	// Llamado por un avión cuando desea aterrizar en una pista
	public void pistaResevada(int avionNumero, int pista) {


		pistaOcupada.lock();

		System.out.println("avion #" + avionNumero+1 + " esta adquiriendo la pista :"
				+ PistasAeropuerto.nombPista(pista));
		
		

		while (listaDePistas[pista].availablePermits() == 0) {
			try {
				pisDispo.signal();
				pisDispo.await();

			} catch (InterruptedException e) { 
				e.printStackTrace();
			}
		} 

		
		if (pista == PistasAeropuerto.PISTA_A) {

			while ((listaDePistas[PistasAeropuerto.PISTA_E].availablePermits() == 0
					|| listaDePistas[PistasAeropuerto.PISTA_F].availablePermits() == 0)
					|| listaDePistas[PistasAeropuerto.PISTA_A].availablePermits() == 0) {
				try {
					pisDispo.signal();
					pisDispo.await();
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}

			try {

				listaDePistas[pista].acquire();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}

		} 

		if (pista == PistasAeropuerto.PISTA_B) {

			while ((listaDePistas[PistasAeropuerto.PISTA_E].availablePermits() == 0
					|| listaDePistas[PistasAeropuerto.PISTA_F].availablePermits() == 0
					|| listaDePistas[PistasAeropuerto.PISTA_C].availablePermits() == 0)
					|| listaDePistas[PistasAeropuerto.PISTA_B].availablePermits() == 0) {
				try {
					pisDispo.signal();
					pisDispo.await();
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}

			try {

				listaDePistas[pista].acquire();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}

		}

		if (pista == PistasAeropuerto.PISTA_C) {

			while ((listaDePistas[PistasAeropuerto.PISTA_B].availablePermits() == 0
					|| listaDePistas[PistasAeropuerto.PISTA_F].availablePermits() == 0)
					|| listaDePistas[PistasAeropuerto.PISTA_C].availablePermits() == 0) {
				try {
					pisDispo.signal();
					pisDispo.await();
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}

			try {

				listaDePistas[pista].acquire();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		} 

		if (pista == PistasAeropuerto.PISTA_D) {
			while (listaDePistas[PistasAeropuerto.PISTA_D].availablePermits() == 0) {
				try {
					pisDispo.signal();
					pisDispo.await();
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}

			try {

				listaDePistas[pista].acquire();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		} 


		if (pista == PistasAeropuerto.PISTA_E) {

			while ((listaDePistas[PistasAeropuerto.PISTA_A].availablePermits() == 0
					|| listaDePistas[PistasAeropuerto.PISTA_B].availablePermits() == 0)
					|| listaDePistas[PistasAeropuerto.PISTA_E].availablePermits() == 0) {
				try {
					pisDispo.signal();
					pisDispo.await();
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}

			try {

				listaDePistas[pista].acquire();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}


		if (pista == PistasAeropuerto.PISTA_F) {

			while ((listaDePistas[PistasAeropuerto.PISTA_A].availablePermits() == 0
					|| listaDePistas[PistasAeropuerto.PISTA_B].availablePermits() == 0
					|| listaDePistas[PistasAeropuerto.PISTA_C].availablePermits() == 0)
					|| listaDePistas[PistasAeropuerto.PISTA_F].availablePermits() == 0) {
				try {
					pisDispo.signal();
					pisDispo.await();
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}

			try {

				listaDePistas[pista].acquire();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}

		} 
		PistasAeropuerto.checkAirportStatus(pista);

		pistaOcupada.unlock(); 

		
		int taxiTime = r.nextInt(MAX_TIEMPO);
		System.out.println("avion #" + avionNumero + " esta en la pista " + PistasAeropuerto.nombPista(pista)
				+ " por " + taxiTime + " minutos");
		try {
			Thread.sleep(taxiTime);
		} catch (InterruptedException ex) {
			System.out.println("avion #" + avionNumero + ", pista " + PistasAeropuerto.nombPista(pista)
					+ ": fue despertado");
		}

	} 


	public void liberaPista(int avionNumero, int pista) {


		pistaOcupada.lock(); 
   

		System.out.println("avion #" + avionNumero + " esta liberando la pista despues de aterrizar en "
				+ PistasAeropuerto.nombPista(pista));

		listaDePistas[pista].release();
		pisDispo.signalAll();

   // Actualizar el estado del aeropuerto para indicar que el aterrizaje esta completo
		PistasAeropuerto.desocupoP(pista);

		pistaOcupada.unlock(); 


		int espera = r.nextInt(MAX_ESPERA);
		System.out.println(
				"avion #" + avionNumero + " esta esperando por " + espera + " minutos antes de despegar de nuevo");
		try {
			Thread.sleep(espera);
		} catch (InterruptedException ex) {
			System.out.println("avion #" + avionNumero + ": WaitTime Sleep fue interrumpido");
		}

	} 

}