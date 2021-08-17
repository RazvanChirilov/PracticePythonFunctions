def over_nine_thousand(lst):
    power_level = 0
    for power_values in lst:
        if power_level <= 9000:
            power_level += power_values
    return power_level


print(over_nine_thousand([8000, 900, 120, 5000]))
print(over_nine_thousand([8000, 900]))