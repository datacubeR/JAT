

def agregar_ingrediente(pizza, opcion):
    ingredientes = ['Tomate','Champiñones','Aceituna','Cebolla','Pollo','Jamón','Carne','Tocino','Queso']
    nuevo_ingrediente = ingredientes[opcion-1]
    
    if nuevo_ingrediente in pizza['ingredientes']:
        print('Ese Ingrediente ya es parte de tu Pizza.')
    else:
        pizza['ingredientes'].append(nuevo_ingrediente)

    return pizza

if __name__ == '__main__':
    pizza = dict(
        masa = 'Tradicional', 
        salsa = 'Barbecue',
        ingredientes = ['Tomate','Aceituna','Pollo']    
    )

    opcion = int(input('''Seleccione los ingredientes a Agregar:
                1. Tomate
                2. Champiñones
                3. Aceituna
                4. Cebolla
                5. Pollo
                6. Jamón
                7. Carne
                8. Tocino
                9. Queso
                > '''))
    
    while opcion not in [1,2,3,4,5,6,7,8,9]:
        print('Ingrediente no Válido')
        opcion = int(input('''Seleccione los ingredientes a Agregar:
                1. Tomate
                2. Champiñones
                3. Aceituna
                4. Cebolla
                5. Pollo
                6. Jamón
                7. Carne
                8. Tocino
                9. Queso
                > '''))
    else:
        print(agregar_ingrediente(pizza, opcion))

        