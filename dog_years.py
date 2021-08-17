def dog_years(name, age):
    result = name + ", you are " + str(age*7) + " " + "years old in dog years"
    return result


print(dog_years("Lola", 16))
print(dog_years("Baby", 0))