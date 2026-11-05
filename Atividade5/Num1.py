totalVeiculos = 0
totalAcidentes = 0
veiculosSC = 0
veiculosRS = 0
veiculosPR = 0
acidentesSC = 0
acidentesRS = 0
acidentesPR = 0

if cod >= 11 and cod <= 14:
    estado = "SC"
elif cod >= 21 and cod <= 24:
    estado = "RS"
else:
    estado = "PR"

for i in range (12):
    codigo = int(input("Digite o código da cidade: "))
    veiculos = int(input("Digite o número de veículos: "))
    acidentes = int(input("Digite o número de acidentes com vítimas: "))
    