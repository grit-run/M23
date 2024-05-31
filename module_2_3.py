my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
cntr = 0
while cntr < len(my_list) and my_list[cntr] >= 0:
    if my_list[cntr] > 0:
        print(my_list[cntr])
    cntr += 1