def max_number(num1, num2, num3):
    if num3 < num1 > num2:
        return num1
    elif num1 < num2 > num3:
        return num2
    elif num1 < num3 > num2:
        return num3
    return "It's a tie!"

