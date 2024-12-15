escolha = input("Escolha uma opção de função: 1 ou 2\n")
if escolha == "1":
    def func1(x):
        return x + 1


    s = func1(10)

else:
    def func2(x):
        return x + 2


    s = func2(10)

print(s)

#Separando função do programa principal
def func1(x):
    x = 10
    print(f'Função func1 - x = {x}')


def func2(x):
    x = 20
    print(f'Função func2 - x = {x}')


x = 0
func1(x)
func2(x)
print(f'Programa principal - x = {x}')


#Variaveis globais
def func1():
    global x
    x = 10
    print(f'Função func1 - x = {x}')


def func2():
    global x
    x = 20
    print(f'Função func2 - x = {x}')


x = 0
func1()
func2()
print(f'Programa principal - x = {x}')

#função dentro de função

def taximetro(distancia):
    def calculaMult():
        if distancia < 5:
            return 1.2
        else:
            return 1

    multiplicador = calculaMult()
    largada = 3
    km_rodado = 2
    valor = (largada + distancia * km_rodado) * multiplicador
    return valor

dist = eval(input("Entre com a distancia a ser percorrida em km: \n"))
pagamento = taximetro(dist)
print(f'O valor a pagar é R$ {pagamento}')

#cpf

def validar_cpf(cpf):
    # Removendo caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verificando se o CPF possui 11 dígitos
    if len(cpf) != 11:
        return False

    # Verificando se todos os dígitos são iguais (caso raro, mas inválido)
    if cpf == cpf[0] * 11:
        return False

    # Calculando o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    if resto < 2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto

    # Verificando o primeiro dígito verificador
    if int(cpf[9]) != digito_verificador_1:
        return False

    # Calculando o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto

    # Verificando o segundo dígito verificador
    if int(cpf[10]) != digito_verificador_2:
        return False

    # CPF válido
    return True


# Testando a função
cpf = "123.456.789-09"
if validar_cpf(cpf):
    print(f"O CPF {cpf} é válido.")
else:
    print(f"O CPF {cpf} é inválido.")