package dispatch;

public class Proceso{
    private int nombre;

    public int getNombre() {
        return nombre;
    }

    public void setNombre(int nombre) {
        this.nombre = nombre;
    }
    private float tiempoInactivo;
    private float tiempoLlegada;
    private float tiempoEjecucion;
    private float tiempoRespuesta;
    private float radioPenalizacion;
    private float tiempoEspera;
    private float proporcionRespuesta;
    
    public Proceso(){
        tiempoInactivo=0;
        tiempoLlegada=0;
        tiempoEjecucion=0;
        tiempoRespuesta=tiempoEjecucion+tiempoInactivo;
        radioPenalizacion=tiempoRespuesta/tiempoEjecucion;
        tiempoEspera=tiempoRespuesta-tiempoEjecucion;
        proporcionRespuesta=(1/radioPenalizacion);
    }

    public float getTiempoInactivo() {
        return tiempoInactivo;
    }

    public void setTiempoInactivo(float tiempoInactivo) {
        this.tiempoInactivo = tiempoInactivo;
    }

    public float getTiempoLlegada() {
        return tiempoLlegada;
    }

    public void setTiempoLlegada(float tiempoLlegada) {
        this.tiempoLlegada = tiempoLlegada;
    }

    public float getTiempoEjecucion() {
        return tiempoEjecucion;
    }

    public void setTiempoEjecucion(float tiempoEjecucion) {
        this.tiempoEjecucion = tiempoEjecucion;
    }

    public float getTiempoRespuesta() {
        return tiempoRespuesta;
    }

    public void setTiempoRespuesta() {
        this.tiempoRespuesta = tiempoEjecucion+tiempoInactivo;
    }

    public float getRadioPenalizacion() {
        return radioPenalizacion;
    }

    public void setRadioPenalizacion() {
        this.radioPenalizacion = tiempoRespuesta/tiempoEjecucion;
    }

    public float getTiempoEspera() {
        return tiempoEspera;
    }

    public void setTiempoEspera() {
        this.tiempoEspera = tiempoRespuesta-tiempoEjecucion;
    }

    public float getProporcionRespuesta() {
        return proporcionRespuesta;
    }

    public void setProporcionRespuesta() {
        this.proporcionRespuesta = (1/radioPenalizacion);
    }

}