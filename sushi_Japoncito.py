#Introducción
print('--'*30)
print('\t\tBIENVENIDO A "JAPONCITO"')
print('--'*30)
print('\n\n')
print('--'*30)

#Menú proteinas
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
#input("Porfavor ingrese el número de la proteína que desea: ")

Proteina_Diccionario = {
        1:('Salmon',1500),
        2:('Camaron',1200),
        3:('Atun',1800),
        4:('Pollo',1000),
        5:('Cerdo',1000),
        6:('Carne',1200),
    }
Pro1 = []
pre1 = 0
sel_proteina = int((input("Escoga su proteina: ")))
if sel_proteina in Proteina_Diccionario.keys():
    proteina,precio = Proteina_Diccionario[sel_proteina]
    proteina = Pro1
    precio = pre1


#Menú queso crema
print('--'*30)
print('\t\t\tQUESO CREMA')
print('--'*30)
print("""
    1.- Sí --> $800
    2.- No --> $0
    """)
#input("Porfavor ingrese el número de la opción que desea: ")

contornos_Sel = []  
max_Contornos = 0

queso_Crema = input("""¿Desea agregar queso crema al roll? (si/no)
        Agregar queso crema tiene un valor de $800 
        y reduce el maximo de contornos de dos a uno: """).lower()

if queso_Crema == 'si':
            queso_Crema = 'con queso'
            precio += 800
            max_Contornos += 1
elif queso_Crema == 'no':
            queso_Crema = 'sin queso'
            max_Contornos += 2
else:
            print("Opcion invalida.")

while max_Contornos > 0:
        contornos = {
                1:["Palta","500"],
                2:["Pepino","300"],
                3:["Zanahoria","200"],
                4:["Palmito","200"],
                5:["Piña","300"],
                6:["Cebollin","200"]
            }

        print(f"Total a pagar por este roll: ${precio}")
        print("Contornos elegidos:", ", ".join(contornos_Sel))
        break


#Menú Rellenos
print('--'*30)
print('\t\t\tRELLENOS')
print('--'*30)
print("""
    1.- Palta     --> $500
    2.- Pepino    --> $300
    3.- Zanahoria --> $200
    4.- Palmito   --> $200
    6.- Piña      --> $300
    7.- Cebollín  --> $200
    """)
#input("Porfavor ingrese el número del relleno que desea: ")

#Menú ENVOLTURA
print('--'*30)
print('\t\t\tENVOLTURA')
print('--'*30)
print("""
    1.- Sésamo      --> $500
    2.- Palta       --> $300
    3.- Queso crema --> $200
    4.- Salmón      --> $200
    6.- Panko       --> $300
    7.- Tempura     --> $200
    """)
#input("Porfavor ingrese el número de la envoltura que desea: ")


#Menú Boleta
print('\n\n\n')
print('--'*30)
print('\t\t\tPREPARANDO')
print('--'*30)
#Acordarse de poner los numeros random en el n° de roll y de poner bien los format
#print(f'Se está preparando el roll n°2: Roll de sushi envuelto en {ENVOLTURA}, relleno de {RELLENO}, {CON_QUESOCREMA} y relleno de {RELLENO2})
print("""
    Desea preparar otro roll?
    1.- Si
    2.- No
    """)
#input("Porfavor ingrese el número de la envoltura que desea: ")



#BoletaResumen
print('--'*30)
print('\t\t\tRESÚMEN PEDIDO')
print('--'*30)
#print(n°2: Roll de sushi envuelto en {ENVOLTURA}, relleno de {RELLENO}, {CON_QUESOCREMA} y relleno de {RELLENO2}))
#print(n°2: Roll de sushi envuelto en {ENVOLTURA}, relleno de {RELLENO}, {CON_QUESOCREMA} y relleno de {RELLENO2}))
print('Roll nro 1 -->','valorRoll')
print('Roll nro 2 -->','valorRoll')
print('               -------------')
print('Total      -->','  TOTAL')

#Método de Pago
print('--'*30)
print('\t\t\tMÉTODO DE PAGO')
print('--'*30)
print("""
    1.- Efectivo
    2.- Tarjeta
    """)
#input("Porfavor ingrese el número método de pago que desea: ")



#Saludo Final
print('\n\n\n')
print('MUCHAS GRACIAS POR PREFERIR EL RESTAURANT "JAPONCITO", FELIZ DÍA')

