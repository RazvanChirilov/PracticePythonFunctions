def more_frequent_item(lst, first_item, second_item):
    item1 = lst.count(first_item)
    item2 = lst.count(second_item)
    if item1 > item2:
        return first_item
    return second_item
