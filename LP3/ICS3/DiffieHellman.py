### PUBLIC KEYS
P = 17
G = 27
### PRIVATE KEYS
a = 13
b = 9
### GENERATE KEYS
x = (G ** a) % P
y = (G ** b) % P
print()
print(f'Generated Keys - x: {x}, y: {y}')
print()
### GENERATE SECRET KEY WITH x AND y
key_a = (y ** a) % P
key_b = (x ** b) % P
print(f'Generated Secret Keys - KEY-A: {key_a}, KEY-B: {key_b}')
print()