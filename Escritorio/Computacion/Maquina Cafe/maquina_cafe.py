from maquinacafe_base import MaquinaCafeBase

class NoHayMonedaException(Exception):
    pass


class NoHayAguaException(Exception):
    pass

class NoHayVasoException(Exception):
    pass


class NoHayCafeException(Exception):
    pass


class NoHayLecheException(Exception):
    pass

AGUA_MINIMO = 100
CAFE_MINIMO = 50
LECHE_MINIMO = 50


class MaquinaCafe(MaquinaCafeBase):

    # def validar_cantidades_cafe_solo(self, cantidad_cafe):
    #     if self.monedas == 0:
    #         raise NoHayMonedaException()
    #     if self.agua < AGUA_MINIMO:
    #         raise NoHayAguaException()
    #     if self.vasos == 0:
    #         raise NoHayVasoException()
    #     if self.cafe < cantidad_cafe:
    #         raise NoHayCafeException()

    # def descontar_cantidades_cafe_solo(self):
    #     self.monedas -= 1
    #     self.agua -= AGUA_MINIMO
    #     self.vasos -= 1
    #     self.cafe -= CAFE_MINIMO

    def hacer_cafe_con_leche(self):
        self.hacer('cafe con leche')
        # self.validar_cantidades_cafe_solo(cantidad_cafe=25)
        # if self.leche < LECHE_MINIMO:
        #     raise NoHayLecheException()

        # self.descontar_cantidades_cafe_solo()
        # self.leche -= LECHE_MINIMO

    def hacer_cafe_solo(self):
        self.hacer('cafe')
        # self.validar_cantidades_cafe_solo(cantidad_cafe=CAFE_MINIMO)
        # self.descontar_cantidades_cafe_solo()
