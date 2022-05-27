def estimar_tiempo(pizza):
    n_ingredientes = len(pizza['ingredientes'])
    
    return 20 + 2*n_ingredientes

if __name__ == '__main__':
    pizza = dict(
        masa = 'Tradicional', 
        salsa = 'Barbecue',
        ingredientes = ['Tomate','Aceituna','Pollo','Carne']    
    )
    
    print(estimar_tiempo(pizza))