/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package comp;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * @version 0.1
 * @author Luis
 */
public class Sistema {
    private static float tiempoSistema;
    private static List<PlatilloHorneable> cola;
    public static int numPlatillos;
    private static Sistema instance;
    private static List<Horno> hornos;
    private static List<EstacionDeCocina> estaciones;

    private Sistema(int numPlatillos) {
        Sistema.tiempoSistema=0;
        cola = new ArrayList<>();
        hornos = new ArrayList<>();
        estaciones = new ArrayList<>();
        Sistema.numPlatillos = numPlatillos ;
    }

    public static Sistema getInstance(int numPlatillos){
        synchronized(Sistema.class){
            if(Sistema.instance == null){
                instance = new Sistema(numPlatillos);
            }
        }
        return instance;
    }
    
    public void atiende(){
        while(!cola.isEmpty()){
            for(Horno horno : hornos){
                horno.atiende();
                for(PlatilloHorneable platillo : cola){
                    if(platillo.getVolumen()<=horno.getCapacidad()){
                        horno.addPlatillo(platillo);
                        cola.remove(platillo);
                        System.out.println(platillo.getNombre()+" entra a "+horno.getNombre());
                    }
                    else
                        System.out.println(platillo.getNombre()+" espera por espacio en algún horno");
                }
            }
        }
    }
    
    public void trabajaEstaciones(){
        for(EstacionDeCocina estacion : estaciones){
            estacion.start();
        }
    }
    
    public void creaHornos(){
        Scanner sc=new Scanner(System.in);
        System.out.println("Ahora proporcioname el numero de hornos(agentes de atención de la cola de espera)");
        int n = sc.nextInt();
        for(int i=0; i<n; i++){
            Sistema.hornos.add(new Horno(25));
        }
    }
    
    public void creaEstaciones(){
        Scanner sc=new Scanner(System.in);
        System.out.println("Ahora proporcioname el numero de estaciones de trabajo cocinando(hilos que agregan platillos)");
        int n = sc.nextInt();
        for(int i=0; i<n; i++){
            Sistema.estaciones.add(new EstacionDeCocina("Estacion "+Integer.toString(i)));
        }
    }

    public static void agregaPlatillo(PlatilloHorneable platillo){
        cola.add(platillo);
    }
    
    public synchronized float getTiempoSistema() {
        return tiempoSistema;
    }

    public synchronized void aumentaTiempoSistema(){
        Sistema.tiempoSistema+=1;
    }
}
