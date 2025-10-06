import numpy as np
import matplotlib.pyplot as plt

# Example for simply supported beam with point load (adapt for other cases)
L = 5.0  # m
a = 2.5  # m
P = 10.0  # kN
E = 200.0  # GPa
I = 0.0001  # m^4

b = L - a
R1 = P * b / L
R2 = P * a / L

x = np.linspace(0, L, 101)
V = np.piecewise(x, [x < a, x >= a], [R1, R1 - P])
M = np.piecewise(x, [x < a, x >= a], [lambda x: R1 * x, lambda x: R1 * x - P*(x - a)])
v = np.piecewise(x, [x < a, x >= a], 
                 [lambda x: (P * b * x / (6 * L * E*1e9 * I)) * (L**2 - b**2 - x**2) * 1000, 
                  lambda x: (P * a * (L - x) / (6 * L * E*1e9 * I)) * (L**2 - a**2 - (L - x)**2) * 1000])

fig, ax = plt.subplots(3, 1)
ax[0].plot(x, V)
ax[0].set_title('Shear Force (kN)')
ax[1].plot(x, M)
ax[1].set_title('Bending Moment (kN.m)')
ax[2].plot(x, v)
ax[2].set_title('Deflection (mm)')
plt.tight_layout()
plt.show()

print('Max Shear:', np.max(np.abs(V)))
print('Max Moment:', np.max(np.abs(M)))
print('Max Deflection:', np.max(np.abs(v)))