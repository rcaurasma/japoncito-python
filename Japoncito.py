from tabulate import tabulate

def pago_efectivo(monto):
    """Procesa pagos en efectivo"""
    print(f"\nMonto a pagar: ${monto}")
    pago = int(input("Con cuanto cancela?: "))
    print(f"Usted cancelo con: ${pago}")
    cambio = pago - monto
    
    while cambio < 0:
        print(f"El pago es insuficiente. Aun debe: ${abs(cambio)}")
        pago = int(input("Con cuanto cancela?: "))
        cambio = pago - monto
        print(f"Usted cancela con: ${pago}")
    
    if cambio == 0:
        print("El pago es exacto. No hay cambio.")
    else:
        print(f"Su cambio es: ${cambio}")
    print("Su compra ha sido realizada con exito.")


def pago_debito(monto):
    """Procesa pagos con debito"""
    while True:
        nombre = input("\nPor favor, ingrese su nombre de usuario: ").strip()
        clave = input("Por favor, ingrese su contraseña: ").strip()
        if nombre == 'alex' and clave == '1234':
            print(f"Credenciales correctas. Bienvenido, {nombre}")
            break
        else:
            print("Credenciales incorrectas. Intente nuevamente.")
    
    saldo = 5000
    print(f"\nSu saldo actual: ${saldo}")
    print(f"Monto a pagar: ${monto}")
    
    if monto <= saldo:
        saldo -= monto
        print(f"Pago procesado exitosamente.")
        print(f"Saldo restante: ${saldo}")
    else:
        faltante = monto - saldo
        print(f"Saldo insuficiente. Le faltan: ${faltante}")
    print("Su compra ha sido realizada con exito.")


def pago_cuotas(monto):
    """Procesa pagos en cuotas"""
    while True:
        nombre = input("\nPor favor, ingrese su nombre de usuario: ").strip()
        clave = input("Por favor, ingrese su contraseña: ").strip()
        if nombre == 'alex' and clave == '1234':
            print(f"Credenciales correctas. Bienvenido, {nombre}")
            break
        else:
            print("Credenciales incorrectos. Intente nuevamente.")
    
    num_cuotas = int(input("\nEn cuantas cuotas desea pagar?: "))
    while num_cuotas <= 0:
        print("La cantidad de cuotas debe ser mayor que cero.")
        num_cuotas = int(input("En cuantas cuotas desea pagar?: "))
    
    pago_mensual = monto / num_cuotas
    print(f"\nMonto total: ${monto}")
    print(f"{num_cuotas} cuotas de ${pago_mensual:.0f} cada una.")
    print("Su compra ha sido realizada con exito.")


