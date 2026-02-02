# Write output to file

# TODO Check output file exists ask user ok to overwrite
# TODO Add timestamp to output files
# TODO Add header info to output files

def write_lift_distribution(y_locations, lift_distribution):
    output_file = "lift_distribution.txt"
    with open(output_file, 'w') as f:
        f.write("Spanwise Location (m), Lift Coefficient\n")
        for y, cl in zip(y_locations, lift_distribution):
            f.write(f"{y}, {cl}\n")
    print(f"Lift distribution written to {output_file}")
    return

def write_shear_bending(y_locations, shear, bending_moment):
    output_file = "shear_bending_distribution.txt"
    with open(output_file, 'w') as f:
        f.write("Spanwise Location (m), Shear Force (N), Bending Moment (Nm)\n")
        for y, V, M in zip(y_locations, shear, bending_moment):
            f.write(f"{y}, {V}, {M}\n")
    print(f"Shear and bending moment distribution written to {output_file}")
    return

def write_mass_distribution(y_locations, mass_distribution):
    output_file = "mass_distribution.txt"
    with open(output_file, 'w') as f:
        f.write("Spanwise Location (m), Mass per Unit Length (kg/m)\n")
        for y, m in zip(y_locations, mass_distribution):
            f.write(f"{y}, {m}\n")
    print(f"Mass distribution written to {output_file}")
    return

