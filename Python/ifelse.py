idade = eval(input("Digite sua idade: "))

if idade < 10:
    print("Você é criança")

elif idade < 18:
    print("Você é adolescente")

elif idade < 65:
    print("Você é adulto")

else:
    print("Você ta velho")
