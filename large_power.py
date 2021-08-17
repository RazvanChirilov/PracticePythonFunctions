def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False


solution = large_power(10, 5)
print(solution)