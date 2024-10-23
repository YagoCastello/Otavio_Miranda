# numeros = [1,2,3,4,5,6,7,8]
# divisao = [ numero/2 for numero in numeros]
# print(numeros)
# print(divisao)

########MAP##########################
# numeros = [1,2,3,4,5,6,7,8]

# def divisãoFn(x,y):
#     return x/y


# def multiplicaçãoFn(x,y):
#     return x*y


# def potenciaçãoFn(x,y):
#     return x**y

# divisao = [ divisãoFn(numero,2) for numero in numeros]
# multiplicacao = [ multiplicaçãoFn(numero,2) for numero in numeros]
# potencializacao = [ potenciaçãoFn(numero,2) for numero in numeros]
# print('Exemplo de MAP')
# print(numeros)
# print(divisao)
# print(multiplicacao)
# print(potencializacao)

# #FILTER###################

# valores = [1,2,3,4,5,6,7,8,9,10]

# novos_valores = [valor for valor in valores if valor >5]
# print('Exemplo de filter')
# print(novos_valores)
# impares = [valor for valor in valores if valor%2==1]
# print('Valores ímpares',impares)

# pares = [valor for valor in valores if valor%2==0]
# print('Valores ímpares',pares)

# numeros = [1,2,3,4,5,6,7,8,9,10]

# outro_if = [

#     numero if numero != 6
#     else 600
#     for numero in numeros
#     if numero %2 ==0 
# ]

# print(outro_if)

# numeros = [1,2,3,4,5,6,7,8,9,10]

# linhas_e_colunas = [ 
#     (x,y)
#     if y != 2 else 'Você não é 2'
#     for x in range(1,11)
#     for y in range(1,6)
#     if x != 2
# ]

# print(' ')
# print(' ')
# print(' ')
# print(' ')
# print(' ')
# linhas_e_colunas_multiplicacao = [ 
#     (x,y)
#     if y != 2 else (x*75,y*1000)
#     for x in range(1,11)
#     for y in range(1,6)
#     if x != 2
# ]
# print(linhas_e_colunas_multiplicacao)


# string = 'Otávio Miranda'
# numero_de_letras = 2
# nova_string = '.'.join([
#     string[indice:indice +  numero_de_letras]
#     for indice in range(0, len(string), numero_de_letras)
#     ])
# print(nova_string)

nomes = ['Otavio','Felipe','Yago','Maria']

# novos_nomes = [nome.lower() for nome in nomes]
# print(novos_nomes)
bugado = [
    f'{nome[:-1].lower()}{nome[-1].upper()}'
    for nome in nomes ]
print(bugado)