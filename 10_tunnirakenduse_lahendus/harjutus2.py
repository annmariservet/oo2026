class Kann:
    def __init__ (self, välistemperatuur, kontroll_kannutemperatuur, jahtumine_30s):
        self.välistemperatuur = float(välistemperatuur)
        erinevus = float(kontroll_kannutemperatuur) - self.välistemperatuur
        self.k = float(jahtumine_30s) / erinevus
    def jahtumine(self, hetke_kannutemperatuur):
        jahtunudkraadid = self.k * (float(hetke_kannutemperatuur) - self.välistemperatuur)
        return round(jahtunudkraadid, 2)

kelder = Kann(10, 25, 5)
print(kelder.jahtumine(5))
kann = Kann(15, 20, 15)
print(kann.jahtumine(8))