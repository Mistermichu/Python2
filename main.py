package_quantity = None
while not isinstance(package_quantity, int):
    try:
        package_quantity = input("Podaj liosc paczek: ")
        package_quantity = int(package_quantity)
    except ValueError:
        print("Podana wartosc jest niepoprawna, sprobuj ponownie!")

print(f"Ilosc paczek: {package_quantity}")

item_weight = []

for item_weight_input_number in range(package_quantity):
    
    item_weight_input = None
    while not isinstance(item_weight_input, float):
        try:
            item_weight_input = input(f"Podaj wage paczki {item_weight_input_number + 1}.: ").replace(",", ".")
            item_weight_input = float(item_weight_input)
            item_weight.append(item_weight_input)
        except ValueError:
            print("Podana wartosc jest nieporawna, sprobuj ponownie!")
    
    

print(item_weight)