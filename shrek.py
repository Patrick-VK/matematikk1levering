import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

Mtemp = np.array([76.8,73.9,72.3,71.9,69.9,68.7,66.7,64.7,
63.5,62.3,60.9,59.7,58.5,57.3,56.5,55.7,54.5,53.7,52.5,
51.7,51.2,50.8,50,49.2,48.4,47.6,47.2,46.8,46,45.2,44.8,
44.4,44,43.6,43.2,42.5,41.6,41.2,40.8,40.8,40.1,40.1,39.7,
38.9,38.5,38.5,38.1,37.7,37.3,36.9,36.9,36.3,36.3,35.9,35.5,
35.5,35.1,34.7,34.7,34.3,33.9,33.7,33.7,33.3,32.9,32.9,32.9,
32.5,32.5,32.1,31.7,31.4,31.4,31.4,31,31,31,30.6,30.6,30.6,
30.2,30,30,30,29.8,29.4,29.4,29.4,29,29
])
tid = np.linspace(0, 90, 90)

t_k = 23.1
t_0 = Mtemp[0]

def teoretiskModell(t, t0, a):
    return t_k+(t0-t_k)*np.exp(-a*t)



##Vi finner a ved å bruke regresjon, her cruvefit. Denne funksjonen lager en modell etter ae^(alpha*t)
popt, pcov = curve_fit(lambda t, a: teoretiskModell(t, t_0, a), tid, Mtemp)
Ttemp = teoretiskModell(tid, t_0, popt[0])

print("Avkjølingskonstanten er: ")
print(popt[0])

plt.plot(tid,Mtemp, label=f"Målte temperaturer")
plt.plot(tid, Ttemp, label=f"Teoretisk modell, alpha er {popt[0]}")
plt.xlabel("Tid")
plt.ylabel("Temperatur")
plt.legend()
plt.grid()
plt.show()
