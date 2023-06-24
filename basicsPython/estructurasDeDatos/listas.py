# Programa que suma los elementos de una lista utilizando un bucle for
valoresLista = [1, 2, 3, 4, 5,'a','b','c',2.1,2.2,True,False]
suma = 0

for val in valoresLista:
    print(val)


print("imprimiendo posicion especifica: "+valoresLista[5])
print("imprimiendo ultima posicion : ",valoresLista[len(valoresLista)-1])
print(valoresLista)
#eliminar ultimo valor lista
valoresLista.pop()
print("luego de pop",valoresLista)
print("imprimiendo desde pos 0 a 8",valoresLista[0:8])

#agregando valores de 90 a 100 en lista

for n in range(90,101):
    valoresLista.append(n)
print("imprimiendo luego de ageegar valores",valoresLista)

#concatenando strings de una lista
listaJoin=['h','o','l','a']
listaJoin=''.join(listaJoin)
print(listaJoin)