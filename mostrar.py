
def mostrar_ingredientes(pizza):
    
    print(f"Su masa es: {pizza['masa']}")
    print(f"Su salsa es: {pizza['salsa']}")
    
    print(f"Sus Ingredientes son: ")
    for i in pizza['ingredientes']:
        print(f'''  - {i}''')


if __name__ == '__main__':
    pizza = dict(
        masa = 'Tradicional', 
        salsa = 'Barbecue',
        ingredientes = ['Tomate','Aceituna','Pollo','Carne']    
    )
    
    mostrar_ingredientes(pizza)