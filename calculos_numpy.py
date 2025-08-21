import numpy as np

#criando uma array Numpy (vetor)
arr = np.array([1,2,3,4,5])

print(f'Array Numpy: \n {arr}')

#Operacoes matematicas em arrays( é a gaveta)
print('\n Array multiplicado por 2:')
print(arr * 2)

#mais um exemplo
print(arr[2]*2)

#operacao entre arrays
arr2 = np.array([10,20,30,40,50])
print(arr+arr2)

#criando uma matrix (2d)
matriz = np.array([[1,2,3],[4,5,6]])
print('\nMatriz 2x3')
print(matriz)

#soma e media da matriz
print('\nSoma de todos os elementos da matriz')
print(np.sum(matriz))

print ('\n Media dos elementos da Matriz')
print(np.mean(matriz)) #mean é media

#transposta da matriz
print('\nMatriz Transposta')
print(matriz.T)

#gerando numeros aleatorios
print('\n Numeros aleatorios entre 0 e 1:')
print(np.random.rand(3,3))

#valor maximo do array
print('\nValor Maximo da array')
print(np.max(arr))

#valor minimo do array
print('\nValor minimo da array')
print(np.min(arr))

#Desvio padrao
print('\nDesvio padrao da array')
print(np.std(arr2))

#Indexacao avancada
print('\nElementos maiores que 3')
print(arr[arr > 3])



#ordenação dos dados
arr3 = np.array([10,4,35,22,13])
print('\nArry ordenada')
print(np.sort(arr3))

#gerando numeros aleatorios entre 1 e 100 (legal para fazerescolhas aleatorias para a mega sena)
print('\nNumerosinteiros entre 1 a 100')
print(np.random.randint(1,100, size=(3,3)))

#reorganizando dados
print('\nReshapeda matriz (2x3 para 3x2)')
print(matriz.reshape(3,2))