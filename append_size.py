def append_size(lst):
    length = len(lst)
    lst.append(length)
    return lst


solution = append_size([10, 20, 30])
print(solution)

solution2 = append_size(solution + [2])
print(solution2)
