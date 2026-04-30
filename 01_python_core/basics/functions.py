def greet(name):
    return f"My name is {name}" 

print(greet("Adeel"))


#Function with default PArameters


def power(x,y=2):
    return x**y

print(power(5))
print(power(5,3))