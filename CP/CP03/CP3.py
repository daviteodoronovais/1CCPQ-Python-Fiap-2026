temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]
somas = []
medias = []
medidor = []
limite = 33
for i, linha in enumerate(temperaturas):
        m = sum(1 for x in linha if x >= limite)
        somas.append(sum(temperaturas[i]))
        medidor.append(m)

maiorRisco = max(medidor)
sala_maior_risco = medidor.index(maiorRisco)

for j in range(len(somas)):
    medias.append(somas[j]/4)


for s in range(len(temperaturas)):
    print(f"Sala: {s+1}")
    print(f"Média: {medias[s]}")
    print(f"Registros críticos: {medidor[s]}")
    print()

print(f"Sala com maior risco: Sala {sala_maior_risco + 1}")