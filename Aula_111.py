def soma(*args):
    total = 0
    for a in args:
        total+=a 
    return total 

print(soma(1,2,3,4,5))