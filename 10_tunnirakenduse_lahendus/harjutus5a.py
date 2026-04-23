#10kg radiaator. 1 kraad soojenemist = 10 * 412 = 4120 J
#1 kW * 10sek = 10000J. 10000/4120 ~ 2,43 kraadi
#10 kraadi jahtumist - 41200 J 
# 41200 / 30 / 1245 = 1.1 kraadi toa õhk soojemaks

class Materjalikogus:
    def __init__(self, umass, uerisoojus, utemperatuur):
        self.mass=umass
        self.erisoojus=uerisoojus
        self.temperatuur=utemperatuur
    
    def kysiTemperatuur(self):
        return self.temperatuur
    
    def energiavahetus(self, j):
        self.temperatuur+=j/self.mass/self.erisoojus

class Ohukogus(Materjalikogus):
    def __init__ (self, pikkus, laius, korgus, temperatuur):
        super().__init__(pikkus*laius*korgus*1.23, 1012, temperatuur)

 
radiaator=Materjalikogus(10, 412, 20)
print(radiaator.kysiTemperatuur())

radiaator.energiavahetus(10000)
print(round(radiaator.kysiTemperatuur(), 2))

toaohk=Ohukogus(3, 4, 2.5, 20)
print(toaohk.kysiTemperatuur())
toaohk.energiavahetus(100000)
print(round(toaohk.kysiTemperatuur(), 2))
