/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package comp;

import java.util.Scanner;

/**
 *
 * @author Luis
 */
public class Main {
    private static Scanner sc=new Scanner(System.in);
    public static void main(String[] args){
        System.out.println("Bienvenido al restaurante gerente");
        System.out.println("Para comenzar vamos a definir los parámetros de la simulación");
        System.out.println("Primero proporcioname el número de platillos que deseas crear en esta simulacion");
        Sistema singleton = Sistema.getInstance(sc.nextInt());
        
    }
}
