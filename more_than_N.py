# we have different flavour snakes
# we want to check the instances of a certain type
def more_than_n(type_of_snakes, item_type_of_snake_we_are_looking_for, number_of_instances):
    if type_of_snakes.count(item_type_of_snake_we_are_looking_for) > number_of_instances:
        return True
    return False


print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

