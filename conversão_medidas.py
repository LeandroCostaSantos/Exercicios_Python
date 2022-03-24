print("======================================================================================")
print("=========        Bem vindo à Calculadora de Conversão de Medidas v1.0       ==========")
print("======================================================================================")
print("                      Criado por: Leandro Costa Santos                              \n")

print("Para converter de Metros por Segundo para Kilômetros por hora (ms/s > km/h) - Digite 1. ")
print("Para converter de Kilômetros por hora para Metros por Segundo (km/h > ms/s) - Digite 2. ")
print("Para converter de Kilômetros por hora para Milhas por hora (km/h > mp/h     - Digite 3. ")
print("Para converter um ângulo para radianos (em graus)                           - Digite 4. ")
print("Para converter de radianos para ângulo (em graus)                           - Digite 5. ")
print("Para converter de Polegadas para Centímetros                                - Digite 6. ")
print("Para converter de Centímetros para Polegadas                                - Digite 7. ")
print("Para converter de Metros Cúbicos para Litro                                 - Digite 8. ")
print("Para converter de Litros para Metros Cúbicos                                - Digite 9. ")
print("Para converter de Kilos (kg) para Libras (Lb)                              - Digite 10.\q")



convert = int(input('Digite sua escolha: '))
if convert == 1:
    c1 = float(input("Digite quantos Metros / Segundo quer converter: "))
    print(f'O valor em KM/H é {float(c1 * 3.6):.2f}.')
elif convert == 2:
    c2 = float(input('Digite quantos KM/H quer converter: '))
    print(f'O valor em M/S: {float(c2/3.6):.2f}.')
elif convert == 3:
    c3 = float(input('Digite quantos KM/H quer converter: '))
    print(f'O valor em milhas é: {float(c3/1.61):.2f}')
elif convert == 4:
    c4 = float(input('Digite um ângulo em graus para converter em radianos: '))
    print(f'O valor em radianos: {float(c4*3.14/180):.2f}')
elif convert == 5:
    c5 = float(input('Digite o valor em radianos para converter em graus: '))
    print(f'O valor em graus é: {float(c5*180/3.14):.2f}')
elif convert == 6:
    c6 = float(input('Digite quantas polegadas quer converter para Centímetros:'))
    print(f'O Valor em CM é: {float(c6*2.54)}')
elif convert == 7:
    c7 = float(input('Digite quantos Centímetros quer converter para Polegadas: '))
    print(f'O valor em polegadas : {float(c7/2.54):.2f}')
elif convert == 8:
    c8 = float(input('Digite quantos metros cúbicos quer converter para litros: '))
    print(f'O valor em litros: {float(1000*c8):.2f}')
elif convert == 9:
    c9 = float(input('Digite quantos litros quer converter para metros cúbicos: '))
    print(f'O valor em metros cúbicos é: {float(c9/1000):.2f}')
elif convert == 10:
    c10 = float(input('Digite quantos KG quer converter em Libras: '))
    print(f'O valor em Libras é: {float(c10/0.45):.2f}')
else:
    print(f' Por favor, Digitar um valor válido.')