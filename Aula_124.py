perguntas = [
    {
        'Pergunta':'Quanto é 2+2? ',
        'Opções': ['1','2','3','4'],
        'resposta' :'4'
    },{
        'Pergunta':'Quanto é 5*5? ',
        'Opções': ['25','55','10','51'],
        'resposta' :'25'
    },{
        'Pergunta':'Quanto é 10/2? ',
        'Opções': ['4','5','2','1'],
        'resposta' :'5'
    },
    ]
acertos = 0
contador = 0
while True:
    
    for dici in perguntas:
        contador +=1
        for chave, valor in dici.items():
            if chave == 'resposta':
                ...
            else:
                print(chave,valor)
        
        usuario = input('Qual é a sua resposta: ')
        if usuario == valor:
            acertos +=1
            print('Você acertou')
        else:
            print('Você errou!')
    if contador >= 3:
        break

print('')
print('-='*20)    
print(f'Você acertou {acertos} questões.')
print('-='*20)    