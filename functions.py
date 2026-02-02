# Functions fo the span loads program
# Sean O'Meara Jan 2026

# Functions required:
# 1. aircraft() - define aircraft parameters and geometry
# 2. lift_distribution() - calculate spanwise lift distribution using Schrenk approximation
# 3. running_shear_bending() - calculate running shear and bending moment from lift
# 4. distribute_mass() - create mass distribution along span based on chord

import numpy as np
import matplotlib.pyplot as plt


def aircraft():
    # USER INPUT FOR AIRCRAFT PARAMETERS
    print("Defining aircraft parameters...")
    span = float(input(" Enter span [m]: "))
    root_chord = float(input(" Enter root chord [m]: "))
    taper_ratio = float(input(" Enter taper ratio [-]: "))
    no_span_locations = int(input(" Enter number of span locations [-]: "))

    # Calculate parameters
    area_ref = root_chord * span * (1 + taper_ratio) / 2
    span_locations = np.linspace(0, span/2, num=no_span_locations)
    eta = 2*span_locations/span
    chord_distribution = np.zeros(no_span_locations)
    for i in range(len(eta)):
        chord_distribution[i] = root_chord * (1 - (1 - taper_ratio) * eta[i])

    aircraft = {
        "span": span,
        "area_ref": area_ref,
        "root_chord": root_chord,
        "taper_ratio": taper_ratio,
        "y_locations": span_locations,
        "eta": eta,
        "chord_distribution": chord_distribution
    }
    return aircraft


def lift_distribution(y, chord_distribution, span, ref_area ):
    # Schrenk approximation based on method in Peery "Aircraft Structures p224"
    y = np.array(y)
    eta = np.zeros_like(y)
    chord = np.zeros_like(y)
    five = np.zeros_like(y)
    cc = np.zeros_like(y)
    cl = np.zeros_like(y)
    for i in range(len(y)):
        y_i = y[i]
        eta[i] = 2*y_i/span
        chord[i] = chord_distribution[i]
        five[i] = (4*ref_area)/(np.pi*span) * np.sqrt(1 - (2*y[i]/span)**2)
        cc[i] = 0.5*(chord[i] + five[i])
        cl[i] = five[i]/cc[i]
    return cl


def running_shear_bending_distributed(y, distribution):
    # Calculate running shear and bending moment from lift distribution
    shear = np.zeros_like(y)
    bending_moment = np.zeros_like(y)

    for i in reversed(range(len(y))):
        if i == len(y)-1:
           shear[i] = 0
           bending_moment[i] = 0
        else:
            dy = y[i+1] - y[i]
            lift_per_length = distribution[i]  # Assuming lift_dist is per unit length
            shear[i] = shear[i+1] + lift_per_length * dy
            bending_moment[i] = bending_moment[i+1] + shear[i+1] * dy
    return shear, bending_moment


def running_shear_bending_point(y, distribution):
    # Calculate running shear and bending moment from point loads
    # Note assumes no moments TODO to expand to have Mx moment
    shear = np.zeros_like(y)
    bending_moment = np.zeros_like(y)

    for i in reversed(range(len(y))):
        if i == len(y)-1:
           shear[i] = distribution[i]
           bending_moment[i] = 0 #Assumes no a applied moments
        else:
            dy = y[i+1] - y[i]
            shear[i] = shear[i+1] + distribution[i]
            bending_moment[i] = bending_moment[i+1] + shear[i+1] * dy
    return shear, bending_moment


def distribution_mass(mass, y, chord_distribution):
    # Distributes the mass based on local chord length.
    # Mass per unit length is proportional to chord length.
    # Note the tip panel is is at y[max-1] and is from y[max] to y[(max-2+max-1/2)]
    
    mass_per_panel = np.zeros_like(y)
    for i in range(len(y)):
        if i == 0: # first panel
            mass_per_panel[i] = chord_distribution[i] * (y[i+1]-y[i])/2
        elif i == len(y)-1: # last panel
            mass_per_panel[i-1] =chord_distribution[i] * (y[i]-(y[i-1]+y[i-2])/2)
            mass_per_panel[i] = 0.0
        else:
            mass_per_panel[i] = chord_distribution[i] * (y[i+1]-y[i-1])/2

    # Scale distribution to match the total mass
    total_mass_check, bend = running_shear_bending_point(y, mass_per_panel)
    mass_per_panel = mass/total_mass_check[0] * mass_per_panel

    return mass_per_panel

