package dispatch;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.Iterator;
import java.util.List;
import java.util.stream.Collectors;


public class RoundRobin implements Despachador{
    
    public float tiempoEjecucion=0;
    public float tiempoRespuesta=0;
    public float radioPenalizacion=0;
    public float tiempoEspera=0;
    public float proporcionRespuesta=0;
    private int quantum=0;
    private List<Proceso> procesos=null;
    
    public RoundRobin(int quantum){
        this.quantum=quantum;
    }

    @Override
    public void atiende() {
        float r=0;
        procesos=Sistema.streamSupplier.get().sorted(Comparator.comparing(Proceso::getTiempoLlegada)).collect(Collectors.toList());
        while(!procesos.isEmpty()){
            for(Iterator<Proceso> itr = procesos.iterator(); itr.hasNext();){
                Proceso p= itr.next();
                r=p.getTiempoEjecucion();
                if(Sistema.tiempoSist<p.getTiempoLlegada() && r<quantum){
                    Sistema.tiempoSist+=quantum;
                    this.tiempoEjecucion+=quantum;
                    r-=quantum;
                }else{
                    Sistema.tiempoSist+=quantum;
                    this.tiempoEjecucion+=quantum;
                    this.radioPenalizacion+=p.getRadioPenalizacion();
                    this.proporcionRespuesta+=p.getProporcionRespuesta();
                    this.tiempoEspera+=p.getTiempoEspera();
                    this.tiempoRespuesta+=p.getTiempoRespuesta();
                    itr.remove();
                }
            }
        }
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