def same_values(lst1, lst2):
    storing_lst = []
    for item in range(len(lst1)):
        if lst1[item] == lst2[item]:
            storing_lst.append(item)
    return storing_lst

