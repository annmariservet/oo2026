class Kann:
    def __init__ (self, võimsus, veehulk, algtemperatuur):
        self.võimsus = võimsus
        self.veehulk = veehulk
        self.algtemperatuur = algtemperatuur
    def kuumutamine(self):
        aeg = (100 - self.algtemperatuur) * (self.veehulk / (4190 / self.võimsus))
        print(round(aeg, 2))

K=Kann(1000, 1, 20)
K.kuumutamine()    