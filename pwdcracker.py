from time import time
pwd = '1234'


def brute(password):
    lista = '1234567890abcdefghijklmnopqrstuvwxyz'
    a = []

    for current in range(len(password)):
        a = [i for i in lista]
        for y in range(current):
            a = [x+i for i in lista for x in a]
    print(a.index(password))

start = time()
brute(pwd)
end = time()
print('Vrijeme je: %.2f sekundi' % (end  - start))
