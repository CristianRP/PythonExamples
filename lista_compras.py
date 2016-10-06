lista_compras = ['manzana', 'piña', 'lechuga', 'avena', 'pechuga']

def clasificar_compra(lista_compras):
    frutas = ['manzana', 'naranja', 'banano', 'fresa', 'pera', 'piña', 'uva']
    verduras = ['tomate', 'papa', 'zanahoria', 'güicoy', 'lechuga']
    carnes = ['pechuga', 'puyaso', 'pierna de cerdo', 'pierna de pollo']
    cereales = ['avena', 'hojuelas de maiz', 'cebada', 'maiz', 'arroz', 'trigo']
    fruits = []
    vegetables = []
    meats = []
    cereals = []

    for compra in lista_compras:
        for fruta in frutas:
            if (compra == fruta):
                fruits.append(fruta)
        for verdura in verduras:
            if (compra == verdura):
                vegetables.append(verdura)
        for carne in carnes:
            if (compra == carne):
                meats.append(carne)
        for cereal in cereales:
            if (compra == cereal):
                cereals.append(cereal)

    print('Frutas:', fruits)
    print('Verduras:', vegetables)
    print('Carnes:', meats)
    print('Cereales:', cereals)

clasificar_compra(lista_compras)
