lista = ['nasa','pato','casa','bolo','nasa','pato','casa','bolo']
meu_SET = {}
for item in lista:
    if item not in meu_SET:
        meu_SET.update(item)
        print(item)