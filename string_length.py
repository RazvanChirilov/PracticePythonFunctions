def get_length(string):
    string_length = 0
    for ch in string:
        string_length += 1
    return string_length


a = get_length("Test")
print(a)