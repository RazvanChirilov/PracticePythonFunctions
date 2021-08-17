def add_greetings(names):
    add_greetings = []
    for name in names:
        add_greetings.append('Hello, ' + name)
        continue
    return add_greetings


print(add_greetings(["Owen", "Max", "Sophie"]))