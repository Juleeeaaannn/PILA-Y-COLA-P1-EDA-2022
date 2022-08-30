from calendar import c
import random
import numpy as np
from persona import Persona
class Cola:
    __items=None
    __max=0
    __pr=0
    __ul=0
    __canti=0
    def __init__(self,max=20):
        self.__items=np.empty(max,dtype=Persona)
        self.__max=max
        self.__pr=0
        self.__ul=0
        self.__canti=0
    def Vacia(self):
        bandera = True
        if self.__canti != 0:
            bandera = False
        return bandera
    def Agregar(self,elemento):
        if self.__canti<self.__max:
            self.__items[self.__ul]=elemento
            self.__ul += 1
            self.__canti += 1
        else: 
            print("La cola se encuentra llena")
    def Suprimir(self):
        x = None
        if self.Vacia():
            print("La cola se encuentra vacía")
        else:
            x = self.__items[self.__pr]
            self.__items[self.__pr] = 0
            self.__pr = (self.__pr+1)%self.__max
            self.__canti -= 1
        return x
    def Recorrer(self):
        s = ""
        if not self.Vacia():
            for i in range(self.__canti):
                s = s + str(self.__items[i]) + ", "
            return s
        else:
            print("La cola se encuentra vacía")
if __name__=='__main__':

    # Realice un programa  que simule el comportamiento de un hospital,
    # donde los pacientes acuden a sacar turnos para los consultorios externos en mesa de entradas  
    # donde se toma la siguiente información: 
    # nombre, documento y especialidad (Ginecología, Clínica médica, Oftalmología, Pediatría)  
    # con un tiempo promedio de atención de 2 minutos. 
    # Dependiendo de la especialidad se le indica el numero de  consultorio en que será atendido.
    # El tiempo promedio de atención del médico es de 20’.

    # Considerando que la frecuencia de llegada de los pacientes al hospital es de 1 por minutos  aproximadamente;
    # que en cada especialidad se atiende un máximo de 10 pacientes y los turnos solamente se dan de 7 a 8 de la mañana.

    #  Se pide    a) calcular el tiempo promedio de espera en la cola de turnos.

    #             b) tiempo promedio de espera de los pacientes en cada especialidad.

    #             c) cantidad de personas que no pudieron obtener turnos.
    # Nota: considere el tiempo de simulación de 4 horas
    colaAtencion=Cola()
    colaAux=Cola()
    colaGine=Cola(10)
    colaClinica=Cola(10)
    colaOfta=Cola(10)
    colaPedia=Cola(10)
    cajeroLibre=True
    cantiturnos=0
    cantiperson=0
    llegada=int(input("Indique frecuencia de llegada de las personas:"))
    atencion=int(input("Indique tiempo en que tarda una persona en ser atendida:"))
    for minutos in range(60):
        if random.randint(0,1) == 1 and minutos % llegada == 0 and cajeroLibre:
            a=random.randint(0,3)
            persona=Persona(a , minutos)
            colaAtencion.Agregar(persona)
            cajeroLibre=False
            print("PERSONA AGREGADA A LA COLA DE ENTRADA")

        if minutos - persona.Tiempo() > atencion and not colaAtencion.Vacia():
            personaAtendida=colaAtencion.Suprimir()
            colaAux.Agregar(personaAtendida)
            cajeroLibre=True
            print("PERSONA SACADA DE LA COLA DE ENTRAD")
        print(minutos)

    minutos=0
    noAtendidos=0
    cantig=0
    cantic=0
    cantio=0
    cantip=0
    gineLibre=True
    clinicaLibre=True
    oftaLibre=True
    pediaLibre=True
    for minutos in range(60,240):
        if random.randint(0,1) == 1:
            persona=colaAux.Suprimir()
            if(persona.Especialidad().lower()=="ginecologia" and gineLibre):
                persona.setTiempo(minutos)
                colaGine.Agregar(persona)
                gineLibre=False
                print("PERSONA AGREGADA A GINECOLOGIA")

            elif(persona.Especialidad().lower()=="clinica medica" and clinicaLibre):
                persona.setTiempo(minutos)
                colaClinica.Agregar(persona)
                clinicaLibre=False
                print("PERSONA AGREGADA A CLINICA MEDICA")

            elif(persona.Especialidad().lower()=="oftalmologia" and oftaLibre):
                persona.setTiempo(minutos)
                colaOfta.Agregar(persona)
                oftaLibre=False
                print("PERSONA AGREGADA A OFTALMOLOGIA")

            elif(persona.Especialidad().lower()=="pediatria" and pediaLibre):
                persona.setTiempo(minutos)
                colaPedia.Agregar(persona)
                pediaLibre=False
                print("PERSONA AGREGADA A PEDIATRIA")

            else:
                noAtendidos+=1
                print(f"No hay mas lugar en la especialidad:{persona.Especialidad()}")
        
        
        
        
        if not colaGine.Vacia():
            personGine=colaGine.Suprimir()
            if minutos - personGine.Tiempo() >= 20:
                personaAtendida=colaGine.Suprimir()
                gineLibre=True
        else:
            print('Cola gine vacia')

        if not colaClinica.Vacia():
            personClinica=colaClinica.Suprimir()
            if minutos - personClinica.Tiempo() >= 20:
                personaAtendida=colaClinica.Suprimir()
                clinicaLibre=True
        else:
            print('Cola clinica vacia')

        if not colaOfta.Vacia():
            personOfta=colaOfta.Suprimir()
            if minutos - personOfta.Tiempo() >= 20 :
                personaAtendida=colaOfta.Suprimir()
                oftaLibre=True
        else:
            print('Cola ofta vacia')

        if not colaPedia.Vacia():
            personPedia=colaPedia.Suprimir()
            if minutos - personPedia.Tiempo() >= 20 :
                personaAtendida=colaPedia.Suprimir()
                pediaLibre=True
        else:
            print('Cola pedia vacia')

        print(minutos)

