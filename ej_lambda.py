def multiplicar(x,y):
    return x * y

print(multiplicar(4,5))

multiplicar1 = lambda x,y: x * y
print(multiplicar1(4,5))

print(f'{(lambda x,y: x * y)(4,5)}')