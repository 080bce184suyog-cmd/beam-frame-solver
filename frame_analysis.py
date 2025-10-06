import numpy as np

# Example for portal frame with fixed supports and horizontal load using stiffness method
h = 3.0  # height m
w = 4.0  # width m
E = 200e9  # Pa
I = 1e-4  # m4
P = 10e3  # N horizontal at left top
A = 1e6  # large area

# Local k for member
def get_local_k(L, E, A, I):
    EI = E * I
    EA = E * A
    L2 = L**2
    L3 = L**3
    return np.array([
        [EA / L, 0, 0, -EA / L, 0, 0],
        [0, 12 * EI / L3, 6 * EI / L2, 0, -12 * EI / L3, 6 * EI / L2],
        [0, 6 * EI / L2, 4 * EI / L, 0, -6 * EI / L2, 2 * EI / L],
        [-EA / L, 0, 0, EA / L, 0, 0],
        [0, -12 * EI / L3, -6 * EI / L2, 0, 12 * EI / L3, -6 * EI / L2],
        [0, 6 * EI / L2, 2 * EI / L, 0, -6 * EI / L2, 4 * EI / L]
    ])

# Transformation matrix for angle
def get_transformation(angle):
    c = np.cos(angle)
    s = np.sin(angle)
    R = np.array([
        [c, s, 0],
        [-s, c, 0],
        [0, 0, 1]
    ])
    T = np.block([
        [R, np.zeros((3,3))],
        [np.zeros((3,3)), R]
    ])
    return T

# Global K 6x6
K = np.zeros((6,6))

# Left column
k_local = get_local_k(h, E, A, I)
T = get_transformation(np.pi / 2)
k_global = T.T @ k_local @ T
K[0:3, 0:3] += k_global[3:6, 3:6]  # only upper for node 2

# Right column
k_local = get_local_k(h, E, A, I)
T = get_transformation(np.pi / 2)
k_global = T.T @ k_local @ T
K[3:6, 3:6] += k_global[3:6, 3:6]  # upper for node 3

# Beam
k_local = get_local_k(w, E, A, I)
T = get_transformation(0)
k_global = T.T @ k_local @ T
K[0:3, 0:3] += k_global[0:3, 0:3]
K[0:3, 3:6] += k_global[0:3, 3:6]
K[3:6, 0:3] += k_global[3:6, 0:3]
K[3:6, 3:6] += k_global[3:6, 3:6]

# Load F
F = np.zeros(6)
F[0] = P  # horizontal at node 2 u

# Solve U = K^-1 F
U = np.linalg.solve(K, F)

# Sway
sway = U[0] * 1000  # mm

# Moment example for left column
disp_left = np.array([0,0,0, U[0], U[1], U[2]])
force_local = k_local @ (T @ disp_left)
moment_base = force_local[2]
moment_top = force_local[5]

print('Sway Deflection:', sway)
print('Max Bending Moment:', max(abs(moment_base), abs(moment_top)) / 1000, 'kN.m')