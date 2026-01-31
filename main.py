# SPAN LOADING
# Based on the Schrenk approximation (trapezoidal approximation)
# Author : Sean O'Meara
# Date   : Feb 2026

# DONE: Basic Schrenk span loading implementation (taper no twist)
# DONE: Input parameters for span and lift distribution
# DONE: Output spanwise lift distribution in CSV format
# TODO: Add control surface deflections
# TODO: Add twist distributions
# TODO: Add roll rate effects
# TODO: Add ability to define chord distribution


## MAIN PROGRAM ##
if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    from functions import aircraft, lift_distribution, running_shear_bending

# Define aircraft parameters
aircraft = aircraft()

print("DEFINED AIRCRAFT PARAMETERS:")
print(f"Span: {aircraft['y_locations']} m")
print(f"Chord distribution: {aircraft['chord_distribution']} m")
print(f"eta distribution: {aircraft['eta']}")

# Calculate lift distribution
lift_distribution = lift_distribution(aircraft['y_locations'],
                                      aircraft['chord_distribution'],
                                      aircraft['span'],
                                      aircraft['area_ref'])

print(f"Lift coefficient distribution: {lift_distribution}")

# Determine running shear and bending moment
shear, bending_moment = running_shear_bending(aircraft['y_locations'],
                                              lift_distribution,
                                              aircraft['span'])

print(f"Shear Distribution: {shear}")
print(f"Bending Moment Distribution: {bending_moment}")

# Plot results
fig, (ax1, ax2) = plt.subplots(2)
plt.subplots_adjust(hspace=0.5)
# Plot chord distribution
ax1.plot(aircraft['y_locations'], aircraft['chord_distribution'], label='Chord Distribution')
ax1.set_xlabel('Spanwise Location y [m]')
ax1.set_ylabel('Chord Length [m]')
ax1.set_title('Chord Distribution along Span')
ax1.grid()

# Plot lift coefficient distribution
ax2.plot(aircraft['y_locations'], lift_distribution, label='Lift Coefficient Distribution', color='orange')
ax2.set_xlabel('Spanwise Location y [m]')
ax2.set_ylabel('Lift Coefficient Cl [-]')
ax2.set_title('Lift Coefficient Distribution along Span')
ax2.grid()

fig, (ax3, ax4) = plt.subplots(2)
plt.subplots_adjust(hspace=0.5)
# Plot shear distribution
ax3.plot(aircraft['y_locations'], shear, label='Shear Distribution', color='green')
ax3.set_xlabel('Spanwise Location y [m]')
ax3.set_ylabel('Shear Force [N]')
ax3.set_title('Shear Force Distribution along Span')
ax3.grid()
# Plot bending moment distribution
ax4.plot(aircraft['y_locations'], bending_moment, label='Bending Moment Distribution', color='red')
ax4.set_xlabel('Spanwise Location y [m]')
ax4.set_ylabel('Bending Moment [Nm]')
ax4.set_title('Bending Moment Distribution along Span')
ax4.grid()
plt.show()


