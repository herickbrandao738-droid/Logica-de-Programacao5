#Uma loja tem 150 clientes cadastrados e deseja mandar uma
#correspondência a cada um deles anunciando um bônus especial. Escreva
#um algoritmo que leia o nome do cliente e o valor das suas compras no ano
#passado e calcule um bônus de 10% se o valor das compras for menor que
#500.00 e de 15 %, caso contrário.

for contagem in range (1, 150):
    cliente = str(input("Digite o nome do Cliente: "))
    valorGasto = float(input("Digite o valor gasto no último ano: "))
    contagem += 1
    if valorGasto < 500.0:
       print ("O valor bonus do Cliente é: " , valorGasto * 0.1) 
    else:
        print ("O valor bonus do Cliente é: " , valorGasto * 0.15)