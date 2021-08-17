def double_index(lst, index_to_double):
    if index_to_double >= len(lst):
        return lst
    else:
        new_list = lst[:index_to_double]
        new_list.append(lst[index_to_double]*2)
        new_list = new_list + lst[index_to_double + 1:]
        return new_list


print(double_index([1, 2, 3, 4], 3))








