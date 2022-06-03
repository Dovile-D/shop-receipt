# Byloje prekes.txt pateiktas prekių sąrašas ir jų kainos. Byloje krepselis.txt pateiktas sąrašas perkamų prekių ir
# jų kiekis. Parašykite programą, kuri apskaičiuotų kiek reikės mokėti už kiekvieną prekių poziciją ir už visą
# pirkinių krepšeli. Pirkinio suma viršija 50 eur. – trims brangiausioms pozicijoms taikoma 15% nuolaida. Rezultatą
# išveskite į bylą cekis.txt. Pateikite prekių sąrašas ir suma be nuolaidos ir jei reikia, apačioje pateikite 3
# prekių sąrašą, jų nuolaidos dydį ir galutinę mokamą sumą.
#
# Naudokite funkcijas, dict tipą, konstantas pirkinio sumai ir nuolaidos dydžiui.

import constant


def add_items_to_dict(file_path):
    """Function that takes path of txt file as a parameter and returns a dictionary with key:value pair of every row
    of that file"""
    with open(file_path) as file:
        dict = {}
        for line in file:
            # extracting item and price values from a row
            key = line.rsplit('_', 1)[0].strip("\n").strip("\t")
            # separating price value from unnecessary symbols and changing it to a float:
            value = float((line.rsplit('_', 1)[1]).strip("\n").strip("\t").replace(",", "."))
            dict[key] = value
        return dict


def calculate_total_price_of_cart_item(price_dict, quantity_dict):
    """Function that takes 2 dictionaries as parameters and returns a dictionary of overlapping keys from both as a
    key and and multiplication of both values as a value"""
    dict = {}
    for key in price_dict:
        if key in quantity_dict:
            value = price_dict[key] * quantity_dict[key]
            dict[key] = value
    return dict


def calculate_total_price_of_cart(cart_dict):
    """Function that takes dictionary as a parameter and returns total sum of it's values"""
    total_price = 0.0
    for key in cart_dict:
        total_price += cart_dict[key]
    return total_price

def sort_values(cart_dict):
    """Function that takes dictionary as a parameter and returns sorted dictionary by values"""
    dict = {}
    sorted_keys = sorted(cart_dict, key=cart_dict.get)
    for i in sorted_keys:
        dict[i] = cart_dict[i]
    return dict


def get_most_expensive_items(sorted_dict, number_of_items):
    """Function that takes sorted dictionary and number as parameters and returns a dictionary of most expensive items.
    The length of this dictionary is equals to passed number"""
    dict = {}
    # adding keys of dict to a list to get their indexes:
    keys = list(sorted_dict.keys())
    # dictionary is sorted ascending so
    j = -1
    if number_of_items > len(sorted_dict):
        number_of_items = len(sorted_dict)
    for item in range(number_of_items):
        # adding items to a dictionary in descending order
        dict[keys[j]] = sorted_dict[keys[j]]
        j -= 1
    return dict


def reduce_price(most_expensive_dict, percentage):
    """Function that takes a dictionary as a parameter and reduces it's values by given percentage and returns a dict
    with new values"""
    dict = {}
    for key in most_expensive_dict:
        dict[key] = most_expensive_dict[key] - (percentage * (most_expensive_dict[key])) / 100
    return dict



items_dict = add_items_to_dict("prekes.txt")
cart_dict = add_items_to_dict("krepselis.txt")
total_cart_item_dict = calculate_total_price_of_cart_item(items_dict, cart_dict)
total_cart_price = calculate_total_price_of_cart(total_cart_item_dict)
sorted_total_cart_dict = sort_values(total_cart_item_dict)
most_expensive_items_dict = get_most_expensive_items(sorted_total_cart_dict, 3)

print(items_dict)
print(cart_dict)
print(total_cart_item_dict)
print(total_cart_price)
print(sorted_total_cart_dict)
print(most_expensive_items_dict)
