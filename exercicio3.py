# entrada do usuario 
valor = float(input("digite um valor:"))

# calculos
dobro = valor * 2
triplo = valor * 3
quadrado = valor ** 2
raiz_quadrada = valor ** 0.5
raiz_cubica = valor ** (1/3)

# Saidas 
print('resultados para o valor {valor}:')
print(f'Dobro:{dobro}')
print(f'Triplo:{triplo}')
print(f'Ao quadrado: {quadrado}')
print(f'Raiz quadrada:{raiz_quadrada:.2f}')
print(f'Raiz cubica:{raiz_cubica:2f}')