import unittest
from varasto import Varasto

"""Pääluokka"""
class TestVarasto(unittest.TestCase):
    #SetUp funktio
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(-5)
        self.varasto3 = Varasto(5, -5)
        self.varasto4 = Varasto(5, 10)
    #Tyhjän varaston testaus
    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)
    #Oikean tilavuuden testaus
    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
    #Lisäyksen testaus
    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)
    #Tilan muutoksen testaus
    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)
    #Ottamisen testaus
    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)
    #Tilan lisäyksen testaus
    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    #Negatiivisen tilavuuden testaus
    def test_tilavuus_pienempi_kuin_nolla(self):
        self.assertAlmostEqual(self.varasto2.tilavuus, 0)
    #Negatiivisen saldon testaus
    def test_alku_saldo_pienempi_kuin_nolla(self):
        self.assertAlmostEqual(self.varasto3.saldo, 0)
    #Suuremman saldon kuin tilavuus testaus
    def test_alku_saldo_suurempi_kuin_tilavuus(self):
        self.assertAlmostEqual(self.varasto4.saldo, self.varasto4.tilavuus)
    #Negatiivisen lisäyksen testaus
    def test_lisays_pienempi_kuin_nolla(self):
        self.varasto.lisaa_varastoon(-5)

        self.assertAlmostEqual(self.varasto.saldo, 0)
    #Tilavuuden puutteen testaus
    def test_lisays_pienempi_kuin_tilavuus(self):
        self.varasto.lisaa_varastoon(15)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)
    #Negatiivisen ottamisen testaus
    def test_ota_varastosta_pienempi_kuin_nolla(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-5), 0.0)
    #Suuremman ottamisen kuin saldon testaus
    def test_ota_varastosta_maara_suurempi_kuin_saldo(self):
        self.varasto.ota_varastosta(5)

        self.assertAlmostEqual(self.varasto.saldo, 0.0)
    #Voiko ottaa kaiken
    def test_kaikki_mita_voidaan(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(5), 0)
    #STR testaus
    def test_str_palauttaa_oikein(self):
        self.assertAlmostEqual(self.varasto.__str__(), "saldo = 0, vielä tilaa 10")