def japoncito():
    # Introduccion y presentacion
    print('\n' + '='*60)
    print('BIENVENIDO A RESTAURANT JAPONCITO'.center(60))
    print('='*60)
    print('En esta app podras armar tu propio roll de sushi a tu gusto.')
    print('A continuacion, verás el menu con las opciones disponibles.')
    input('\nPresiona ENTER para continuar...')

    print('\n')
    total_Pagar = 0
    num_roll = 1
    
    while True:
        precio = 0

        # Menu proteinas
        print('\n' + '='*60)
        print(f'ROLL #{num_roll} - PROTEINAS'.center(60))
        print('='*60)
        proteinas = {
            1:["Salmon","1500"],
            2:["Camaron","1200"],
            3:["Atun","1800"],
            4:["Pollo","1000"],
            5:["Cerdo","1000"],
            6:["Carne","1200"]
        }
        
        tabla_proteinas = [[k, v[0], f"${v[1]}"] for k, v in proteinas.items()]
        print(tabulate(tabla_proteinas, headers=["Opcion", "Proteina", "Precio"], tablefmt="grid"))
        print()
        seleccion_Proteina = int(input("Seleccione el numero de su proteina: "))

        if seleccion_Proteina in proteinas:
            precio += int(proteinas[seleccion_Proteina][1])
        
        contornos_Sel = []
        max_Contornos = 0

        # Menu queso crema
        print('\n' + '='*60)
        print('QUESO CREMA'.center(60))
        print('='*60)
        tabla_queso = [["1", "Si", "$800"], ["2", "No", "$0"]]
        print(tabulate(tabla_queso, headers=["Opcion", "Opcion", "Precio"], tablefmt="grid"))
        print()

        queso_Crema = input("Desea agregar queso crema al roll? (si/no)\nNota: agregar queso crema cuesta $800 \ny reduce el maximo de contornos de dos a uno: ").lower()

        if queso_Crema == 'si':
            queso_Crema = 'con queso'
            precio += 800
            max_Contornos += 1
        elif queso_Crema == 'no':
            queso_Crema = 'sin queso'
            max_Contornos += 2
        else:
            print("Opcion invalida.")
        
        # Menu contornos
        while max_Contornos > 0:
            print('\n' + '='*60)
            print(f'CONTORNOS ({max_Contornos} disponibles)'.center(60))
            print('='*60)
            contornos = {
                1:["Palta","500"],
                2:["Pepino","300"],
                3:["Zanahoria","200"],
                4:["Palmito","200"],
                5:["Piña","300"],
                6:["Cebollin","200"]
            }
            
            tabla_contornos = [[k, v[0], f"${v[1]}"] for k, v in contornos.items()]
            print(tabulate(tabla_contornos, headers=["Opcion", "Contorno", "Precio"], tablefmt="grid"))
            print()
            seleccion_Contornos = int(input("Seleccione el numero de su contorno: "))

            precio_Contorno = int(contornos[seleccion_Contornos][1])
            precio += precio_Contorno
            max_Contornos -= 1
            contornos_Sel.append(contornos[seleccion_Contornos][0])
        
        # Menu envolturas
        print('\n' + '='*60)
        print('ENVOLTURA'.center(60))
        print('='*60)
        envolturas = {
            1:["Sesamo","100"],
            2:["Palta","800"],
            3:["Queso Crema","1000"],
            4:["Salmon","1500"],
            5:["Panko","300"],
            6:["Tempura","200"]
        }
        
        tabla_envolturas = [[k, v[0], f"${v[1]}"] for k, v in envolturas.items()]
        print(tabulate(tabla_envolturas, headers=["Opcion", "Envoltura", "Precio"], tablefmt="grid"))
        print()
        seleccion_Envolturas = int(input("Seleccione el numero de su envoltura: "))

        if seleccion_Envolturas in envolturas:
            precio += int(envolturas[seleccion_Envolturas][1])
        
        total_Pagar += precio
        print("\n" + "-"*60)
        print(f"Total a pagar por este roll: ${precio}")
        print(f"Contornos elegidos: {', '.join(contornos_Sel)}")
        print("-"*60)
        print()
        
        # Opcion para continuar pidiendo
        seguir_pedido = input("Desea preparar otro roll? (si/no): ").lower()
        if seguir_pedido == "no":
            break
        num_roll += 1

    # Metodo de pago
    print('\n' + '='*60)
    print('METODO DE PAGO'.center(60))
    print('='*60)
    tabla_pagos = [
        ["1", "Efectivo"],
        ["2", "Debito (usuario: alex | clave: 1234)"],
        ["3", "Cuotas (usuario: alex | clave: 1234)"]
    ]
    print(tabulate(tabla_pagos, headers=["Opcion", "Metodo"], tablefmt="grid"))
    print()
    
    metodo_pago = input("Seleccione su metodo de pago (1/2/3): ").strip()
    
    if metodo_pago == '1':
        print("\nProcesando pago en EFECTIVO...")
        pago_efectivo(total_Pagar)
    elif metodo_pago == '2':
        print("\nProcesando pago en DEBITO...")
        pago_debito(total_Pagar)
    elif metodo_pago == '3':
        print("\nProcesando pago en CUOTAS...")
        pago_cuotas(total_Pagar)
    else:
        print("Opcion invalida. Pago no procesado.")

    # Resumen y saludo final
    print('\n' + '='*60)
    print('RESUMEN PEDIDO'.center(60))
    print('='*60)
    print(f"Total a pagar por los {num_roll-1} roll(s) de sushi: ${total_Pagar}")
    print()
    print('MUCHAS GRACIAS POR PREFERIR EL RESTAURANT JAPONCITO'.center(60))
    print('FELIZ DIA!'.center(60))
    print('='*60 + '\n')


japoncito()
print('--'*30)


japoncito()

