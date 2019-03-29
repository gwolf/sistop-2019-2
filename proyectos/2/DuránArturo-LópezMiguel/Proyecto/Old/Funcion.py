import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

dia_completo = 60*60*24

hora_pico1 = ((7*60)+30)*60
#desviacion = 0.39
funcion = st.norm(7.5,1.2)
funcion2 = st.norm(17.5,1.5)
#for t in range (0,24):
#print(t," :",funcion.pdf(t)+funcion2.pdf(t))

t = np.linspace(0, 24,24*2)

entreSemana = 1
finSemana = 0

desviacion  = 3.5
desviacion1 = 6

#3.5
#4.3
plt.plot(t,st.norm.pdf(t, 17.5, desviacion )  )
plt.show()
