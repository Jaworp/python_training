class human:
    imie = ""
    wiek=None

    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek=wiek
    def witaj(self):
        print("Cześć, mam na imie ", self.imie)
czl=human
czl.imie = "Stef"
czl.wiek=22
print(czl.imie, czl.wiek)
