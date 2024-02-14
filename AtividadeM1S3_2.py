# ESTUDAR!
# Obrigatório: Função
# Opcional: Versão Recursiva

def mostra_ate_zero(numero):
  while numero >= 0:
    print(numero)
    numero -= 1 # Mesma coisa que 'numero = numero - 1'

numero = int(input('Digite o número: '))

mostra_ate_zero(numero)