class Ember:
    def __init__(self, sor:str) -> None:
        adattagok:list[str] = sor.strip().split(';')
        nev:list[str] = adattagok[0].split(' ')
        self.kereszt_nev:str = nev[0]
        self.vezetek_nev:str = nev[1]
        datum:list[str] = adattagok[1].split('-')
        self.szul_ev:int = int(datum[0])
        self.szul_ho:int = int(datum[1])
        self.szul_nap:int = int(datum[2])
        self.van_cica:bool = adattagok[2] == 'igen'