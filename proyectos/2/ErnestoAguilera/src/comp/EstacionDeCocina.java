/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package comp;

import java.util.Random;

/**
 * @version 0.1
 * @author Luis Aguilera
 */
public class EstacionDeCocina extends Thread {
    
    private PlatilloHorneable platillo;
    private Random rand;

    public EstacionDeCocina(String name){
        super(name);
        rand = new Random();
    }
    
    @Override
    public void run() {
        synchronized(Sistema.class){
            while(Sistema.numPlatillos>0){
                int x = rand.nextInt(100);
                if(x>0 && x<35){
                    this.platillo = new Pastel(2+3*rand.nextFloat(), rand.nextInt(5)+1);
                }else{
                    if(x>=35 && x<85){
                        this.platillo = new Pizza(3+3*rand.nextFloat(), rand.nextInt(3)+1);
                    }else{
                        if(x>=85 && x<100){
                            this.platillo = new Pavo(4+3*rand.nextFloat(), 2);
                        }
                    }
                }
                Sistema.agregaPlatillo(platillo);
                Sistema.numPlatillos-=1;
            }
        }
    }
    
}
