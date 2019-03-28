package dispatch;

import java.util.Arrays;
import java.util.function.Supplier;
import java.util.stream.Stream;
/* Clase principal desde la que invocamos todos los algoritmos, para facilitar la integración 
*  todos se invocan como despachadores(clase Despachador), esta clase proveé un acceso global a 
*  la lista de procesos en modo Stream así como al tiempo del sistema y el número de procesos
*  en la lista.
*/
public class Sistema{
    public static final int NUMEROPROC=10; //Numero de procesos en el sistema
    public static float tiempoSist=0; //Tiempo del sistema, debe actualizarse al terminar un proceso o un quantum
    private static Proceso[] listaProc=null; //Lista de procesos
    private static float tiempoTotal; //Tiempo total de ejecución de los procesos
    private static Despachador[] opc=null; //Lista de algoritmos despachadores
    public static Supplier<Stream<Proceso>> streamSupplier; //Stream de procesos a través del cuál accedemos a la lista de procesos.
    
    public static void main(String[] args){
        opc = new Despachador[3];
        opc[0]=new Fifo();
        opc[1]=new Spn();
        opc[2]=new RoundRobin(1);
        for(Despachador despachador : opc){ //Recorremos todos los algoritmos invocados
            System.out.println("\t\t\t"+despachador.getClass().toString()); //Nombre del algoritmo
            int j=4;
            for(int count=0; count<j; count++){ //Número de rondas de cada Algoritmo.
                Proceso p = null;
                listaProc = new Proceso[NUMEROPROC];
                for(int i=0;i<NUMEROPROC;i++){ //Creamos n procesos con tiempos variables en cada ronda y además con tiempos de coma flotante
                    p = new Proceso();
                    p.setNombre(i+1);
                    p.setTiempoEjecucion((float)(Math.random()*10)+1);
                    p.setTiempoLlegada((float)(tiempoSist+Math.random()));
                    listaProc[i] = p;
                }
                streamSupplier = () ->Stream.of(listaProc);//Creamos el acceso a la lista de procesos (reutilizable)
                System.out.println("\t-->Ronda "+(count+1));
                streamSupplier.get().forEach(z -> {
                    System.out.print("Proceso "+z.getNombre()+" ,");
                    System.out.print("t="+z.getTiempoEjecucion()+"; ");
                    tiempoTotal+=z.getTiempoEjecucion();
                });
                System.out.println("Tiempo total:"+tiempoTotal);
                despachador.atiende(); //Atendemos a los procesos
                tiempoSist=0;
                tiempoTotal=0;
            }
            System.out.println();
        }
    }
}
