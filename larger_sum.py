def larger_sum(lst1, lst2):
    lst1_sum = 0
    lst2_sum = 0
    while len(lst1) > 0:
        lst1_sum = sum(lst1)
        while len(lst2) > 0:
            lst2_sum = sum(lst2)
            if lst1_sum > lst2_sum:
                return lst1
            else:
                return lst2


print(larger_sum([1, 9, 5], [2, 3, 7]))

