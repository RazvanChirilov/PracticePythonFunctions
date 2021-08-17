def combine_sort(lst1, lst2):
    combined_list = sorted(lst1 + lst2)
    return combined_list


a = combine_sort([1,2,3], [8,9])
print(a)