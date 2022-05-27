from masa import elegir_masa
from salsa import elegir_salsa
from agregar import agregar_ingrediente
from remover import remover_ingrediente
from tiempo import estimar_tiempo
from mostrar import mostrar_ingredientes
from utils import MENU_ADD, MENU_INICIAL, MENU_MASA, MENU_REM, MENU_SALSA

import os 
import time 

# estructura de datos: 
pizza = dict(
    masa = 'Tradicional', 
    salsa = 'Tomate',
    ingredientes = ['Queso']
)

os.system('clear')
print('Bienvenido a Pizza JAT')
while True:
    opcion = input(MENU_INICIAL)
    
    if opcion == "1":
        os.system('clear')
        eleccion = input(MENU_MASA).upper()
        pizza = elegir_masa(pizza, eleccion)
        
    elif opcion == "2":
        os.system('clear')
        eleccion = input(MENU_SALSA).upper()
        pizza = elegir_salsa(pizza, eleccion)
    
    elif opcion == "3":
        os.system('clear')
        eleccion = int(input(MENU_ADD))
    
        while eleccion not in [1,2,3,4,5,6,7,8,9]:
            os.system('clear')
            print('Ingrediente no Válido')
            eleccion = int(input(MENU_ADD))
        else:
            pizza = agregar_ingrediente(pizza, eleccion)

    elif opcion == "4":
        os.system('clear')
        eleccion = int(input(MENU_REM))
    
        while eleccion not in [1,2,3,4,5,6,7,8,9]:
            os.system('clear')
            print('Ingrediente no Válido')
            eleccion = int(input(MENU_REM))
        else:
            pizza = remover_ingrediente(pizza, eleccion)
    
    elif opcion == "5":
        os.system('clear')
        tiempo = estimar_tiempo(pizza)
        print(f'El tiempo estimado para su Pizza es {tiempo} minutos')
        
        ordenar = input('Desea ordenar ahora? ').upper()
        if ordenar == 'S':
            print('Gracias por Ordenar en Pizza JAT')
            print('Disfrute su Pizza')
            time.sleep(2)
            
            os.system('clear')
            exit()
        
    elif opcion == "9":
        os.system('clear')
        mostrar_ingredientes(pizza)
        time.sleep(5)
        
    os.system('clear')
    
    
    



