/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


/**
 *
 * @author sandy
 */
public class ServiciosCuentaBancaria implements Runnable{
    private CuentaBancaria acct = new CuentaBancaria(80);
 
    public static void main(String[] args) {
 
        ServiciosCuentaBancaria r = new ServiciosCuentaBancaria();
        Thread one = new Thread(r);
        Thread two = new Thread(r);
        one.setName("Francisco");
        two.setName("Hortensia");
        one.start();
        two.start();
    }
 
    public void run() {
        realizarRetiro(50);
        if (acct.getBalance() < 0) {
            System.out.println("Cuenta Sobregirada! " + acct.getBalance());
        }
    }
 
    private void realizarRetiro(int amt) {
        synchronized(this){
        if (acct.getBalance() >= amt) {
            System.out.println(Thread.currentThread().getName() + " esta por realizar un retiro por:$"+amt);
                acct.retirar(amt);
                System.out.println(Thread.currentThread().getName() + " completó el retiro,el balance de la cuenta es:"+acct.getBalance());
            } else {
                System.out.println("No hay suficiente dinero para que " + Thread.currentThread().getName() + " realice el retiro"
                        + acct.getBalance());
            }
        }
    }
    public class CuentaBancaria{
    private int balance;
 
    CuentaBancaria(int balanceInicial) {
        this.balance = balanceInicial;
    }
 
    int getBalance() {
        return balance;
    }
 
    void retirar(int cantidad) {
        balance = balance - cantidad;
    }


}

}


