package_quantity = None
while not isinstance(package_quantity, int):
    try:
        package_quantity = input("Podaj liosc paczek: ")
        package_quantity = int(package_quantity)
    except ValueError:
        print("Podana wartosc jest niepoprawna, sprobuj ponownie!")

print(f"Ilosc paczek: {package_quantity}")