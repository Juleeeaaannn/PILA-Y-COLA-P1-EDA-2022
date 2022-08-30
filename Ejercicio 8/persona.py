class Persona:
    especialidad=None
    tiempo=None
    def __init__(self,especialidad,tiempo):
        if especialidad == 0:
            self.__especialidad="Ginecologia"
        if especialidad == 1:
            self.__especialidad="Clinica medica"
        if especialidad == 2:
            self.__especialidad="Oftalmologia"
        if especialidad == 3:
            self.__especialidad="Pediatria"
        self.__tiempo=tiempo
    def Especialidad(self):
        return self.__especialidad
    def Tiempo(self):
        return self.__tiempo
    def setTiempo(self, tiempo):
        self.__tiempo=tiempo
