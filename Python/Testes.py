preco_hamburguer = 10.00
preco_refri = 5.00
preco_batata = 7.00

quantidade_hamburguer = int(input("Digite a quantidade desejada de hamburguer: "))
quantidade_refri = int(input("Quantidade de refrigerante: "))
quantidade_batata = int(input("Quantidade de batata: "))

ValorFinal = (preco_hamburguer * quantidade_hamburguer) + (quantidade_refri * preco_refri) + (quantidade_batata * preco_batata)

print("O valor total ficou em: ", ValorFinal)