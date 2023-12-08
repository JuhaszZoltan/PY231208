from module import *

stream = open(file='adatok.txt', mode='r', encoding='utf-8')

emberek:list[Ember] = []
for sor in stream:
    e:Ember = Ember(sor)
    emberek.append(e)

print('akinek van cicája:')
for e in emberek:
    if e.van_cica == 'igen':
        print(f'\t- {e.nev}')

s:int = 0
for e in emberek:
    szu_ev:int = int(e.szul.split('-')[0])
    s += 2023 - szu_ev
print(f'emberek átlagéletkora: {s/len(emberek)} év')

c:int = 0
for e in emberek:
    if '-07-' in e.szul:
        c += 1
print(f'összesen {c} embernek van júliusban a születésnapja')