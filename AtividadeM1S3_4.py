# Extra: utilizar Função e *args (opcional).

numero = int(input('Digite um número: '))
soma = 0

while numero != -1:
    soma = soma + numero
    numero = int(input('Digite outro número: '))    

    if numero == -1:
        print('Soma é', soma)
    