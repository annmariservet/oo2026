class Kann:
    def __init__ (self, veehulk, väli_temp, kann_temp):
        if veehulk > 2:
            raise ValueError("Kann mahutab kuni kaks liitrit.")
        else:
            self.veehulk = veehulk
            self.väli_temp = väli_temp
            self.kann_temp = kann_temp
        self.energia_kraadi_kohta = 104.75
        
    def jahtumine_100s(self):
        temp_erinevus = self.kann_temp - self.väli_temp
        eraldunud_energia = temp_erinevus * self.energia_kraadi_kohta
        jahtumine = eraldunud_energia / (self.veehulk * 4190)
        self.kann_temp -= jahtumine

    def simuleeri_jahtumist(self, aeg_sekundites):
        sammud=aeg_sekundites // 100
        for i in range(sammud):
            self.jahtumine_100s()
            print((i+1)*100, self.kann_temp)

kann = Kann(2, 100, 20)
kann.simuleeri_jahtumist(800)

kann2 = Kann(2.2, 100, 20)
kann.simuleeri_jahtumist(800)
