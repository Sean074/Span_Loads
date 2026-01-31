# SPAN LOADING
# Based on the Schrenk approximation (trapezoidal approximation)
# Author : Sean O'Meara
# Date   : Feb 2026

# DONE: Basic Schrenk span loading implementation (taper no twist)
# DONE: Input parameters for span and lift distribution
# DONE: Calculate span load distribution
# DONE: Calculate shear and bending moment distributions
# DONE: Plot chord, lift, shear and bending moment distributions
# TODO: Add the inertia
# TODO: Generate a load case (aero + inertia)
# TODO: Modify the span cuts to be more dense towards the tip
# TODO: Output to CSV
# TODO: Write a log file
# TODO: Add control surface deflections
# TODO: Add twist distributions
# TODO: Add roll rate effects
# TODO: Add ability to define chord distribution


## MAIN PROGRAM ##
if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    from functions import aircraft, lift_distribution, running_shear_bending
    from plotting import plot_span_loading, plot_shear_bending

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


## PLOTTING RESULTS ##
print("PLOTTING RESULTS...")
print("Select 1 for span loading")
print("Select 2 for shear and bending moment")
print("Select 3 for both")
selection =input("Selection: ")

if selection == '1':
    plot_span_loading(aircraft, lift_distribution)
elif selection == '2':
    plot_shear_bending(aircraft, shear, bending_moment)
elif selection == '3':
    plot_span_loading(aircraft, lift_distribution)
    plot_shear_bending(aircraft, shear, bending_moment)
else:   
    print("Invalid selection, please select 1, 2 or 3")
