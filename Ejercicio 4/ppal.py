class Pila:
    __items=[]
    __tope=0

    def __init__(self):
        self.__items=[]
        
    def Vacia(self):
        return self.__items == []

    def Apilar(self,elemento):
        self.__items.append(elemento)
        self.__tope+=1

    def Desapilar(self):
        self.__tope-=1
        return self.__items.pop()

    def Mostrar(self):
        variable=self.__tope
        while(variable!=0):
            print(self.__items[variable-1])
            variable-=1

if __name__=='__main__':
    pass