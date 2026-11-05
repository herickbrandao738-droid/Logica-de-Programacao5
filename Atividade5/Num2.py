#Construa um algoritmo que receba o código de vários produtos e os
#classifique de acordo com a tabela:
#CÓDIGO CLASSIFICAÇÃO
#1 Alimento não-perecível
#2 a 4 Alimento perecível
#5 e 6 Vestuário
#7 Higiene pessoal
#8 a 15 Limpeza e utensílios domésticos
#Qualquer outro código inválido exibe uma mensagem ao usuário.
#Quando o usuário digitar 0 (zero) o programa finaliza e exibe o número total
#de produtos classificados em cada categoria.

qtdProdutosTotal = 0
qtdProdutosAlimentoNaoPerecivel = 0
qtdProdutosAlimentoPerecivel = 0
qtdProdutosVestuario = 0
qtdProdutosHigientePessoal = 0
qtdProdutosLimpeza = 0
cod = 1


while cod != 0:
    cod = int(input("Digite o código do produto: "))
    if cod == 1:
        print ("Produto é 'Alimento não-perecível' ")
        qtdProdutosAlimentoNaoPerecivel += 1
        qtdProdutosTotal += 1
    elif cod >=2 and cod <= 4:
        print ("Produto é 'Alimento perecível' ")
        qtdProdutosAlimentoPerecivel += 1
        qtdProdutosTotal += 1
    elif cod >= 5 and cod <= 6:
        print ("Produto é 'Vestuário' ")
        qtdProdutosVestuario += 1
        qtdProdutosTotal += 1
    elif cod == 7:
        print ("Produto é 'Higiene pessoal' ")
        qtdProdutosHigientePessoal += 1
        qtdProdutosTotal += 1
    elif cod >= 8 and cod <= 15:
        print ("Produto é 'Limpeza e utensílios domésticos' ")
        qtdProdutosLimpeza += 1
        qtdProdutosTotal += 1
    else:
        print ("Código inválido. ")

print ("-FIM DA COMPRA-\nTotal de itens nessa compra: " , qtdProdutosTotal , "\nTotal de itens de Alimento não-perecível: " , qtdProdutosAlimentoNaoPerecivel)
print ("Total de itens de Alimento perecível: " , qtdProdutosAlimentoPerecivel , "\nTotal de itens de Vestuário:" , qtdProdutosVestuario)
print ("Total de itens de Higiene pessoal: " , qtdProdutosHigientePessoal , "\nTotal de itens de Limpeza e utensílios domésticos: " , qtdProdutosLimpeza)