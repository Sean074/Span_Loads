# SPAN LOADING
# Based on the Schrenk approximation (trapezoidal approximation)
# Author : Sean O'Meara
# Date   : Feb 2026

# DONE: Basic Schrenk span loading implementation (taper no twist)
# DONE: Input parameters for span and lift distribution
# DONE: Calculate span load distribution
# DONE: Calculate shear and bending moment distributions
# DONE: Plot chord, lift, shear and bending moment distributions
# DONE: Add the mass distribution
# TODO: Clean up the user interface
# TODO: Add discrete mass
# TODO: Generate a load case (aero + inertia)
# TODO: Output to CSV
# TODO: Write a log file
# TODO: Add spanwise drag forces
# TODO: Modify the span cuts to be more dense towards the tip
# TODO: Add control surface deflections
# TODO: Add twist distributions
# TODO: Add roll rate effects
# TODO: Add ability to define chord distribution (non-straight-tapered)
# TODO: Add pitching moment


## MAIN PROGRAM ##
if __name__ == "__main__":
    import numpy as np
    import scipy as scipy
    import matplotlib.pyplot as plt
    from functions import aircraft, lift_distribution, running_shear_bending_distributed
    from functions import distribution_mass
    from plotting import plot_span_loading, plot_shear_bending, plot_mass_distribution
    from output import write_lift_distribution, write_shear_bending, write_mass_distribution

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

area = (aircraft['chord_distribution'], aircraft['y_locations'])
input(f"Area, half span (1 wing): {area} m^2")


# Determine running shear and bending moment
shear, bending_moment = running_shear_bending_distributed(aircraft['y_locations'],
                                              lift_distribution )

# Create mass model
one_wing_mass = float(input("Wing mass per side (kg): "))
mass_distribution = distribution_mass(one_wing_mass,
                                    aircraft['y_locations'],
                                   aircraft['chord_distribution'])

## PLOTTING RESULTS ##
print("PLOTTING RESULTS...")
print("Select 1 for span loading")
print("Select 2 for shear and bending moment")
print("Select 3 for both")
print("Select 4 for mass distribution")
print("Select 5 to write output file")
selection =input("Selection: ")

if selection == '1':
    plot_span_loading(aircraft, lift_distribution)
elif selection == '2':
    running_shear_bending_distributed(aircraft, shear, bending_moment)
elif selection == '3':
    plot_span_loading(aircraft, lift_distribution)
    running_shear_bending_distributed(aircraft, shear, bending_moment)
elif selection == '4':
    plot_mass_distribution(aircraft, mass_distribution)
elif selection == '5':
    from output import write_lift_distribution
    write_lift_distribution(aircraft['y_locations'], lift_distribution)
    write_shear_bending(aircraft['y_locations'], shear, bending_moment)
    write_mass_distribution(aircraft['y_locations'], mass_distribution)
else:   
    print("Invalid selection, please select 1, 2, 3 or 4.")
