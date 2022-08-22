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
            print(self.__items[variable-1],end='')
            variable-=1
        print('||',end='\t')
    def MostrarUltima(self):
        if self.Vacia():
            retorna=0
            print('lista vacia!')
        else:
            retorna=self.__items[self.__tope-1]
        return retorna
if __name__=='__main__':
    pila1=Pila()
    pila2=Pila()
    pila3=Pila()
    i=0
    band=1
    while i!=-1:
        canti=int(input('Ingrese cantidad de discos para jugar:'))
        j=canti
        while j>=1:
            pila1.Apilar(j)
            j-=1
        movimiento=int(input('Ingrese a que pila desea mover el primer disco(no se puede mover a la 1):'))
        if movimiento==2:
            ultimodisco=pila1.Desapilar()
            pila2.Apilar(ultimodisco)
        elif movimiento==3:
            ultimodisco=pila1.Desapilar()
            pila3.Apilar(ultimodisco)
        else:
            print('numero incorrecto!')
        while band!=0:
            disco=int(input('Ingrese la torre donde esta el disco que desea mover:'))
            movimiento=int(input('Ingrese a que torre desea mover el disco:'))
            if disco==1 and not pila1.Vacia():
                torreinicio=pila1.MostrarUltima()#cargo ficha que voy a mover
                if movimiento==2:
                    if pila2.Vacia():
                        torreinicio=0
                    if pila2.MostrarUltima() >= torreinicio:
                            disco=pila1.Desapilar()
                            pila2.Apilar(disco)
                    else:
                        print('El disco que quiere mover es mas chico que el disco que esta en la torre de destino')
                elif movimiento==3:
                    if pila3.Vacia():
                        torreinicio=0
                    torredestino=pila3.MostrarUltima()
                    if torredestino >= torreinicio:
                            disco=pila1.Desapilar()
                            pila3.Apilar(disco)
                    else:
                        print('El disco que quiere mover es mas chico que el disco que esta en la torre de destino')
                else:
                    print('EL DISCO QUE QUIERE INGRESAR ES MAS chico QUE EL QUE ESTA!!!!!!!!!!!')
            elif disco==2 and not pila2.Vacia():
                torreinicio=pila2.MostrarUltima() #cargo ficha que voy a mover
                if movimiento==1:
                    if pila1.Vacia():
                        torreinicio=0
                    if pila1.MostrarUltima()>=torreinicio :
                            disco=pila2.Desapilar()
                            pila1.Apilar(disco)
                    else:
                        print('El disco que quiere mover es mas chico que el disco que esta en la torre de destino')
                elif movimiento==3:
                    if pila3.Vacia():
                        torreinicio=0
                    if pila3.MostrarUltima()>=torreinicio:
                            disco=pila2.Desapilar()
                            pila3.Apilar(disco)
                    else:
                        print('El disco que quiere mover es mas chico que el disco que esta en la torre de destino')
                else:
                    print('EL DISCO QUE QUIERE INGRESAR ES MAS chico QUE EL QUE ESTA!!!!!!!!!!!')
            elif disco==3 and not pila3.Vacia():
                torreinicio=pila3.MostrarUltima()
                if movimiento==1:
                    if pila1.Vacia():
                        torreinicio=0
                    if pila1.MostrarUltima()>=torreinicio:
                            disco=pila3.Desapilar()
                            pila1.Apilar(disco)
                elif movimiento==2:
                    if pila2.Vacia():
                        torreinicio=0
                    if pila2.MostrarUltima()>=torreinicio :
                            disco=pila3.Desapilar()
                            pila2.Apilar(disco)
                    else:
                        print('El disco que quiere mover es mas chico que el disco que esta en la torre de destino')
                else:
                    print('EL DISCO QUE QUIERE INGRESAR ES MAS chico QUE EL QUE ESTA!!!!!!!!!!!')
            else:
                print('no entro a ninguna torre')
            if pila1.Vacia() and pila2.Vacia():
                band=0
            pila1.Mostrar()
            pila2.Mostrar()
            pila3.Mostrar()
            print('')
