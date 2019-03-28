package dispatch;

import java.util.Comparator;
/* Clase del algoritmo de "Primero llegado, primero servido"
*  se utiliza un flujo de datos dada la facilidad del problema.
*
*/

public class Fifo implements Despachador{
    
    public float tiempoEjecucion=0;
    public float tiempoRespuesta=0;
    public float radioPenalizacion=0;
    public float tiempoEspera=0;
    public float proporcionRespuesta=0;

    @Override
    public void atiende() {
        Sistema.streamSupplier.get().sorted(Comparator.comparing(Proceso::getTiempoLlegada)).forEach(
            p -> {
                Sistema.tiempoSist+=p.getTiempoEjecucion();
                p.setTiempoInactivo(Sistema.tiempoSist-p.getTiempoLlegada());
                p.setTiempoRespuesta();
                p.setRadioPenalizacion();
                p.setProporcionRespuesta();
                p.setTiempoEspera();
                this.tiempoEjecucion+=p.getTiempoEjecucion();
                this.radioPenalizacion+=p.getRadioPenalizacion();
                this.proporcionRespuesta+=p.getProporcionRespuesta();
                this.tiempoEspera+=p.getTiempoEspera();
                this.tiempoRespuesta+=p.getTiempoRespuesta();
            }
        );
        this.tiempoEjecucion=this.tiempoEjecucion/Sistema.NUMEROPROC;
        this.radioPenalizacion=this.radioPenalizacion/Sistema.NUMEROPROC;
        this.proporcionRespuesta=this.proporcionRespuesta/Sistema.NUMEROPROC;
        this.tiempoEspera=this.tiempoEspera/Sistema.NUMEROPROC;
        this.tiempoRespuesta=this.tiempoRespuesta/Sistema.NUMEROPROC;
        System.out.print("\tºº:\tT="+this.tiempoRespuesta);
        System.out.print("\tE="+this.tiempoEspera);
        System.out.print("\tP="+this.radioPenalizacion);
        System.out.print("\tR="+this.proporcionRespuesta);
        System.out.print("\tt="+this.tiempoEjecucion+"\n");
    }
    
}
