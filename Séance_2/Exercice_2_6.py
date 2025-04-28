import numpy as np
import matplotlib.pyplot as plt

R = 220
C = 1*10**(-6)

fc = 1 / (2 * np.pi * R * C)

frequencies = np.logspace(1, 6, 500)
omega = 2*np.pi*frequencies

#fonction transfert
H = 1/(1+1j*omega*R*C)
#gain en dB
gain = 20*np.log10(np.abs(H))
#phase en degrés
phase = np.angle(H, deg=True)
# Tracé du diagramme de Bode
plt.figure(figsize=(12, 8))

# Gain (Magnitude)
plt.subplot(2, 1, 1)
plt.semilogx(frequencies, gain)
plt.title('Diagramme de Bode du filtre passe-bas RC')
plt.ylabel('Gain (dB)')
plt.grid(which='both', linestyle='--', linewidth=0.5)
# Marquer la fréquence de coupure
plt.plot(fc, -3, 'r*', markersize=15, label=f"f_c = {fc:.2f} Hz")
plt.legend()

# Phase
plt.subplot(2, 1, 2)
plt.semilogx(frequencies, phase)
plt.xlabel('Fréquence (Hz)')
plt.ylabel('Phase (°)')
plt.grid(which='both', linestyle='--', linewidth=0.5)
# Marquer la fréquence de coupure
plt.plot(fc, -45, 'r*', markersize=15, label=f"f_c = {fc:.2f} Hz")
plt.legend()

plt.tight_layout()
plt.show()
