import streamlit as st
import csv

# Function to load chemicals from CSV file
def load_chemicals_from_csv(csv_file):
    chemicals = {}
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            if len(row) >= 2:
                chemical_name = row[0].strip()
                molecular_weight = float(row[1].strip())
                chemicals[chemical_name] = molecular_weight
    return chemicals

# Function to convert volume to liters
def convert_to_L(media_volume, unit_vol):
    if unit_vol.lower() == 'liter':
        return media_volume
    elif unit_vol.lower() == 'milliliter':
        return media_volume / 1000
    elif unit_vol.lower() == 'microliter':
        return media_volume / 1_000_000
    else:
        raise ValueError("Invalid unit for volume")

# Function to convert molarity to Molar
def convert_to_molar(molarity, unit):
    if unit.lower() == 'micromolar':
        return molarity / 1_000_000
    elif unit.lower() == 'millimolar':
        return molarity / 1_000
    elif unit.lower() == 'molar':
        return molarity
    else:
        raise ValueError("Invalid unit for molarity")


# Function to calculate mass of a chemical
def calculate_mass(chemical_name, molarity, unit, media_volume_liters, m_chemicals):
    """Calculate the mass of a chemical needed in the media."""
    if not chemical_name:
        raise ValueError("Chemical name cannot be empty.")
    elif chemical_name not in m_chemicals:
        raise ValueError(f"Chemical {chemical_name} not found in the list.")
    else:
        Mol_weight = m_chemicals[chemical_name]
        Molar_concentration = convert_to_molar(molarity, unit)
        Mass_grams = Molar_concentration * media_volume_liters * Mol_weight  # Mass in grams
        return Mass_grams * 1000000  # Convert grams to micrograms


# Function to handle input validation for chemical concentration
def validate_concentration(concentration):
    if concentration < 0:
        raise ValueError("Concentration cannot be negative.")
    return concentration

# Main function to run the Streamlit app
def main():
    st.title('Chemical Calculator')

    csv_file = st.text_input("Enter the path to the CSV file containing chemical data:")
    if csv_file:
        m_chemicals = load_chemicals_from_csv(csv_file)
    else:
        m_chemicals = {}

    num_chemicals = st.number_input("How many chemicals do you want to add?", min_value=1, step=1)
    unit_vol = st.selectbox("Enter the unit of volume:", ['Liter', 'Milliliter', 'Microliter'])
    media_volume = st.number_input("How much volume will the solution contain?", min_value=0.0)

    summary_data = []  # Initialize summary data list

    for i in range(1, num_chemicals + 1):
        chemical_name = st.selectbox(f"What chemical will you use? {i}", options=list(m_chemicals.keys()))
        unit = st.selectbox(f"Enter the unit of molarity for final concentration {i}:", ['Micromolar', 'Millimolar', 'Molar'])
        Mol_concentration = st.number_input(f"What concentration {unit} of {chemical_name} do you want in the media? {i}", min_value=0.0)

        try:
            Mol_concentration = validate_concentration(Mol_concentration)
        except ValueError as e:
            st.error(str(e))
            continue

        try:
            media_volume_liters = convert_to_L(media_volume, unit_vol)
            Mass_micrograms = calculate_mass(chemical_name, Mol_concentration, unit, media_volume_liters, m_chemicals)

            chemical_data = {"Chemical": chemical_name, "Amount": None, "Unit": None}
            if Mass_micrograms > 1000000:
                Mass_grams = Mass_micrograms / 1000000
                chemical_data["Amount"] = f"{Mass_grams:.4f}"
                chemical_data["Unit"] = "grams"
            elif Mass_micrograms > 1000:
                Mass_milligrams = Mass_micrograms / 1000
                chemical_data["Amount"] = f"{Mass_milligrams:.4f}"
                chemical_data["Unit"] = "milligrams"
            else:
                chemical_data["Amount"] = f"{Mass_micrograms:.4f}"
                chemical_data["Unit"] = "micrograms"

            summary_data.append(chemical_data)

        except ValueError as e:
            st.error(str(e))
            continue

    if summary_data:  # Display the summary table
        st.write("Summary of Chemicals and Amounts Required:")
        st.table(summary_data)

if __name__ == '__main__':
    main()
