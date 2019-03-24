package dispatch;
/* Interfaz que nos proveé el comportamiento estándar de
*  los algoritmos para despachar procesos, si se necesitan agregar
*  nuevos algoritmos se debe formar un nuevo contrato para evitar 
*  romper el código del sistema principal.
*/
public interface Despachador{
    public void atiende();
}
