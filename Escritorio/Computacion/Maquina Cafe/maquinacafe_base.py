CAFE = 'cafe'
AGUA = 'agua'
LECHE = 'leche'
CHOCOLATE = 'chocolate'
TE = 'te'

RECETAS = {
    'cafe':{
        CAFE: 50,
        AGUA: 100,
    },
    'cafe con leche':{
        CAFE: 25,
        AGUA: 80,
        LECHE: 20,
    },
    'chocolate':{
        CHOCOLATE: 50,
        LECHE: 100,
    },
    'te':{
        TE: 1,
        AGUA: 100,
    },
}

class RecetaIncompleta(Exception):
    pass

class NoHayMonedaException(Exception):
    pass

class NoHayVasoException(Exception):
    pass



class MaquinaCafeBase:
    def __init__(self): # CONSTRUCTOR!!!!
        self.vasos = 0
        self.cafe = 0
        self.leche = 0
        self.agua = 0
        self.monedas = 0

    def validar(self, receta_hacer):
        for elemento, cantidad in receta_hacer.items():
            if getattr(self, elemento) < cantidad:
                raise RecetaIncompleta('sin ' + elemento)
            # if elemento == CAFE and cantidad > self.cafe:
            #     raise RecetaIncompleta('sin cafe')
            # if elemento == AGUA and cantidad > self.agua:
            #     raise RecetaIncompleta('sin agua')
            # if elemento == LECHE and cantidad > self.leche:
            #     raise RecetaIncompleta('sin leche')

        if self.monedas == 0:
            raise NoHayMonedaException()

        if self.vasos == 0:
            raise NoHayVasoException()

    def hacer(self, pedido):
        receta_hacer = RECETAS[pedido]

        self.validar(receta_hacer)

        self.vasos -= 1
        self.monedas -= 1

        for elemento, cantidad in receta_hacer.items():
            if elemento == CAFE:
                self.cafe -= cantidad
            if elemento == AGUA:
                self.agua -= cantidad
            if elemento == LECHE:
                self.leche -= cantidad

