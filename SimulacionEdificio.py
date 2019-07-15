# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 20:35:10 2019

@author: Antonio
Listas doblemente enlazadas
para la simulacion de los pisos del edificio
"""
# Clase del piso en general, con los parametros de Conductividad Termica y Resistencia Termica
class Piso(object):
    def __init__(self,NumPiso,Ctermica,Rtermica):
        #Atributos que tendra el nodo
        self.__NumPiso=NumPiso
        self.__Ctermica=Ctermica
        self.__Rtermica=Rtermica
        
        #Punteros del nodo
        self.__pSig = None
        self.__pAnt = None
        
    def getElemento(self):
        return self.__NumPiso, self.__Ctermica,self.__Rtermica
    
# Clase Lista Doblemente Enlazada de los pisos del edificio con todos sus metodos
class ListaDoblePisos(object):
    def __init__(self):
        self.__primero = None
        self.__ultimo = None
    
    def getVacio(self):
        if self.__primero == None:
            return True
    
    def setNodoAlInicio(self,NumPiso,Ctermica,Rtermica):
        nuevo = Piso(NumPiso,Ctermica,Rtermica)
        if self.getVacio()==True:
            self.__primero = self.__ultimo = nuevo
        else:
            nuevo.pSig=self.__primero
            self.__primero.pAnt=nuevo
            self.__primero=nuevo
    
    def setNodoAlFinal(self,NumPiso,Ctermica,Rtermica):
        nuevo = Piso(NumPiso,Ctermica,Rtermica)
        if self.getVacio()==True:
            self.__primero = self.__ultimo = nuevo
        else:
            self.__ultimo.pSig=nuevo
            nuevo.pAnt=self.__ultimo
            self.__ultimo=nuevo
    
    def eliminarPrimero(self):
        if self.getVacio()==True:
            print("La lista esta vacia")
        elif self.__primero==self.__ultimo:
            self.__primero=None
            self.__ultimo=None
            print("Elemento eliminado, la lista esta vacia")
            
        else:
            temp=self.__primero
            self.__primero=self.__primero.pSig
            self.__primero.pAnt=None
            temp=None
            print("Elemento eliminado")
        
    def eliminarUltimo(self):
        if self.getVacio()==True:
            print("La lista esta vacia")
            
        elif self.__primero==self.__ultimo:
            self.__primero=None
            self.__ultimo=None
            print("Elemento eliminado, la lista esta vacia")
            
        else:
            temp=self.__ultimo
            self.__ultimo=self.__ultimo.pAnt
            self.__ultimo.pSig=None
            temp = None
            print("Elemento eliminado")
           
        
    def printListaPrimeroUltimo(self):
        if self.getVacio()==True:
            print("la lista esta vacia")
        else:
            validar=True
            temp= self.__primero
            while(validar):
                print(temp.getElemento())
                if temp == self.__ultimo:
                    validar=False
                else:
                    temp= temp.pSig
        
    def printListaUltimoPrimero(self):
        if self.getVacio()==True:
            print("la lista esta vacia")
        else:
            validar=True
            temp= self.__ultimo
            while(validar):
                print(temp.getElemento())
                if temp == self.__primero:
                    validar=False
                else:
                    temp= temp.pAnt
                    
# Clase de la estructura interna de un piso
class PisoInterno(object):
    def __init__(self,MatParedes,CantCuartos,UsoPiso,TempMin,TempMax):
        #Atributos que tendra el nodo
        self.__MatParedes=MatParedes
        self.__CantCuartos=CantCuartos
        self.__UsoPiso=UsoPiso
        self.__TempMin=TempMin
        self.__TempMax=TempMax
        
        #Punteros del nodo
        self.__pSig = None
        self.__pAnt = None
        
    def getElementos(self):
        return self.__MatParedes,self.__CantCuartos,self.__UsoPiso,self.__TempMin,self.__TempMax

# Clase Lista Doblemente Enlazada de los cuartos del edificio con todos sus metodos
class ListaDobleCuartos(object):
    def __init__(self):
        self.__primero = None
        self.__ultimo = None
    
    def getVacio(self):
        if self.__primero == None:
            return True
    
    def setNodoAlInicio(self,MatParedes,CantCuartos,UsoPiso,TempMin,TempMax):
        nuevo = PisoInterno(MatParedes,CantCuartos,UsoPiso,TempMin,TempMax)
        if self.getVacio()==True:
            self.__primero = self.__ultimo = nuevo
        else:
            nuevo.pSig=self.__primero
            self.__primero.pAnt=nuevo
            self.__primero=nuevo
    
    def setNodoAlFinal(self,MatParedes,CantCuartos,UsoPiso,TempMin,TempMax):
        nuevo = PisoInterno(MatParedes,CantCuartos,UsoPiso,TempMin,TempMax)
        if self.getVacio()==True:
            self.__primero = self.__ultimo = nuevo
        else:
            self.__ultimo.pSig=nuevo
            nuevo.pAnt=self.__ultimo
            self.__ultimo=nuevo
    
    def eliminarPrimero(self):
        if self.getVacio()==True:
            print("La lista esta vacia")
        elif self.__primero==self.__ultimo:
            self.__primero=None
            self.__ultimo=None
            print("Elemento eliminado, la lista esta vacia")
            
        else:
            temp=self.__primero
            self.__primero=self.__primero.pSig
            self.__primero.pAnt=None
            temp=None
            print("Elemento eliminado")
        
    def eliminarUltimo(self):
        if self.getVacio()==True:
            print("La lista esta vacia")
            
        elif self.__primero==self.__ultimo:
            self.__primero=None
            self.__ultimo=None
            print("Elemento eliminado, la lista esta vacia")
            
        else:
            temp=self.__ultimo
            self.__ultimo=self.__ultimo.pAnt
            self.__ultimo.pSig=None
            temp = None
            print("Elemento eliminado")
           
        
    def printListaPrimeroUltimo(self):
        if self.getVacio()==True:
            print("la lista esta vacia")
        else:
            validar=True
            temp= self.__primero
            while(validar):
                print(temp.getElementos())
                if temp == self.__ultimo:
                    validar=False
                else:
                    temp= temp.pSig
        
    def printListaUltimoPrimero(self):
        if self.getVacio()==True:
            print("la lista esta vacia")
        else:
            validar=True
            temp= self.__ultimo
            while(validar):
                print(temp.getElementos())
                if temp == self.__primero:
                    validar=False
                else:
                    temp= temp.pAnt




#Pruebas con los objetos, falta calcular con los datos reales en un nuevo metodo.                   
prueba= ListaDoblePisos()
prueba2=ListaDobleCuartos()

prueba2.setNodoAlFinal("Hierro",2,"Contabilidad",18,23)

prueba.setNodoAlFinal(1,4,8)
prueba.setNodoAlFinal(2,5,7)
prueba.setNodoAlInicio(3,2,6)
prueba2.printListaPrimeroUltimo()



prueba.printListaUltimoPrimero()
prueba.eliminarPrimero()
prueba.eliminarUltimo()
prueba.printListaPrimeroUltimo()
prueba.printListaUltimoPrimero()            
            
            
            
            
            
            
            
            
            
            
            
            
            