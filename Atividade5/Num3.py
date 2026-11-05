#João tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10
#metro e cresce 3 centímetros por ano. Construa um algoritmo que calcule e
#imprima quantos anos serão necessários para que Zé seja maior que João.
altJoao = 1.50
altze = 1.10
ano = 0
while altze < altJoao:
    altze = altze+0.03
    altJoao = altJoao+0.02
    ano += 1
print ("Zé demorou " , ano , " anos para passar João.")