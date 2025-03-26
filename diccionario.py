# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 08:09:42 2025

@author: Miguel Gonzalez Duran

---DICCIONARIO---

"""
#Aqui definimos una funcion que vivualiza un diccionario 
def visualizar_diccionario(dato_diccionario):
    print('El contenido del diccionario es:')
     
    for llave in un_diccionario.keys():
        print(f'Llave : {llave} \n  Valor: {un_diccionario[llave]}')        
        print(f"\n El diccionario tiene {len(un_diccionario)} elementos")
    
    
#Aqui definimos una funcion que vivualiza las llaves de un diccionario    
def visualizar_llaves(dato_llaves):
    print('\n las llaves del diccionario son:')
    for una_llave in dato_llaves:
     print(una_llave)






print('Programa para demostrar el funcionamiento de un diccionario ')
un_diccionario = {
    "recorcholis":"expresion atipica de la region central de colombia",
    "Futbol":"Deporte en el que todo un pai puede llorar al mismo tiempo",
    "Zapato":"prenda de vestir que se usa para caminar",
    "Collar":"Accesorio que se usa en el cuello",
    "Palindromo":"Palabra que se lee igual al derecho y al reves"
       }
print(f"el diccionario es de tipo {type(un_diccionario)}")
print(f"el diccionario tiene {len(un_diccionario)} elementos")
print(f"El contenido del diccionario es: ")


    
visualizar_llaves(un_diccionario.keys())
visualizar_diccionario(un_diccionario)

llave_buscada = input('\n Ingrese la llave que desea encontrar: ')
if llave_buscada not in list(un_diccionario.keys()):
    print(f'la llave no existe en el diccionario')
else: 
    print(f'la definicion para {llave_buscada} es {un_diccionario[llave_buscada]}')
    
#aqui asignamos un nuevo elemnto al diccionario
nueva_llave = input('\n ingrese la nueva llave: ')
nueva_definicion = input('Ingrese la nueva definicion: ')
un_diccionario[nueva_llave] = nueva_definicion


visualizar_llaves(un_diccionario.keys())
visualizar_diccionario(un_diccionario)