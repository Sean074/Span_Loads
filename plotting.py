# Plotting results for span loads program
# Sean O'Meara Jan 2026

import matplotlib.pyplot as plt

from functions import aircraft

def plot_span_loading(aircraft, lift_distribution):
    # Plot chord and lift distributions
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
    plt.show()

def plot_shear_bending(aircraft, shear, bending_moment):
    # Plot shear and bending moment distributions``
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

def plot_mass_distribution(aircraft, mass_distribution):
    # Plot shear and bending moment distributions``
    fig, (ax1, ax4) = plt.subplots(2)
    plt.subplots_adjust(hspace=0.5)

    # Plot shear distribution
    ax1.plot(aircraft['y_locations'], aircraft['chord_distribution'], label='Chord Distribution')
    ax1.set_xlabel('Spanwise Location y [m]')
    ax1.set_ylabel('Chord Length [m]')
    ax1.set_title('Chord Distribution along Span')
    ax1.grid()

    # Plot bending moment distribution
    ax4.plot(aircraft['y_locations'], mass_distribution, label='Mass Distribution', color='red')
    ax4.set_xlabel('Spanwise Location y [m]')
    ax4.set_ylabel('Mass per Unit Length [kg/m]')
    ax4.set_title('Mass Distribution along Span')
    ax4.grid()
    plt.show()
    return