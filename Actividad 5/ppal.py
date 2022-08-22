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
        print('--------------')
        print('|w|')
        variable=self.__tope
        while(variable!=0):
            print(self.__items[variable-1])
            variable-=1
        print('--------------')
    def MostrarUltima(self):
        if self.Vacia():
            retorna=0
        else:
            retorna=self.__items[self.__tope-1]
        return retorna
if __name__=='__main__':
    pila1=Pila()
    pila2=Pila()
    pila3=Pila()
    i=0
    while i!=-1:
        canti=int(input('Ingrese cantidad de discos para jugar:'))
        j=0
        while j!=canti:
            pila1.Apilar(j+1)
            j+=1
        movimiento=int(input('Ingrese a que pila desea mover el primer disco(no se puede mover a la 1):'))
        if movimiento==2:
            ultimodisco=pila1.Desapilar()
            pila2.Apilar(ultimodisco)
        elif movimiento==3:
            ultimodisco=pila1.Desapilar()
            pila3.Apilar(ultimodisco)
        else:
            print('numero incorrecto!')
        while movimiento!=0:
            disco=int(input('Ingrese la torre donde esta el disco que desea mover:'))
            movimiento=int(input('Ingrese a que torre desea mover el disco:'))
            if disco==1 and not pila1.Vacia():
                anterior=pila1.MostrarUltima()
                if movimiento==2:
                    if pila2.Vacia():
                        anterior=0
                    if anterior <= pila2.MostrarUltima():
                            disco=pila1.Desapilar()
                            pila2.Apilar(disco)
                elif movimiento==3:
                    if pila3.Vacia():
                        anterior=0
                    if anterior <= pila3.MostrarUltima():
                            disco=pila1.Desapilar()
                            pila3.Apilar(disco)
                else:
                    print('EL DISCO QUE QUIERE INGRESAR ES MAS GRANDE QUE EL QUE ESTA!!!!!!!!!!!')
            elif disco==2 and not pila2.Vacia():
                anterior=pila2.MostrarUltima()
                if movimiento==1:
                    if pila1.Vacia():
                        anterior=0
                    if anterior <= pila1.MostrarUltima():
                            disco=pila2.Desapilar()
                            pila1.Apilar(disco)
                elif movimiento==3:
                    if pila3.Vacia():
                        anterior=0
                    if anterior <= pila3.MostrarUltima():
                            disco=pila2.Desapilar()
                            pila3.Apilar(disco)
                else:
                    print('EL DISCO QUE QUIERE INGRESAR ES MAS GRANDE QUE EL QUE ESTA!!!!!!!!!!!')
            elif disco==3 and not pila3.Vacia():
                anterior=pila3.MostrarUltima()
                if movimiento==1:
                    if pila1.Vacia():
                        anterior=0
                    if anterior > pila1.MostrarUltima():
                            disco=pila3.Desapilar()
                            pila1.Apilar(disco)
                elif movimiento==2:
                    if pila2.Vacia():
                        anterior=0
                    if anterior > pila2.MostrarUltima():
                            disco=pila3.Desapilar()
                            pila2.Apilar(disco)
                else:
                    print('EL DISCO QUE QUIERE INGRESAR ES MAS GRANDE QUE EL QUE ESTA!!!!!!!!!!!')
            else:
                print('no entro a ninguna torre')
            pila1.Mostrar()
            pila2.Mostrar()
            pila3.Mostrar()

            