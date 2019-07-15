import pylab
from functools import reduce
import numpy as np

def crearLista(tamaño, valores):
    return [valores for i in range(tamaño)]

def crearMatriz(tamañoFila, tamañoColumna, valores):
    return [[valores for j in range(tamañoFila)] for i in range(tamañoColumna)]

def funcionMultiplicarListas(factor1, factor2):
        return [factor1[i]*factor2[i] for i in range(len(factor1))]

def funcionSumarListas(sumando1, sumando2):
    return [sumando1[i] + sumando2[i] for i in range(len(sumando1))]

def funcionLineal(constantes, variables, sistemaActual):
    i = sistemaActual
    resultado = 0
    for j in (range(3)):
        resultado = resultado + constantes[i][j]*variables[i+j]
    return resultado

def rungeKutta(f, sumVar, multVar, var, cons, lim, p):
    j = 0
    tamVar = len(var)
    h = crearLista(tamVar, p)
    h2 = crearLista(tamVar, p/2)
    k1 = crearLista(tamVar, 0)
    k2 = crearLista(tamVar, 0)
    k3 = crearLista(tamVar, 0)
    k4 = crearLista(tamVar, 0)
    posiciones = crearMatriz(lim,tamVar, 0)
    
    while(j<limite):
        for i in range(tamVar-2):
            k1[i] = h[0] * f(cons, var, i) #k1[x0] = h * (c1xs, c2x0, c3x1)
        for i in range(tamVar-2):
            k2[i] = h[0] * f(cons, sumVar(var, multVar(h2, k1)), i)
        for i in range(tamVar-2):
            k3[i] = h[0] * f(cons, sumVar(var, multVar(h2, k2)), i)
        for i in range(tamVar-2 ):
            k4[i] = h[0] * f(cons, sumVar(var, multVar(h, k3)), i)
        for i in range(tamVar):
            if i<(tamVar-1): #La ultima variable var(tamVar-1) corresponde a 0, no existe, la primera es una constante Ts, por eso no cambian
                var[i+1] = var[i+1] + (1/6) * (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) #la variable x[i+1] es la variable que corresponde a la derivada i
        for i in range(tamVar):
                posiciones[i][j]=var[i]
        j+=1
    return posiciones

def graficar(variableDependiente, variableIndependiente):
    t = variableDependiente
    x = variableIndependiente
    leyenda=["variable Sub"]
    for i in range(len(variables)):
        pylab.plot(t ,x[i] ,'-')
        #print("Variable "+  str(i) + ": " + str(x[i]))
        if i!=0:
            leyenda.append("Variable " + str(i-1))
    for i in range(len(x[1])):
        print("t: "+str(t[i])[:4]+", x: "+str(x[1][i]))
    pylab.legend(leyenda)
    pylab.grid(True)
    pylab.show()

def construirConstantes(cap, res): #Existen n pisos, con n capacitancias, y n+1 resistencias 
    constantes = crearMatriz(3, len(cap))
    if len(cap)>2:
        for i in range(len(cap)):# i representa los pisos (sistema de ecuaciones), la primera resistencia representa el piso inferior, la segunda resistencia representa la del primer piso o actual (i+1)
            constante[i][0] = (1/(cap[i]*res[i-1]))
            constante[i][1] = ((-1)/(cap[i]*res[i])) + ((-1)/(cap[i]*res[i-1]))
            constante[i][2] = ((1/cap[i]*res[i]))
    #construir un caso para 1 y 2 pisos

inicio=0
final=6
paso=0.01
t = np.arange(inicio, final, paso)
limite=int((final-inicio)/paso)
#variables = [1,2,3,5,0,0]
#constantes = [[1,-1,1],[1,1,-1],[1,1,1],[1,1,0]]

variables=[0,-1,-1,0]
constantes=[[0,-1,1],[2,-5,0]]

x = (rungeKutta(funcionLineal, funcionSumarListas, funcionMultiplicarListas, variables, constantes, limite, paso))
t=t+paso
graficar(t,x)
#x[1] = funcionSumarListas(x[1],crearLista(len(x[1]),1))

