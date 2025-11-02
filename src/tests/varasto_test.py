import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_konstruktori_negatiivinen_tilavuus_nollautuu(self):
        varasto = Varasto(-1)
        self.assertAlmostEqual(varasto.tilavuus, 0)
    
    def test_konstruktori_negatiivinen_alkusaldo_nollataan(self):
        varasto = Varasto(10, -5)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_lisays_negatiivinen_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_yli_tilavuuden_tayttaa(self):
        self.varasto.lisaa_varastoon(100)
        self.assertAlmostEqual(self.varasto.saldo, 10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_ottaminen_negatiivinen_palauttaa_nolla_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(3)
        saatu = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(saatu, 0.0)
        self.assertAlmostEqual(self.varasto.saldo, 3)

    def test_ottaminen_yli_saldon_tyhjentaa(self):
        self.varasto.lisaa_varastoon(3)
        saatu = self.varasto.ota_varastosta(5)
        self.assertAlmostEqual(saatu, 3)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_str_palauttaa_saldon_ja_tilan(self):
        varasto = Varasto(10, 10)
        self.assertEqual(str(varasto), "saldo = 10, vielä tilaa 0")
