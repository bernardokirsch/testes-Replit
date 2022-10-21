import numpy as np

lista = [10, 8, 6, 7, 4]

media = np.mean(lista)

soma_lista = 0

for i in lista: 
  soma_lista += i

media_lista = soma_lista / len(lista)

print('Média da lista normal: ', media_lista)
print('Média da lista usando função mean do NumPy: ', media)