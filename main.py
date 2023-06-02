print("Witaj w systemie obslugi paczek.")  # Done
print("Pamietaj, ze wysylane przedmioty musza miescic sie w przedziale wagowym od 1kg do 10kg.")  # Done
print("W jednej paczce zmiesci sie 20kg towaru.")
print("Jezeli dodawany przedmiot przekroczy dozwolona wage paczki, zostanie on wyslany w kolejnej paczce.")
print("Jezeli dodawany przedmiot bedzie wykraczal poza dozwolony przedzial wagowy, dodawanie przedmiotow zostanie zakonczone.\n")  # Done

# Wprowadzenie ilości elementów
item_quantity = None
while not isinstance(item_quantity, int):
    try:
        item_quantity = input("Podaj ilosc przedmiotow do wyslania: ")
        item_quantity = int(item_quantity)
    except ValueError:
        print("Podana wartosc jest niepoprawna, sprobuj ponownie!")

print(f"Ilosc przedmiotow: {item_quantity}")

# Wprowadzenie wagi poszczególnych elementów
item_weight = []

for item_weight_input_number in range(item_quantity):

    item_weight_input = None
    while not isinstance(item_weight_input, float):
        while not isinstance(item_weight_input, float):
            try:
                item_weight_input = input(
                    f"Podaj wage {item_weight_input_number + 1}. przedmiotu: ").replace(",", ".")
                item_weight_input = float(item_weight_input)
            except ValueError:
                print("Podana wartosc jest nieporawna, sprobuj ponownie!")
    if item_weight_input < 1 or item_weight_input > 10:
        print("Waga danego przedmiotu nie miesci sie w dozwolonym przedziale wagowym.")
        print("Dodawanie elementow zostaje zablokowane.")
        break
    else:
        item_weight.append(item_weight_input)

print("Wyszczegolnione wagi elementow:")
print(item_weight)

package_quantity = []

# Obliczenie wagi paczek
print("*" * 80)
print(f"Liczba elementow do wysłania: {len(item_weight)}")
print("-" * 5)


combined_elements = 0
for item_number, item_number_weight in enumerate(item_weight):
    print(f"Rozpoczeto dodawanie elementu: {item_number + 1}")
    if combined_elements == 0:
        print("Trwa generowanie nowej paczki")
        number_of_combined_elements = 1
        first_element_index = 0
        next_element_index = first_element_index + 1
        first_item = item_weight[first_element_index]
        print(f"Waga pierwszego przedmiotu: {first_item}")
        if item_number < len(item_weight) - 1:
            next_item = item_weight[next_element_index]
            print(f"Waga nastepnego przemdiotu w kolejce: {next_item}")
        else:
            next_item = 0
            print(f"W kolejce nie ma już wiecej przedmiotow.")
            removed_item = item_weight.pop(0)
            package_quantity.append(removed_item)
            print("*" * 20)
            print("Utworzono paczke.")
            print("Ilosc paczek:")
            print(len(package_quantity))
            print("Wyszczegolnione wagi paczek:")
            print(package_quantity)
            print("*" * 20)
            break
        combined_elements = first_item + next_item
        print(f"Laczna waga paczki {combined_elements}")
        if combined_elements > 20:
            print("Waga paczki przekroczyla 20kg. Nie mozna dodac przedmiotu do paczki")
            removed_item = item_weight.pop(0)
            package_quantity.append(removed_item)
            combined_elements = 0
            first_element_index = 0
            print("*" * 20)
            print("Utworzono paczke.")
            print("Ilosc paczek:")
            print(len(package_quantity))
            print("Wyszczegolnione wagi paczek:")
            print(package_quantity)
            print("*" * 20)
        else:
            number_of_combined_elements += 1
            print("Obecna waga paczki mniejsza niz 20kg. Dodawanie kolejnego przedmiotu")
            print(
                f"Obecna liczba przedmiotow w paczce: {number_of_combined_elements}")
    else:
        print("Trwa dodawanie kolejnego przedmiotu")
        next_element_index += 1
        first_item = combined_elements
        print(f"Obecna waga paczki: {first_item}")
        if item_number < len(item_weight) - 1:
            next_item = item_weight[next_element_index]
            print(f"Waga nastepnego przemdiotu w kolejce: {next_item}")
        else:
            next_item = 0
            print(f"W kolejce nie ma już wiecej przedmiotow.")
            del item_weight[:number_of_combined_elements]
            package_quantity.append(combined_elements)
            print("*" * 20)
            print("Utworzono paczke.")
            print("Ilosc paczek:")
            print(len(package_quantity))
            print("Wyszczegolnione wagi paczek:")
            print(package_quantity)
            print("*" * 20)
            break
        combined_elements = first_item + next_item
        print(f"Laczna waga paczki {combined_elements}")
        if combined_elements > 20:
            print("Waga paczki przekroczyla 20kg. Nie mozna dodac przedmiotu do paczki")
            del item_weight[:number_of_combined_elements]
            combined_elements -= next_item
            package_quantity.append(combined_elements)
            print(
                f"Dodano {number_of_combined_elements} elementow do paczki. Laczna waga dodanych przedmiotow: {combined_elements}")
            combined_elements = 0
            number_of_combined_elements = 1
            first_element_index = 0
            print("*" * 20)
            print("Utworzono paczke.")
            print("Ilosc paczek:")
            print(len(package_quantity))
            print("Wyszczegolnione wagi paczek:")
            print(package_quantity)
            print("*" * 20)
        else:
            number_of_combined_elements += 1
            print("Obecna waga paczki mniejsza niz 20kg. Dodawanie kolejnego przedmiotu")
            print(
                f"Obecna liczba przedmiotow w paczce: {number_of_combined_elements}")
