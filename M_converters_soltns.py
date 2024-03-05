def convert_to_L(media_volume, unit_vol):
    """Convert volume to Liters."""
    if unit_vol == 'Liter':
        return media_volume
    elif unit_vol == 'MilliLiter':
        return media_volume / 1000
    elif unit_vol == 'microLiter':
        return media_volume / 1_000_000
    else:
        raise ValueError("Invalid unit for volume")


def convert_to_molar(molarity, unit):
    """Convert molarity to Molar."""
    if unit == 'microMolar':
        return molarity / 1_000_000
    elif unit == 'MilliMolar':
        return molarity / 1_000
    elif unit == 'Molar':
        return molarity
    else:
        raise ValueError("Invalid unit for molarity")


def calculate_mass(hormone_name, molarity, unit, media_volume_liters):
    """Calculate the mass of a hormone needed in the media."""
    if hormone_name in m_hormones:
        Mol_weight = m_hormones[hormone_name]
        Molar_concentration = convert_to_molar(molarity, unit)
        Mass_grams = Molar_concentration * media_volume_liters * Mol_weight  # Mass in grams
        return Mass_grams * 1_000_000  # Convert grams to micrograms
    else:
        raise ValueError(f"Hormone {hormone_name} not found in the list.")


def main():
    m_hormones = {
        "IBA": 203.2,
        "BA": 225.3,
        'THCL': 337.26,
        'Trans-ZR': 351.4,
        'GA3': 346.4,
        '2,4-D': 221,
        'Kanamycin': 484.49,
        'Thiaduzron': 220.2,
        'Spec': 332.35,
        'Gent': 477.59,
        # Add more hormones as needed
    }

    try:
        num_hormones = int(input("How many hormones do you want to add? "))
        unit_vol = input("Enter the unit of volume (microLiter, MilliLiter, or Liter): ")
        media_volume = float(input("How much media do you want to make? "))
        total_mass_required_micrograms = 0

        for _ in range(num_hormones):
            hormone_name = input("What hormone? ")
            unit = input("Enter the unit of molarity (microMolar, MilliMolar, or Molar): ")
            Mol_concentration = float(input(f"What concentration [M] of {hormone_name} do you want in the media?: "))

            media_volume_liters = convert_to_L(media_volume, unit_vol)
            Mass_micrograms = calculate_mass(hormone_name, Mol_concentration, unit, media_volume_liters)

            if Mass_micrograms < 0.001:
                print(f"You need to add {Mass_micrograms:.2f} micrograms of {hormone_name} to your media")
            else:
                print(f"You need to add {Mass_micrograms:.4f} grams of {hormone_name} to your media")

            total_mass_required_micrograms += Mass_micrograms

        if total_mass_required_micrograms < 1_000:
            print(f"Total mass of phytohormones required: {total_mass_required_micrograms:.2f} micrograms")
        else:
            total_mass_required_grams = total_mass_required_micrograms / 1_000_000
            print(f"Total mass of phytohormones required: {total_mass_required_grams:.4f} grams")

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
