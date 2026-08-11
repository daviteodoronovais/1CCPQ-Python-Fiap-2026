palavra = input("Digite uma palavra: ").lower()

def contador(palavra):
    dicionario = dict()
    for caractere in palavra:
        if caractere not in dicionario:
            dicionario[caractere] = 1
        else:
            dicionario[caractere] += 1

    return dicionario
dict_contagem = contador(palavra)
print(dict_contagem)