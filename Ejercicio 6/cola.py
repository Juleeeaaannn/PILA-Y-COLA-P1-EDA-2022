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
    def Vacia(self):
        retorna=False
        if self.__canti!=0:
            retorna=True
        return retorna
    def agregar(self,elemento):
        if self.__canti<self.__max:
            self.__items[self.__ul] = elemento
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
            self.__cant -= 1
        return x
    def recorrer(self):
        s = ""
        if not self.vacia():
            for i in range(self.__cant):
                s = s + str(self.__items[i]) + ", "
            return s
        else:
            print("La cola se encuentra vacía")
    