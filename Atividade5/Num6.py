#Faça uma Programa que receba, como entrada, uma lista de números
#positivos ou negativos finalizada com o número zero e forneça, como saída, a
#soma dos números positivos, a soma dos números negativos e a soma das
#duas somas parciais e mostre os números pares e ímpares ao final.
positivo = 0
negativo = 0
numPar = ""
numImpar = ""
while True:
    num = float(input("Digite um número: "))
    if num > 0:
        positivo += num
        if num % 2 == 0:
            numPar += str(num)
            numPar += ", "
        else:
            numImpar += str(num)
            numImpar += ", "
    elif num < 0:
        negativo += num
        if num % 2 == 0:
            numPar += str(num)
            numPar += ", "
        else:
            numImpar += str(num)
            numImpar += ", "
    else:
        print ("A soma dos números positivos é: " , positivo)
        print ("A soma dos números negativos é: " , negativo)
        print ("A diferença entre os números positivos e negativos é: " , positivo - negativo)
        print ("Os números pares informados são: " , numPar)
        print ("Os números ímpares informados são: " , numImpar)
        break