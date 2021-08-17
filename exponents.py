def exponents(bases, powers):
    result = []
    for base in bases:
        for power in powers:
            result.append(base ** power)
    return result


print(exponents([2, 3, 4], [1, 2, 3]))
