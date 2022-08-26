from tokenize import String
import numpy as np
class Cola:
    __items=None
    __max=0
    __pr=0
    __ul=0
    __canti=0
    def __init__(self,max=20):
        self.__items=np.empty(max)
        self.__max=max
        self.__pr=0
        self.__ul=0
        self.__canti=0
    def vacia(self):
        bandera = True
        if self.__canti != 0:
            bandera = False
        return bandera
    def agregar(self,elemento):
        if self.__canti<self.__max:
            self.__items[self.__ul]=elemento
            self.__ul += 1
            self.__canti += 1
        else: 
            print("La cola se encuentra llena")
    def suprimir(self):
        x = None
        if self.vacia():
            print("La cola se encuentra vacía")
        else:
            x = self.__items[self.__pr]
            self.__items[self.__pr] = 0
            self.__pr = (self.__pr+1)%self.__max
            self.__canti -= 1
        return x
    def recorrer(self):
        s = ""
        if not self.vacia():
            for i in range(self.__canti):
                s = s + str(self.__items[i]) + ", "
            return s
        else:
            print("La cola se encuentra vacía")
if __name__=='__main__':
    #Una entidad bancaria que realiza el cobro de servicios,
    #habilita una caja que atiende a una cola de clientes. 
    #Cada cliente avanza para realizar su pago cuando la caja está desocupada.
    #Considerar que el tiempo de atención del cajero es de 5 minutos y la frecuencia de llegada de los clientes es de 2 minutos.
    #Realizar un programa que simule esta realidad.
    #Obtener el tiempo máximo de espera de los clientes en la cola.
    #Nota: Ingresar el tiempo de atención de cajero y la frecuencia de llegada de los clientes a la cola.
    cola=Cola()
    band=int(input('ingrese tiempo de simulacion:'))
    atencion=int(input('Ingrese tiempo de atencion:'))
    frecuencia=int(input('Ingrese tiempo de llegada de las personas:'))
    minutos=0
    espera=0
    cantipersonas=0
    cajeroVacio=True
    for minutos in range(band):
        print(minutos)
        if minutos % frecuencia == 0 and cajeroVacio == True:
            cola.agregar(minutos)
            print('persona agregada')
        if minutos % atencion == 0:
            cajeroVacio=True
            x=cola.suprimir()
            espera=minutos-x
            print('persona atendida')

    print('el tiempo de espera de las personas es de {} minutos'.format(espera))
