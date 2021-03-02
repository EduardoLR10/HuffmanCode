import math

total = int(input())
originalTotal = total
enviado = 0
taxas = []


while enviado != total:
    transferenciaAtual = int(input())
    taxas.append(transferenciaAtual)
    enviado += transferenciaAtual

segundos = 0
enviado = 0

print("Transmitindo " + str(originalTotal) + " bytes...")
for taxa in taxas:
    enviado += taxa
    segundos = segundos + 1
    if (segundos % 5) == 0:
        if enviado != 0:
            taxaMedia = enviado / 5;
            restante = math.ceil(round(((total - enviado) / taxaMedia), 2))
            if restante != 0:
                print("Tempo restante: " + str(restante) + " segundos.")
                total -= enviado
                enviado = 0
        else:
            print("Tempo restante: pendente...")

print("Tempo total: " + str(len(taxas)) + " segundos.")
