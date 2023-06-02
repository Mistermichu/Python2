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

index = 0
for item_number, item_number_weight in enumerate(item_weight):
    first_item = item_weight[index]
    if item_number < len(item_weight) - 1:
        next_item = item_weight[index + 1]
    else:
        next_item = 0
    combined_elements = first_item + next_item
    if combined_elements > 20:
        removed_item = item_weight.pop(0)
        package_quantity.append(removed_item)
    else:

    print(first_item)
    print(next_item)
