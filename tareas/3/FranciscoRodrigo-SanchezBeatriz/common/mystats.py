def estadisticas(tiempo_exe,espera,procesos):
    tiempo_total = [0]*len(tiempo_exe)
    for j in range(len(tiempo_exe)):
        tiempo_total[j] = tiempo_exe[j] + espera[j]

    print("T = "+ str(prom_t_total(tiempo_total)))
    print("E ="+str(prom_t_espera(espera)))
    print("P ="+str(round(prom_t_p(tiempo_total,tiempo_exe),3)))

def prom_t_total(tiempo_total):
    sum = 0
    for j in tiempo_total:
        sum += j
    return sum/len(tiempo_total)

def prom_t_espera(espera):
    sum = 0
    for j in espera:
        sum += j
    return sum/len(espera)

def prom_t_p(tiempo_total,tiempo_exe):
    sum = 0
    for i in range(len(tiempo_total)):
        sum += tiempo_total[i] / tiempo_exe[i]

    return sum / len(tiempo_total)
