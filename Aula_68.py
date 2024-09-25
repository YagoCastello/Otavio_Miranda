"""Calculadora com while"""

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    
    numero_validos = None

    num_1_float = 0
    num_2_float = 0
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numero_validos = True
    except:
        numero_validos = None
        
    if numero_validos is None:
        print('Um ou ambos os números digitados são inválidos')
        continue
    
    operadores_permitidos = '+-*/'
    
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    print('Realizando sua conta.')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = {num_1_float + num_2_float}')
    elif operador == '-':
        print(f'{num_1_float } - {num_2_float} = {num_1_float-num_2_float}' )
    elif operador == '/':
        print(f'{num_1_float} / {numero_2} = {num_1_float / num_2_float}')
    elif operador == '*':
        print(f'{num_1_float} * {numero_2} = {num_1_float * num_2_float}')
    else:
        print('Nunca deveria chegar aqui.')
        
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break