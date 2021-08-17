def in_range(first_parameter, lower_bound, upper_bound):
    if lower_bound <= first_parameter <= upper_bound:
        return True
    return False


solution = in_range(22, 20, 30)
print(solution)