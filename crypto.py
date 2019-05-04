import math
import numpy as np
W = np.array([[1, 1], [1, -1]],int)
p = (12,4,6,2,10,5,11,9,14,8,13,7,0,3,15,1)
#####Матрица Адамара-Сильвестра#####
def hadamardMatrix(dimension):
    if dimension == 1:
        return W
    else:
        return np.hstack((np.vstack((hadamardMatrix(dimension-1),hadamardMatrix(dimension-1))),np.vstack((hadamardMatrix(dimension-1),-hadamardMatrix(dimension-1)))))
#####Получение массива значений функций#####
def functionValue(function):
    values = [ [] for _ in range(len(bin(max(function))[2:]))]
    for value in function:
        for function_number in range(len(bin(max(function))[2:])):
            values[function_number].append(value >> function_number & 1)
    values.reverse()
    return values
########Многочлен Жегалкина#######
def anf(function):
    buff = []
    iterations = len(function)
    ANF = [ function[0] ]
    for _ in range(iterations-1):
        for i in range(len(function)-1):
            buff.append(function[i]^function[i+1])
        print(buff)
        ANF.append(buff[0])
        function = buff
        buff = []
    return ANF
#####Список Фурье образов для всех разрядных функций#####
def fourierSpectrum(function):
    values = functionValue(function)
    spectrum = [] 
    M = hadamardMatrix(int(math.log2(len(function))))
    for functions in range(len(bin(max(function))[2:])):
        spectrum.append(np.matmul(np.array(values[functions]).T,M).tolist())
    return spectrum
#########################################################
#####Список Уолш образов для всех разрядных функций#####
def walschSpectrum(function):
    values = functionValue(function)
    unit_array = np.array([1 for _ in range(len(function))])
    M = hadamardMatrix(int(math.log2(len(function))))
    spectrum = []
    for functions in range(len(bin(max(function))[2:])):
        spectrum.append(np.matmul((unit_array - 2 * np.array(values[functions])).T,M).tolist())
    return spectrum
####################Задание 5 ###############################
def ordinaryProbability(function):
    values = functionValue(function)
    var = [[0] for _ in range(int(math.log2(len(function))))]
    for k in range(int(math.log2(len(function)))): 
        for i in range(int(math.log2(len(function)))):
            num = 0
            for j in range(len(function)):
                 if values[k][j] != values[k][j^(2**i)]:
                     num=num+1
            var[k][0]=var[k][0]+num
    return var
################# Задание 6################
def doubleProbability(function):
    values = functionValue(function)
    g = {1:[0,1],2:[0,2],3:[1,2],4:[0,3],5:[1,3],6:[2,3]}
    var = [[0] for _ in range(6)]
    for k in g: 
        for i in range(int(math.log2(len(function)))):
            num = 0
            for j in range(len(function)):
                 if values[g[k][0]][j] != values[g[k][0]][j^(2**i)] and values[g[k][1]][j] != values[g[k][1]][j^(2**i)]:
                     num=num+1
            var[k-1][0]=var[k-1][0]+num
    return var,g
#############Задание 7############
def anyProbability(function):
    values = functionValue(function)
    var = [[0] for _ in range(5)]
    for i in range(int(math.log2(len(function)))):
        for j in range(len(function)):
            num = 0
            for k in range(int(math.log2(len(function)))):
                if values[k][j] != values[k][j^(2**i)]:
                    num=num+1
            var[num][0]=var[num][0]+1
    return var
print(np.array(anf(p)))
print(np.array(fourierSpectrum(p)))
print(np.array(walschSpectrum(p)))
print(np.array(ordinaryProbability(p)))
print(np.array(doubleProbability(p)))
print(np.array(anyProbability(p)))
