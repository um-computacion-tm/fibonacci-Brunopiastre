import unittest
from ascensor import (
    Ascensor,
    ImposibleBajarException,
    ImposibleSubirException,
)

class TestAscensor(unittest.TestCase):
    def setUp(self):
        self.ascensor = Ascensor(10)

    def test_inicial(self):
        self.assertEqual(
            self.ascensor.piso_actual,
            0,
        )
        self.assertEqual(
            self.ascensor.cantidad_pisos,
            10,
        )

    def test_ir_piso_3(self):
        self.ascensor.subir(3)
        self.assertEqual(
            self.ascensor.piso_actual,
            3,
        )

    def test_ir_piso_5_en_2_pasos(self):
        self.ascensor.subir(3)
        self.ascensor.subir(2)
        self.assertEqual(
            self.ascensor.piso_actual,
            5,
        )

    def test_ir_piso_4_en_2_pasos(self):
        self.ascensor.subir(5)
        self.ascensor.bajar(1)
        self.assertEqual(
            self.ascensor.piso_actual,
            4,
        )

    def test_imposible_bajar_menos_cero(self):
        with self.assertRaises(ImposibleBajarException):
            self.ascensor.bajar(1)
        self.assertEqual(
            self.ascensor.piso_actual,
            0,
        )

    def test_imposible_bajar_menos_cero(self):
        self.ascensor.subir(1)
        with self.assertRaises(ImposibleBajarException):
            self.ascensor.bajar(2)
        self.assertEqual(
            self.ascensor.piso_actual,
            1,
        )

    def test_imposible_subir_mas_del_limite(self):
        with self.assertRaises(ImposibleSubirException):
            self.ascensor.subir(11)
        self.assertEqual(
            self.ascensor.piso_actual,
            0,
        )

    def test_imposible_subir_mas_del_limite_incremental(self):
        self.ascensor.subir(5)
        with self.assertRaises(ImposibleSubirException):
            self.ascensor.subir(6)
        self.assertEqual(
            self.ascensor.piso_actual,
            5,
        )

    def test_auditoria(self):
        self.assertEqual(
            self.ascensor.auditoria,
            [],
        )
        self.ascensor.subir(1)
        self.ascensor.subir(3)
        with self.assertRaises(ImposibleSubirException):
            self.ascensor.subir(8)
        self.ascensor.bajar(2)
        with self.assertRaises(ImposibleBajarException):
            self.ascensor.bajar(5)
        self.assertEqual(
            self.ascensor.auditoria,
            [1, 3, -2],
        )

if __name__ == '__main__':
    unittest.main()