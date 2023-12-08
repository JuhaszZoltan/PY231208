class Ember:
    def __init__(self, adatsor:str) -> None:
        adattagok:list[str] = adatsor.strip().split(';')
        self.nev:str = adattagok[0]
        self.szul:str = adattagok[1]
        self.van_cica:str = adattagok[2]