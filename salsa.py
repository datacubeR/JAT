def elegir_salsa(pizza, opcion):
    while opcion not in ['T','A','B','P']:
        print('Salsa no Válida. Ingrese una Salsa válida.')
        opcion = input('''Seleccione el tipo de Salsa:
                T. Salsa de Tomate.
                A. Salsa Alfredo.
                B. Salsa Barbecue.
                P. Salsa Pesto.
                > ''').upper()
    else:
        if opcion == 'T':
            pizza['salsa'] = 'Salsa de Tomate'
        elif opcion == 'A':
            pizza['salsa'] = 'Salsa Alfredo'
        elif opcion == 'B':
            pizza['salsa'] = 'Salsa Barbecue'
        elif opcion == 'P':
            pizza['salsa'] = 'Salsa Pesto'
            
    return pizza

if __name__ == '__main__': # ejecutar el codigo abajo solo si es que estoy ejecutando el script actual...
    pizza = dict(
        masa = 'Tradicional', 
        salsa = 'Barbecue',
        ingredientes = ['Tomate','Aceituna','Pollo']
    )

    opcion = input('''Seleccione el tipo de Salsa:
                T. Salsa de Tomate.
                A. Salsa Alfredo.
                B. Salsa Barbecue.
                P. Salsa Pesto.
                > ''').upper()
    
    print(elegir_salsa(pizza, opcion))