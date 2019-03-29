/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package comp;

/**
 * @version 0.1
 * @author Luis
 */
public abstract class PlatilloHorneable {
    private String nombre;
    private float tiempo;
    private int volumen;

    public int getVolumen() {
        return volumen;
    }

    public void setVolumen(int volumen) {
        this.volumen = volumen;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public float getTiempo() {
        return tiempo;
    }

    public void setTiempo(float tiempo) {
        this.tiempo = tiempo;
    }
    
    public void disminuyeTick(){
        float aux=this.tiempo-1;
        if(aux>0){
            this.tiempo-=1;
        }
        else
            this.tiempo=0;
    }

    @Override
    public String toString() {
        return this.getNombre()+"\tTiempo de prep: "+Float.toString(this.tiempo)+"\tVolumen: "+Integer.toString(this.volumen);
    }
    
}
