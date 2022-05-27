from utils import MENU_REM

def remover_ingrediente(pizza, opcion):
    ingredientes = ['Tomate','Champiñones','Aceituna','Cebolla','Pollo','Jamón','Carne','Tocino','Queso']
    ingrediente_remover = ingredientes[opcion-1]
    
    if ingrediente_remover in pizza['ingredientes']:
        pizza['ingredientes'].remove(ingrediente_remover)
    elif len(pizza['ingredientes']) == 0:
        print('Actualmente tu Pizza no tiene Ingredientes.')
    else:
        print('Ese Ingrediente no es parte de tu Pizza.')

    return pizza

if __name__ == '__main__':
    pizza = dict(
        masa = 'Tradicional', 
        salsa = 'Barbecue',
        ingredientes = []    
    )

    opcion = int(input(MENU_REM))
    
    while opcion not in [1,2,3,4,5,6,7,8,9]:
        print('Ingrediente no Válido')
        opcion = int(input(MENU_REM))
    else:
        print(remover_ingrediente(pizza, opcion))
