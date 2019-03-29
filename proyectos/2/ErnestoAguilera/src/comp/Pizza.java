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
public class Pizza extends PlatilloHorneable{
    private static int count;

    public Pizza(float tiempo, int volumen) {
        nuevo();
        this.setNombre("Pizza"+Integer.toString(count));
        this.setTiempo(tiempo);
        this.setVolumen(volumen);
    }
    
    private synchronized void nuevo(){
        Pizza.count+=1;
    }
    
    public synchronized void resetContador(){
        Pizza.count=0;
    }
}
