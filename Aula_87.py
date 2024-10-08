nomes = ['pedro','ana','claudia']
nomes1,nomes2,nomes3 = nomes
print(nomes1)


nome1,nome2,nome3 = ['pedro','ana','claudia']
print(nome2)
pessoa1,*resto  = ['pedro','ana','claudia']
print(resto)
print(pessoa1)

#USO DO UNDERLINE _ Normalmente é usado pra dizer que você não pretende usar essa variável


pessoas1,*_ = ['pedro','ana','claudia']
print(_)
print(pessoas1)
print('separação das strings')

_,pessoas2,*_ = ['pedro','ana','claudia','janaina']
print(_)
print(pessoas2)