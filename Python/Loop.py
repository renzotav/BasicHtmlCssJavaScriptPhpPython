#loops for, while
nomes = ['Renzo', 'Lorena', 'Bruce', 'Igor Jesus']
for nome in nomes:
    print(nome)

#calcular o quadrado dos números
numeros = [2, 4, 6, 8]
for numero in numeros:
    quadrado = numero ** 2
    print(f"O quadrado de {numero} é {quadrado}")

#somar números
numeros = [2, 4, 6, 8]
soma = 0
for numero in numeros:
    soma += numero
print(f'A soma dos números é: {soma}')

#contar letras
texto = "Programação"
letra_para_contar = "r"
contador = 0
for letra in texto:
    if letra == letra_para_contar:
        contador += 1
print(f'Quantidade de {letra_para_contar} na palavra {texto}: {contador}')

#laço while
palavra = input('Entre com uma palavra: \n')
while palavra != 'sair':
    palavra = input('Digite sair para encerrar o laço: \n')
print('Você digitou sair e agora está fora do laço')

#laço infinito
while True:
    print('Você está no primeiro laço.')
    opcao1 = input('Deseja sair dele? Digite SIM para isso. \n')
    if opcao1 == 'SIM':
        break  # este break é do primeiro laço
    else:
        while True:
            print('Você está no segundo laço.')
            opcao2 = input('Deseja sair dele? Digite SIM para isso. \n')
            if opcao2 == 'SIM':
               break  # este break é do segundo laço
        print('Você saiu do segundo laço.')
print('Você saiu do primeiro laço')

#continue
for num in range(1, 11):
    if num == 5:
        continue
    else:
        print(num)
print('Laço encerrado')

#exec
for num in range (1000,10000):
    menor = num % 100 #obtem o numero dos algarismos menos significativos
    maior = num // 100 #obtem o numero dos algarismos mais significativos
    raiz = menor + maior  #obtem a raiz

    if (raiz * raiz ) == num: #valida se a raiz gera o numero testado
        print(num)
        print(menor)
        print(maior)
        print(raiz)
print('terminou')
print('saiu ', num)
