/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package comp;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @version 0.1
 * @author Luis
 */
public class Horno {
    
    private int capacidad;
    private String nombre;
    private static int count;
    private List<PlatilloHorneable> platillos;

    public Horno(int capacidad) {
        nuevo();
        this.capacidad=capacidad;
        this.nombre="Horno "+Integer.toString(count);
        System.out.println(this.nombre+" con capacidad de:"+this.capacidad);
    }
    
    public synchronized void atiende(){
        for(PlatilloHorneable platillo : platillos){
            if(platillo.getTiempo()>0){
                platillo.disminuyeTick();
            }
            else
                platillos.remove(platillo);
        }
    }
    
    public List<PlatilloHorneable> getPlatillos() {
       return platillos;
    }
    
    private int calculateVolume(){
        int x = 0;
        for(PlatilloHorneable platillo : platillos) {
            x+=platillo.getVolumen();
        }
        return x;
    }
    
    public void setPlatillos(PlatilloHorneable[] platillos) {
        this.platillos = new ArrayList<>(Arrays.asList(platillos));
    }
    
    public synchronized void addPlatillo(PlatilloHorneable platillo){
        this.platillos.add(platillo);
    }
    
    public synchronized int getCapacidad() {
        return capacidad-calculateVolume();
    }

    public synchronized String getNombre() {
        return nombre;
    }
    
    private synchronized void nuevo(){
        Horno.count+=1;
    }
    
    public synchronized void resetContador(){
        Horno.count=0;
    }
}
