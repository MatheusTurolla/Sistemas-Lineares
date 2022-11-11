import numpy as np
import pandas as pd

#Função que lê e mapeia o arquivo em csv com o pandas
def readingCsv():
    data = pd.read_csv('Entrada.csv', names=['x1','x2','r'], header=None)
    return data

#Pega o retorno da função acima, calcula todos os valores e mapeia
def calculate():
    content = readingCsv()

    A = np.array([[content['x1'][0],content['x2'][0]],[content['x1'][1],content['x2'][1]]], dtype=float)
    B = np.array([[content['r'][0]],[content['r'][1]]], dtype=float)

    result = np.linalg.solve(A,B)
    
    print(f'Resultado de x1: {result[0]}')
    print(f'Resultado de x2: {result[1]}')

def main():
    calculate()

if __name__ == "__main__":
    main()

