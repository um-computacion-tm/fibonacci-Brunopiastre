class ImposibleBajarException(Exception):
    pass


class ImposibleSubirException(Exception):
    pass


class Ascensor:
    def __init__(self, cantidad_pisos):
        self.piso_actual = 0
        self.cantidad_pisos = cantidad_pisos
        self.auditoria = []

    def subir(self, pisos):
        nuevo_piso = self.piso_actual + pisos
        if nuevo_piso > self.cantidad_pisos:
            raise ImposibleSubirException("No se puede subir más del límite.")
        self.piso_actual = nuevo_piso
        self.auditoria.append(pisos)

    def bajar(self, pisos):
        nuevo_piso = self.piso_actual - pisos
        if nuevo_piso < 0:
            raise ImposibleBajarException("No se puede bajar menos de la PB.")
        self.piso_actual = nuevo_piso
        self.auditoria.append(-pisos)