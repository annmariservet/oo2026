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
        
radiaator=Materjalikogus(10, 412, 20)
print(radiaator.kysiTemperatuur())