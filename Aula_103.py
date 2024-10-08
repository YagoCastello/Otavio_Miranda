import random
#variables- variavéis
soma=0
lista=[]
contador=10
contador_2=11
soma_2=0
multiplicacao=[]


for d in range(0,9):
    valor =random.randint(0,9)
    lista.append(valor)

for d in lista:
    valor_multiplicacao=d*contador
    multiplicacao.append(valor_multiplicacao) 
    soma+= valor_multiplicacao
    contador-=1

resultado = (soma *10)%11

if resultado >9:
    lista.append(0)
else:
    lista.append(resultado)

#segundo digito
multiplicacao.clear
for d in lista:
    valor_multiplicacao=d*contador_2
    multiplicacao.append(valor_multiplicacao) 
    soma_2+= valor_multiplicacao
    contador_2-=1

resultado_2 = (soma_2 *10)%11

if resultado_2 >9:
    lista.append(0)
else:
    lista.append(resultado_2)
palavra=''
for n in lista:
    palavra+=str(n)
print(palavra)

def formatado(text):
    limpo=''
    for c in range(11):
        if c == 2 or c == 5 :
            limpo+=palavra[c]
            limpo+='.'
        elif c==8:
            limpo+=palavra[c]
            limpo+='-'
        else:
            limpo+=palavra[c]
    return limpo

print(formatado(palavra))