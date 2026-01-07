# precio_Prote_Dic = {
#     '1':{'Salmon',1500},
#     '2':{'Camaron',1200},
#     '3':{'Atun',1800},
#     '4':{'Pollo',1000},
#     '5':{'Cerdo',1000},
#     '6':{'Carne',1200},
# }

# seleccion_prote = ((input("Escoga su proteina: ")))
# if seleccion_prote in precio_Prote_Dic.keys():
#             proteina,precio = precio_Prote_Dic[seleccion_prote]
#            print(f'La proteina escogida es de: {proteina}, a un precio de {precio}')
#else:
#        print("Su seleccion no esta en el menu")


# rellenosList = [['Palta',500],['Pepino',300],['Zanahoria',200],['Palmito',200],['Pina',300],['Cebollin',200]]    
# sel_Relleno = int((input("Escoga su proteina: ")))

# for rellenos1 in rellenosList:
#         print('Usted eligio:',rellenosList[sel_Relleno-1][0])
#         print('A un precio de',rellenosList[sel_Relleno-1][1])
#         break


rellenosTuple = (('Palta',500),('Pepino',300),('Zanahoria',200),('Palmito',200),('Pina',300),('Cebollin',200))   
sel_Relleno = int((input("Escoga su proteina: ")))

for rellenos1 in rellenosTuple:
        print('Usted eligio:',rellenosTuple[sel_Relleno-1][0])
        print('A un precio de',rellenosTuple[sel_Relleno-1][1])
        break




