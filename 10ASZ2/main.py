from module import *

emberek:list[Ember] = []
stream = open(file='adatok.txt', mode='r', encoding='utf-8')

for row in stream:
    ember:Ember = Ember(row)
    emberek.append(ember)

c:int = 0
for e in emberek:
    if e.van_cica:
        c += 1
print(f'összesen {c} embernek van cicája')

keresztnevek:list[str] = []
for e in emberek:
    keresztnevek.append(e.kereszt_nev)
keresztnevek.sort()
print(keresztnevek)
















# name:str = 'Zoltan'
# stream.write(f'Hello, {name}!\n')