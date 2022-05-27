
def elegir_masa(pizza, opcion):
    while opcion not in ['T','D','B']:
        print('Ingrediente no Válido. Ingrese un ingrediente válido.')
        opcion = input('''Seleccione el tipo de Masa:
                T. Tradicional
                D. Delgada
                B. Bordes de Queso
                > ''').upper()
    else:    
        if opcion == 'T':
            pizza['masa'] = 'Tradicional'
        elif opcion == 'D':
            pizza['masa'] = 'Delgada'
        elif opcion == 'B':
            pizza['masa'] = 'Bordes de Queso'
            
    return pizza

if __name__ == '__main__': # ejecutar el codigo abajo solo si es que estoy ejecutando el script actual...
    pizza = dict(
        masa = 'Tradicional', 
        salsa = 'Barbecue',
        ingredientes = ['Tomate','Aceituna','Pollo']
    )

    opcion = input('''Seleccione el tipo de Masa:
                T. Tradicional
                D. Delgada
                B. Bordes de Queso
                > ''').upper()
    
    print(elegir_masa(pizza, opcion))








