def odd_indices(lst):
    odds = []
    length = range(len(lst))
    for i in length:
        if length[i] % 2 != 0:
            odds.append(lst[i])
    return odds


print(odd_indices([4, 3, 7, 10, 11, -2]))