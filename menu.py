def menu_proteinas():
    print('\t\t\tPROTEÍNAS')
    print('--'*30)
    print("""
        1.- Salmon  --> $1500
        2.- Camarón --> $1200
        3.- Atún    --> $1800
        4.- Pollo   --> $1000
        6.- Cerdo   --> $1000
        7.- Carne   --> $1200
        """)
    Proteina_Diccionario = {
        1:('Salmon',1500),
        2:('Camaron',1200),
        3:('Atun',1800),
        4:('Pollo',1000),
        5:('Cerdo',1000),
        6:('Carne',1200),
    }

    sel_proteina = int((input("Escoga su proteina: ")))
    if sel_proteina in Proteina_Diccionario.keys():
            proteina,precio = Proteina_Diccionario[sel_proteina]
    proteina = Pro1
    precio = pre1

# def menu_rellenos():
#     print('--'*30)
#     print('\t\t\tRELLENOS')
#     print('--'*30)
#     print("""
#         1.- Palta     --> $500
#         2.- Pepino    --> $300
#         3.- Zanahoria --> $200
#         4.- Palmito   --> $200
#         5.- Piña      --> $300
#         6.- Cebollín  --> $200
#         """)
    
#     rellenosList = [['Palta',500],['Pepino',300],['Zanahoria',200],['Palmito',200],['Pina',300],['Cebollin',200]]    
#     sel_Relleno = int((input("Escoga su proteina: ")))
#     for rell in rellenosList:
#             print('Usted eligio:',rellenosList[sel_Relleno-1][0])
#             print('A un precio de $',rellenosList[sel_Relleno-1][1])
#             break

# menu_rellenos()


def menu_rellenos():
    print('--'*30)
    print('\t\t\tRELLENOS')
    print('--'*30)
    print("""
        1.- Palta     --> $500
        2.- Pepino    --> $300
        3.- Zanahoria --> $200
        4.- Palmito   --> $200
        5.- Piña      --> $300
        6.- Cebollín  --> $200
        """)
    while True:
        try:    
            rellenosList = [['Palta',500],['Pepino',300],['Zanahoria',200],['Palmito',200],['Pina',300],['Cebollin',200]]    
            sel_Relleno = int((input("Elija su proteina: ")))
            for r in rellenosList:
                if sel_Relleno == rellenosList.index(r) +1 :
                    print('Usted eligio:',r[0])
                    print('A un precio de $',r[1])
                    break
            else:
                print("Entrada no válida. Por favor, ingrese un numero de la lista.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

menu_rellenos()