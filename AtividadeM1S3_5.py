def funcao(x):
    if x > 0:
        return 'Positivo'
    elif x < 0:
        return 'Negativo'
    else:
        return 'Zero'

x = int(input())
print(funcao(x))