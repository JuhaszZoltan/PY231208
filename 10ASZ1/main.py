from module import *

emberek:list[Ember] = []
stream = open(file=' ', mode='r', encoding='utf-8')

for sor in stream:
    adattagok:list[str] = sor.strip().split(';')
    n:str = adattagok[0]
    sz:str = adattagok[1]
    van:bool = adattagok[2] == 'igen'
    ember:Ember = Ember(n, sz, van)
    emberek.append(ember)

for e in emberek:
    print(e.nev)

c:int = 0
for e in emberek:
    if e.van_cicaja == True:
        c += 1
print(f'összesen {c} embernek van cicája')