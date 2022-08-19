from tkinter import Variable
import numpy as np
class Memoria:
    __topesecu=0
    __topesecu2=5

    def __init__(self):
        self.__arreglo=np.empty(self.__topesecu2)
        
    def ApilaSecu(self,elemento):
        if self.__topesecu < self.__topesecu2:
            self.__arreglo[self.__topesecu]=elemento
            self.__topesecu+=1
        else:
            print('error!!')

    def ApilaSecu2(self,elemento):
        if self.__topesecu < self.__topesecu2:
            self.__arreglo[self.__topesecu2-1]=elemento
            self.__topesecu2-=1
        else:
            print('error!!')
    def desapilaSecu(self):
        self.__arreglo[self.__topesecu-1]=0
        self.__topesecu-1
    def desapilaSecu2(self):
        self.__arreglo[self.__topesecu2]=0
        self.__topesecu2+1
    def Mostrar(self):
        print(self.__arreglo)
if __name__=='__main__':
    memoria1=Memoria()
    i=-1
    while(i!=0):
        i=int(input('Ingrese elementos(finalizar con 0):'))
        if(i!=0):
            memoria1.ApilaSecu(i)
    i=1
    while(i!=0):
        i=int(input('Ingrese elementos del segundo arreglo(finalizar con 0):'))
        if(i!=0):
            memoria1.ApilaSecu2(i)
    memoria1.Mostrar()
    memoria1.desapilaSecu()
    memoria1.desapilaSecu2()
    memoria1.Mostrar()
    
    