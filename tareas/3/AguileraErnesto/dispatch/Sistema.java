package dispatch;

import java.util.Arrays;
import java.util.function.Supplier;
import java.util.stream.Stream;

public class Sistema{
    public static final int NUMEROPROC=10;
    public static float tiempoSist=0;
    private static Proceso[] listaProc=null;
    private static float tiempoTotal;
    private static Despachador[] opc=null;
    public static Supplier<Stream<Proceso>> streamSupplier;
    
    public static void main(String[] args){
        opc = new Despachador[3];
        opc[0]=new Fifo();
        opc[1]=new Spn();
        opc[2]=new RoundRobin(1);
        for(Despachador despachador : opc){
            System.out.println("\t\t\t"+despachador.getClass().toString());
            int j=4;
            for(int count=0; count<j; count++){
                Proceso p = null;
                listaProc = new Proceso[NUMEROPROC];
                //System.out.print(listaProc);
                for(int i=0;i<NUMEROPROC;i++){
                    p = new Proceso();
                    p.setNombre(i+1);
                    p.setTiempoEjecucion((float)(Math.random()*10)+1);
                    p.setTiempoLlegada((float)(tiempoSist+Math.random()));
                    //tiempoSist+=p.getTiempoLlegada();
                    listaProc[i] = p;
                    //System.out.println(p.getTiempoLlegada());
                }
                streamSupplier = () ->Stream.of(listaProc);
                System.out.println("\t-->Ronda "+(count+1));
                streamSupplier.get().forEach(z -> {
                    System.out.print("Proceso "+z.getNombre()+" ,");
                    System.out.print("t="+z.getTiempoEjecucion()+"; ");
                    tiempoTotal+=z.getTiempoEjecucion();
                });
                System.out.println("Tiempo total:"+tiempoTotal);
                despachador.atiende();
                tiempoSist=0;
                tiempoTotal=0;
            }
            System.out.println();
        }
    }
}