print("===================================================================================")
print("======== Bem vindo ao Programa de Conversão de Escalas Termométricas v1.0 =========")
print("===================================================================================")
print("                  Criado por: Leandro Costa Santos                                 ")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
print("Para converter de Celsius para Fahrenheit - Digite 1.")
print("Para converter de Fahrenheit para Celsius - Digite 2.")
print("Para converter de Celsius para Kelvin     - Digite 3.")
print("Para converter de Kelvin para Celsius     - Digite 4.")
print("Para converter de Fahrenheit para Kelvin  - Digite 5.")
print("Para converter de Kelvin para Fahrenheit  - Digite 6.")
print("===================================================================================")
convert = float(input("Digite a opção desejada: "))

if convert == 1:
    v1 = float(input('Digite a temperatura em Celsius: '))
    print(f'Temperatura em Fahrenheit: {float(v1*(9/5)+32):.2f}F.')
elif convert == 2:
    v2 = float(input('Digite a temperatura em Fahrenheit: '))
    print(f'Temperatura em Celsius: {float(5*(v2-32)/9):.2f}ºC.')
elif convert == 3:
    v3 = float(input('Digite a temperatura em Celsius: '))
    print(f'Temperatura em Kelvin: {float(v3+273.15):.2f}K.')
elif convert == 4:
    v4 = float(input('Digite a temperatura em Kelvin: '))
    print(f'Temperatura em Celsius: {float(v4-273.15):.2f}ºC.')
elif convert == 5:
    v5 = float(input('Digite a temperatura em Fahrenheit: '))
    print(f'Temperatura em Kelvin: {float((v5-32)*5/9+273.15):.2f}K.')
elif convert == 6:
    v6 = float(input('Digite a temperatura em Kelvin: '))
    print(f'A temperatura em Fahrenheit é: {float((v6-273.15)*9/5+32):.2f}F.')
else:
    print(f'Por favor, digite um valor entre 1 à 6.')
