import unittest

class Kalkulaator:
    sisu="0"
    def vajutus(self, nupp):
        nupp=[]
        self.sisu=nupp

    def ekraan(self):
        return self.sisu
    
    def clearlist(self):
        nupp.clear()

class TestKalkulaator(unittest.TestCase):
    k=Kalkulaator()

    def test_algus(self):
        self.assertEqual(self.k.ekraan(), "0")

    def test_vajutus_1(self):
        self.k.vajutus("1")
        self.assertEqual(self.k.ekraan(), "1")
    
    def test_vajutus_2(self):
        self.k.vajutus("2")
        self.assertEqual(self.k.ekraan(), "2")

    """ def test_vajutus_2(self):
        self.k.vajutus.append("1")
        self.k.vajutus.append("2")
        self.assertEqual(self.k.ekraan(), "12") """


suite = unittest.TestLoader().loadTestsFromTestCase(TestKalkulaator)
runner = unittest.TextTestRunner(verbosity=0)
result = runner.run(suite)
print(f'Tests run: {result.testsRun}')