# Utilizar 'slicing' para indexar strings (opcional).

palavra1 = input()
palavra2 = input()

def prefixo_ou_nao(palavra1, palavra2):
    
    if palavra1 in palavra2:
        return True
        
    else:
        return False
    
print(prefixo_ou_nao(palavra1, palavra2))