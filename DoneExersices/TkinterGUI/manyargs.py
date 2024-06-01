

def add(*args):
    suma = 0
    for n in args:
        suma += n
    return suma

print(add(1, 3, 4 ,5))
print(add(2, 3, 5 ,5 ,6))


def calculate(**kwargs):
    print(kwargs)
    
    
calculate(add=3, rest=4)