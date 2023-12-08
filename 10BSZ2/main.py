from module import *

emberek:list[Ember] = []

stream = open(file='adatok.txt', mode='r', encoding='utf-8')

for sor in stream:
    e:Ember = Ember(sor)
    emberek.append(e)

print('a következő embereknek van cicája:')
for e in emberek:
    if e.van_cica == 'igen':
        print(e.nev)

c:int = 0
for e in emberek:
    if '-07-' in e.szul:
        c += 1
print(f'{c} embernek van júliusban a születésnapja')

s:int = 0
for e in emberek:
    szul_ev:int = int(e.szul.split('-')[0])
    s += 2023 - szul_ev
print(f'átlagéletkor: {s / len(emberek)} év')