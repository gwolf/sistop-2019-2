from threading import Semaphore
# varibles locales
turista_esp=0
turista_ing=0
lista_turista_esp=Semaphore(0)
lista_turista_ing=Semaphore(0)
total=4
mutex_guia=Semaphore(1)
