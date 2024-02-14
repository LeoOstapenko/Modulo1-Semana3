def gorjeta(conta, taxa):
    return (conta * taxa) / 100
    

conta = float(input())
taxa = int(input())
resultado = gorjeta(conta, taxa)
print(f'{resultado:.2f}')

