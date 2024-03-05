age = 20
name = 'Swaroop'

print(name, "was", age, "years old when he wrote this book.")
print("%s was %d years old when he wrote this book." % (name, age))
print("{} was {} years old when he wrote this book.".format(name, age))
print("{name} was {age} years old when he wrote this book.".format_map({'name': name, 'age': age}))
print(f"{name} was {age} years old when he wrote this book.")
