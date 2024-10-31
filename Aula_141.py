# Dictionary Comprehension e Set Comprehension
def pula_linha():
    print(' ')
    print(' ')
    

produto = {
    'nome' : 'Caneta Azul',
    'preco':2.5,
    'categoria':'Escritório',
}

dc = {
    chave: valor.upper()
    if isinstance(valor,str) else valor 
    for chave, valor 
    in produto.items()
}

print(dc)
pula_linha()

cd = {
    chave: valor
    if isinstance(valor,(int,float)) else valor.upper() 
    for chave, valor 
    in produto.items()
}

print(cd)
pula_linha()

lista = [
    ('a','valor a'),
    ('b','valor b'),
    ('c','valor c'),
]

ac = {
    chave:valor 
    for chave, valor in lista
}
dicionario = dict(lista)
print(ac)

print()
print(dicionario)

#setssssssssssssssssssssssssssssssssssssssssss

s1 = { i for i in range(10)}
s2= set(range(10))
print(f's1 = {s1}')
print(f's2 = {s2}')