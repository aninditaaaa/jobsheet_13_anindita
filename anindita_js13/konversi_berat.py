def weight_conversion():
    def kg_to_pounds(weight_kg):
        weight_lbs = weight_kg * 2.20462
        return weight_lbs

    def pounds_to_kg(weight_lbs):
        weight_kg = weight_lbs / 2.20462
        return weight_kg

    satuan = input("Masukkan satuan berat (kg atau lbs): ").lower()

    if satuan == 'kg':
        weight_input = float(input("Masukkan berat dalam kilogram: "))
        weight_output = kg_to_pounds(weight_input)
        print(f"{weight_input} kg sama dengan {weight_output:.2f} lbs")
    elif satuan == 'lbs':
        weight_input = float(input("Masukkan berat dalam pounds: "))
        weight_output = pounds_to_kg(weight_input)
        print(f"{weight_input} lbs sama dengan {weight_output:.2f} kg")
    else:
        print("Satuan berat yang dimasukkan tidak valid. Harap masukkan 'kg' atau 'lbs'.")