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
public class Pastel extends PlatilloHorneable{
    private static int count;

    public Pastel(float tiempo, int volumen) {
        nuevo();
        this.setNombre("Pastel "+Integer.toString(count));
        this.setTiempo(tiempo);
        this.setVolumen(volumen);
    }
    
    private synchronized void nuevo(){
        Pastel.count+=1;
    }
    
    public synchronized void resetContador(){
        Pastel.count=0;
    }
}
