from time import time
import string
import itertools

pwd = '12345'


def brute(password):
    lista = string.digits #+ string.ascii_lowercase + string.ascii_uppercase
    brKomb = 8
    pokusaji = 0

    for pwdLen in range(1, brKomb + 1):
        for odabir in itertools.product(lista, repeat=pwdLen):
            pokusaji += 1
            odabir = ''.join(odabir)
            if(odabir == password):
                return 'Lozinka {}. je pronadena nakon {} pokusaja.'.format(odabir, pokusaji)

start = time()
print(brute(pwd))
end = time()
print('Vrijeme je: %.2f sekundi' % (end  - start))
