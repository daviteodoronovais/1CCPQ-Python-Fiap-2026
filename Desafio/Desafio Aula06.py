from operator import truediv

endpoints = ["/login", "/produtos", "/pedidos"]
status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]

def verificarSucesso(codigo):
    return codigo >= 200 and codigo <= 299

def doisErros(listaRequisicoes):
    for i  in range(len(listaRequisicoes) - 1):
        codigoAtual = listaRequisicoes[i]
        proximoCodigo = listaRequisicoes[i + 1]

        if not verificarSucesso(codigoAtual) and not verificarSucesso(proximoCodigo):
            return True

    return False

def analisarEndpoint(listaRequisicoes):
    qtdSucessos = 0

    for codigo in listaRequisicoes:
        if verificarSucesso(codigo):
            qtdSucessos += 1

    qtdRequisicoes = len(listaRequisicoes)
    qtdErros = qtdRequisicoes - qtdSucessos

    percentualSucesso = qtdSucessos / qtdRequisicoes * 100

    errosSeguidos = doisErros(listaRequisicoes)

    if errosSeguidos:
        classificacao = "Crítico"
    elif percentualSucesso >= 80:
        classificacao = "Estável"
    else:
        classificacao = "Instável"

    return (
        qtdSucessos,
        qtdErros,
        percentualSucesso,
        classificacao
    )
maisErros  = -1
endpointMaisErros = ""
for i in range(len(endpoints)):
    nomeEndpoint = endpoints[i]
    statusEndpoint = status[i]

    sucessos, erros, percdntual, classificacao = analisarEndpoint(statusEndpoint)

    print()
    print("-" * 30)
    print(f"Endpoint: {nomeEndpoint}")
    print(f"Sucessos: {sucessos}")
    print(f"Erros: {erros}")
    print(f"Percentual de Sucesso: {percdntual:.1f}%")
    print(f"Classificacao: {classificacao}")


    if erros > maisErros:
        maisErros = erros
        endpointMaisErros = nomeEndpoint

print()
print("-" * 30)
print(f"Endpoint com mais erros: {endpointMaisErros} com ({maisErros}) erros \n")