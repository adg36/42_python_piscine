def ft_count_harvest_recursive(days=0, i=0):
    if i == 0:
        days = int(input("Days until harvest: "))
        i = 1
    if i == days:
        print(f"Day {i}\nHarvest time!")
    else:
        print(f"Day {i}")
        ft_count_harvest_recursive(days, i + 1)
