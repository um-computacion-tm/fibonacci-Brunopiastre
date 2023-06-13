import unittest
from maquina_cafe import MaquinaCafe

from maquinacafe_base import (
    RecetaIncompleta,
    NoHayMonedaException,
    NoHayVasoException,
)

class TestMaquinaCafe(unittest.TestCase):

    def setUp(self):
        self.maquina = MaquinaCafe()

    def test_inicial(self):
        self.assertEqual(self.maquina.vasos, 0)
        self.assertEqual(self.maquina.cafe, 0)
        self.assertEqual(self.maquina.leche, 0)
        self.assertEqual(self.maquina.agua, 0)
        self.assertEqual(self.maquina.monedas, 0)

    def test_cafe_solo(self):
        self.maquina.vasos = 10
        self.maquina.cafe = 200
        self.maquina.agua = 1000
        self.maquina.monedas = 3
        self.maquina.leche = 500
        self.maquina.hacer_cafe_solo()
        self.assertEqual(self.maquina.vasos, 9)
        self.assertEqual(self.maquina.cafe, 150)
        self.assertEqual(self.maquina.agua, 900)
        self.assertEqual(self.maquina.monedas, 2)
        self.assertEqual(self.maquina.leche, 500)

    def test_cafe_solo_sin_moneda(self):
        self.maquina.vasos = 10
        self.maquina.cafe = 200
        self.maquina.agua = 1000
        self.maquina.monedas = 0
        self.maquina.leche = 500

        with self.assertRaises(NoHayMonedaException):
            self.maquina.hacer_cafe_solo()

        self.assertEqual(self.maquina.vasos, 10)
        self.assertEqual(self.maquina.cafe, 200)
        self.assertEqual(self.maquina.agua, 1000)
        self.assertEqual(self.maquina.monedas, 0)
        self.assertEqual(self.maquina.leche, 500)

    def test_cafe_solo_sin_agua(self):
        self.maquina.vasos = 10
        self.maquina.cafe = 200
        self.maquina.agua = 99
        self.maquina.monedas = 1
        self.maquina.leche = 500

        with self.assertRaises(RecetaIncompleta):
            self.maquina.hacer_cafe_solo()

        self.assertEqual(self.maquina.vasos, 10)
        self.assertEqual(self.maquina.cafe, 200)
        self.assertEqual(self.maquina.agua, 99)
        self.assertEqual(self.maquina.monedas, 1)
        self.assertEqual(self.maquina.leche, 500)

    def test_cafe_solo_sin_vaso(self):
        self.maquina.vasos = 0
        self.maquina.cafe = 200
        self.maquina.agua = 100
        self.maquina.monedas = 1
        self.maquina.leche = 500

        with self.assertRaises(NoHayVasoException):
            self.maquina.hacer_cafe_solo()

        self.assertEqual(self.maquina.vasos, 0)
        self.assertEqual(self.maquina.cafe, 200)
        self.assertEqual(self.maquina.agua, 100)
        self.assertEqual(self.maquina.monedas, 1)
        self.assertEqual(self.maquina.leche, 500)

    def test_cafe_solo_sin_cafe(self):
        self.maquina.vasos = 1
        self.maquina.cafe = 49
        self.maquina.agua = 100
        self.maquina.monedas = 1
        self.maquina.leche = 500

        with self.assertRaises(RecetaIncompleta):
            self.maquina.hacer_cafe_solo()

        self.assertEqual(self.maquina.vasos, 1)
        self.assertEqual(self.maquina.cafe, 49)
        self.assertEqual(self.maquina.agua, 100)
        self.assertEqual(self.maquina.monedas, 1)
        self.assertEqual(self.maquina.leche, 500)

    def test_hacer_cafe_con_leche(self):
        self.maquina.vasos = 1
        self.maquina.cafe = 100
        self.maquina.agua = 200
        self.maquina.monedas = 1
        self.maquina.leche = 500

        self.maquina.hacer_cafe_con_leche()

        self.assertEqual(self.maquina.vasos, 0)
        self.assertEqual(self.maquina.cafe, 75)
        self.assertEqual(self.maquina.agua, 120)
        self.assertEqual(self.maquina.monedas, 0)
        self.assertEqual(self.maquina.leche, 480)

    def test_cafe_con_leche_sin_leche(self):
        self.maquina.vasos = 1
        self.maquina.cafe = 50
        self.maquina.agua = 100
        self.maquina.monedas = 1
        self.maquina.leche = 10

        with self.assertRaises(RecetaIncompleta):
            self.maquina.hacer_cafe_con_leche()

        self.assertEqual(self.maquina.vasos, 1)
        self.assertEqual(self.maquina.cafe, 50)
        self.assertEqual(self.maquina.agua, 100)
        self.assertEqual(self.maquina.monedas, 1)
        self.assertEqual(self.maquina.leche, 10)

    def test_cafe_con_leche_sin_moneda(self):
        self.maquina.vasos = 1
        self.maquina.cafe = 50
        self.maquina.agua = 100
        self.maquina.monedas = 0
        self.maquina.leche = 50

        with self.assertRaises(NoHayMonedaException):
            self.maquina.hacer_cafe_con_leche()

        self.assertEqual(self.maquina.vasos, 1)
        self.assertEqual(self.maquina.cafe, 50)
        self.assertEqual(self.maquina.agua, 100)
        self.assertEqual(self.maquina.monedas, 0)
        self.assertEqual(self.maquina.leche, 50)

    def test_cafe_con_leche_sin_cafe(self):
        self.maquina.vasos = 1
        self.maquina.cafe = 20
        self.maquina.agua = 100
        self.maquina.monedas = 1
        self.maquina.leche = 50

        with self.assertRaises(RecetaIncompleta):
            self.maquina.hacer_cafe_con_leche()

        self.assertEqual(self.maquina.vasos, 1)
        self.assertEqual(self.maquina.cafe, 20)
        self.assertEqual(self.maquina.agua, 100)
        self.assertEqual(self.maquina.monedas, 1)
        self.assertEqual(self.maquina.leche, 50)

    def test_cafe_con_leche_sin_agua(self):
        self.maquina.vasos = 1
        self.maquina.cafe = 50
        self.maquina.agua = 79
        self.maquina.monedas = 1
        self.maquina.leche = 50

        with self.assertRaises(RecetaIncompleta):
            self.maquina.hacer_cafe_con_leche()

        self.assertEqual(self.maquina.vasos, 1)
        self.assertEqual(self.maquina.cafe, 50)
        self.assertEqual(self.maquina.agua, 79)
        self.assertEqual(self.maquina.monedas, 1)
        self.assertEqual(self.maquina.leche, 50)

if __name__ == '__main__':
    unittest.main()
