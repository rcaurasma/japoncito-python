
def japoncito():
    print('--'*30)
    print('\t\tBIENVENIDO A "JAPONCITO"')
    print('--'*30)
    print('\n\n')
    print('--'*30)
    total_Pagar = 0
    while True:
        precio = 0

        proteinas = {
            1:["Salmon","1500"],
            2:["Camaron","1200"],
            3:["Atun","1800"],
            4:["Pollo","1000"],
            5:["Cerdo","1000"],
            6:["Carne","1200"]
        }
        
        print("Proteinas disponibles:")
        for key, proteina in proteinas.items():
            print(f"{key}: {proteina[0]} --> ${proteina[1]}")
        seleccion_Proteina = int(input("Seleccione el numero de su proteina: "))

        if seleccion_Proteina in proteinas:
            precio += int(proteinas[seleccion_Proteina][1])
        
        contornos_Sel = []
        max_Contornos = 0

        print('--'*30)
        print('\t\t\tQUESO CREMA')
        print('--'*30)
        print("""
            1.- Sí --> $800
            2.- No --> $0
        """)

        queso_Crema = input("""
        ¿Desea agregar queso crema al roll? (si/no)
        Nota: agregar queso crema tiene un valor de $800 
        y reduce el maximo de contornos de dos a uno """).lower()


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
            print("Contornos disponibles:")
            for key, contorno in contornos.items():
                print(f"{key}: {contorno[0]} --> ${contorno[1]}")
            
            seleccion_Contornos = int(input("Seleccione el numero de su contorno: "))

            precio_Contorno = int(contornos[seleccion_Contornos][1])
            precio += precio_Contorno
            max_Contornos -= 1
            contornos_Sel.append(contornos[seleccion_Contornos][0])
        

        envolturas = {
            1:["Sesamo","100"],
            2:["Palta","800"],
            3:["Queso Crema","1000"],
            4:["Salmon","1500"],
            5:["Panko","300"],
            6:["Tempura","200"]
        }
        print("Envolturas disponibles:")
        for key, envoltura in envolturas.items():
            print(f"{key}: {envoltura[0]} --> ${envoltura[1]}")
        seleccion_Envolturas = int(input("Seleccione el numero de su envoltura: "))

        if seleccion_Envolturas in envolturas:
            precio += int(envolturas[seleccion_Envolturas][1])
        

        total_Pagar += precio
        print(f"Total a pagar por este roll: ${precio}")
        print("Contornos elegidos:", ", ".join(contornos_Sel))
        

        seguir_pedido = input("¿Desea preparar otro roll? (si/no): ").lower()
        if seguir_pedido == "no":
            break

    print(f"\nTotal a pagar por los rolls de sushi: ${total_Pagar}")

japoncito()