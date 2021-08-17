def remove_middle(lst, starting_index, ending_index):
    elements_before_index = lst[:starting_index]
    elements_after_index = lst[ending_index + 1:]
    list_combined = elements_before_index + elements_after_index
    return list_combined


a = remove_middle([4, 8 , 15, 16, 23, 42], 1, 3)
print(a)


