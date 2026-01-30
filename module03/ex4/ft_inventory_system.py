#!/usr/bin/env python3

import sys

def ft_inventory_system() -> None:
    inventory = dict()
    args = sys.argv
    i = 1
    while i < len(args):
        arg = args[i]
        colon_pos = 0
        while colon_pos < len(arg):
            if arg[colon_pos] == ':':
                break
            colon_pos = colon_pos + 1
        
        item = arg[0:colon_pos]
        count = int(arg[colon_pos + 1:])
        inventory[item] = count
        i = i + 1
    
    total_items = 0
    for count in inventory.values():
        total_items = total_items + count
    
    unique_types = len(inventory)
    
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_types}")
    
    sorted_items = []
    for item in inventory.keys():
        sorted_items.append((item, inventory[item]))
    
    n = len(sorted_items)
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if sorted_items[j][1] < sorted_items[j + 1][1]:
                temp = sorted_items[j]
                sorted_items[j] = sorted_items[j + 1]
                sorted_items[j + 1] = temp
            elif sorted_items[j][1] == sorted_items[j + 1][1]:
                if sorted_items[j][0] > sorted_items[j + 1][0]:
                    temp = sorted_items[j]
                    sorted_items[j] = sorted_items[j + 1]
                    sorted_items[j + 1] = temp
            j = j + 1
        i = i + 1
    
    print("\n=== Current Inventory ===")
    for item_tuple in sorted_items:
        item = item_tuple[0]
        count = item_tuple[1]
        percentage = (count / total_items) * 100
        unit_label = "unit"
        if count != 1:
            unit_label = "units"
        print(f"{item}: {str(count)} {unit_label} ({percentage:.1f}%)")
    
    most_item = ""
    most_count = 0
    least_item = ""
    least_count = total_items + 1
    
    for item in inventory.keys():
        count = inventory[item]
        if count > most_count:
            most_count = count
            most_item = item
        if count < least_count:
            least_count = count
            least_item = item
    
    print("\n=== Inventory Statistics ===")
    print("Most abundant: " + most_item + " (" + str(most_count) + " units)")
    print("Least abundant: " + least_item + " (" + str(least_count) + " unit)")
    
    moderate = dict()
    scarce = dict()
    
    for item in inventory.keys():
        count = inventory[item]
        if count >= 4:
            moderate[item] = count
        else:
            scarce[item] = count
    
    print("\n=== Item Categories ===")
    print("Moderate: " + str(moderate))
    print("Scarce: " + str(scarce))
    
    restock = []
    for item in inventory.keys():
        count = inventory[item]
        if count <= 1:
            restock.append(item)
    
    print("\n=== Management Suggestions ===")
    print("Restock needed: " + str(restock))
    
    print("\n=== Dictionary Properties Demo ===")
    print("Dictionary keys: " + str(list(inventory.keys())))
    print("Dictionary values: " + str(list(inventory.values())))
    sword_exists = "sword" in inventory
    print("Sample lookup - 'sword' in inventory: " + str(sword_exists))


def main() -> None:
    ft_inventory_system()


if __name__ == "__main__":
    main()
