# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# def duplica(num):
#     return num*2

# def triplica(num):
#     return num*3

# def quadriplica(num):
#     return num*4


# print(duplica(5))
# print(triplica(5))
# print(quadriplica(5))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


vezes5 = criar_multiplicador(5)
vezes3 = criar_multiplicador(3)
print(vezes5(7))
print(vezes3(8))