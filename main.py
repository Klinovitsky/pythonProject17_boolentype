s = "string"
i = 4
b = False
f = 5.5
print(s, i, b, f)
print(type(s), type(i), type(b), type(f))
f = int(f)
print("\t------------\t--------- CONVERTED to int: ", f, "The TYPE NOW IS: ", type(f))

dynamic_var: bool = True
dynamic_var2: int = 777

s2: str = "Fuck"
i2: int = 444
f2: float = 2.2222

# Convert to boolen type of data
dynamic_var2 = bool(s2)

print("Variable is: ", dynamic_var, s2, i2, f2, dynamic_var2)
print("Variable type is: ", type(dynamic_var), type(s2), type(i2), type(f2), type(dynamic_var2))

t = 1
while t <= 3:
    print(t)
    t += 1
