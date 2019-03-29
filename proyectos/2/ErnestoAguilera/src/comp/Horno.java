/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package comp;

/**
 *
 * @author Luis
 */
public class Horno {
    
    private int capacidad;
    private String nombre;
    private static int count;

    public Horno(int capacidad) {
        nuevo();
        this.capacidad=capacidad;
        this.nombre="Horno "+Integer.toString(count);
    }
    
    public void atiende(){
        
    }
    
    private synchronized void nuevo(){
        Horno.count+=1;
    }
    
    public synchronized void resetContador(){
        Horno.count=0;
    }
}
