#!/usr/bin/env python3

import sys


def ft_inventory_system() -> None:
    # parse the arguments into a dictionary
    args = sys.argv
    inventory = dict()
    restock = []
    for arg in args[1:]:
        item, count_str = arg.split(":")
        count = int(count_str)
        if count <= 1:
            restock.append(item)
        inventory[item] = count

    # sort the values
    values_list = []
    for value in inventory.values():
        values_list.append(value)
    sorted_values_list = values_list.copy()
    sorted_values_list.sort(reverse=True)

    # create new dictionary in descending order
    sorted_inventory = {
            "Moderate": dict(),
            "Scarce": dict()
    }
    copied = []
    for val in sorted_values_list:
        for item, count in inventory.items():
            if count == val and item not in copied:
                if count >= 5:
                    sorted_inventory["Moderate"].update({item: count})
                    copied.append(item)
                else:
                    sorted_inventory["Scarce"].update({item: count})
                    copied.append(item)

    # calculate total and unique items
    total_items = 0
    for count in inventory.values():
        total_items = total_items + count
    unique_types = len(inventory)

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_types}")

    # calculate and print percentages
    print("\n=== Current Inventory ===")
    for key in sorted_inventory["Moderate"].keys():
        units = int(sorted_inventory["Moderate"].get(key))
        percentage = units * 100 / total_items
        print(f"{key}: {units} units ({percentage:.1f}%)")
    for key in sorted_inventory["Scarce"].keys():
        units = int(sorted_inventory["Scarce"].get(key))
        percentage = units * 100 / total_items
        if units == 1:
            print(f"{key}: {units} unit ({percentage:.1f}%)")
        else:
            print(f"{key}: {units} units ({percentage:.1f}%)")

    # calculate most and least abundant
    highest_value = sorted_values_list[0]
    lowest_value = sorted_values_list[-1]
    for k, v in inventory.items():
        if v == highest_value:
            most_abundant = k
        if v == lowest_value:
            least_abundant = k
    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {most_abundant} ({highest_value} units)")
    print(f"Least abundant: {least_abundant} ({lowest_value} unit)")

    print("\n=== Item Categories ===")
    print(f'Moderate: {sorted_inventory["Moderate"]}')
    print(f'Scarce: {sorted_inventory["Scarce"]}')

    print("\n=== Management Suggestions ===")
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")
    keys_list = []
    for key in inventory.keys():
        keys_list.append(key)
    print(f"Dictionary keys: {keys_list}")
    print(f"Dictionary values: {values_list}")

    # find key in dictionary
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


def main() -> None:
    ft_inventory_system()


if __name__ == "__main__":
    main()
