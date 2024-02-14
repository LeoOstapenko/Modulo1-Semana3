# Tentar uma outra hora utilizando '*args'

def somatres(x, y, z):
    soma = x + y + z
    return soma

x = int(input('Primeiro número: '))
y = int(input('Segundo número: '))
z = int(input('Terceiro número: '))

print(somatres(x, y, z))