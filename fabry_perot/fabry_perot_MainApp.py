import numpy as np
import matplotlib.pyplot as plt

r = 0.94  # reflection coefficient
F = (2*r/(1-r**2))**2

delta = np.linspace(-3*np.pi, 3*np.pi, 121)

# without metallic coating on surface of etalon
F1 = (F*(np.sin(delta/2)*np.sin(delta/2)))
I_tran = 1/(1+F1)
I_reflection = F1/(1+F1)
#print("Ireflection",I_reflection)


fig = plt.figure(figsize=(6, 6))
ax =fig.add_subplot(111)
ax.plot(delta, I_tran, label="transmitted")
ax.plot(delta, I_reflection, label="reflected")
fig.legend()
ax.set_title("Fabry-Perot Interferometer's Transmission Function")
ax.set_ylabel("I_t/I_in")
ax.set_xlabel("Angle in radians")
plt.show()
fig.legend()