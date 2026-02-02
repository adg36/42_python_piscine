def ft_count_harvest_recursive(days=0, i=0):
    if i == 0:
        days = int(input("Days until harvest: "))
        if days != 0:
            i = 1
    if i == days & days == 0:
        print("Harvest time!")
    elif i == days & days != 0:
        print(f"Day {i}\nHarvest time!")
    else:
        print(f"Day {i}")
        ft_count_harvest_recursive(days, i + 1)
