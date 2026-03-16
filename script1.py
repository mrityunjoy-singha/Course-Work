import  numpy as np
import  matplotlib.pyplot as plt
import scipy as sp 
# a = np.arange(0, 10, 0.1)
# b = np.sin(a)
# plt.plot(a, b)
# plt.show()

import math

# Constants and given parameters
m_p = 938.272        # Proton rest mass in MeV/c^2
E_kin_0 = 0.5        # Initial kinetic energy in MeV
E_kin_out = 10.0     # Final kinetic energy in MeV
N_cells = 40         # Total number of cells
lambda_rf = 1.5      # RF wavelength in meters

# Energy gained per cell (assumed constant)
delta_E = (E_kin_out - E_kin_0) / N_cells

total_length = 0.0

print(f"{'Cell':<5} | {'E_kin (MeV)':<12} | {'Beta':<10} | {'L_cell (cm)':<12}")
print("-" * 47)

for n in range(1, N_cells + 1):
    # Kinetic energy at the exit of cell n
    E_kin_n = E_kin_0 + n * delta_E
    
    # Calculate relativistic gamma and beta
    gamma = 1.0 + (E_kin_n / m_p)
    beta = math.sqrt(1.0 - (1.0 / (gamma**2)))
    
    # Calculate cell length (beta * lambda)
    L_cell = beta * lambda_rf

    
    # Add to total length
    total_length += L_cell
    
    # Print the first few and last few cells to see the progression
    if n <= 3 or n >= 38:
        print(f"{n:<5} | {E_kin_n:<12.4f} | {beta:<10.5f} | {L_cell * 100:<12.3f}")
    elif n == 4:
        print(f" ...  |     ...      |    ...     |     ...")

print("-" * 47)
print(f"Total length of the accelerator: {total_length:.4f} meters")

s = np.sqrt((938)**2 + (1876)**2 + 2 * 1876 * 948)
print(f"Center-of-mass energy (sqrt(s)): {s:.5f} MeV")