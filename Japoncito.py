from tabulate import tabulate
from colorama import Fore, Style, init
from getpass import getpass
import os

init(autoreset=True)

VERDE = Fore.LIGHTGREEN_EX
BLANCO = Fore.WHITE
RESET = Style.RESET_ALL
BRIGHT = Style.BRIGHT

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def obtener_opcion(mensaje, min_opcion, max_opcion):
    while True:
        try:
            entrada = input(mensaje).strip()
            if not entrada:
                print(f"{BLANCO}Error: Ingrese un número del {min_opcion} al {max_opcion}.{RESET}")
                continue
            opcion = int(entrada)
            if min_opcion <= opcion <= max_opcion:
                return opcion
            print(f"{BLANCO}Error: Ingrese un número del {min_opcion} al {max_opcion}.{RESET}")
        except ValueError:
            print(f"{BLANCO}Error: Ingrese un número del {min_opcion} al {max_opcion}.{RESET}")

def mostrar_menu(titulo, opciones):
    print(f'\n{BRIGHT}{VERDE}{"▬"*60}{RESET}')
    print(f'{BRIGHT}{VERDE}{titulo.center(60)}{RESET}')
    print(f'{BRIGHT}{VERDE}{"▬"*60}{RESET}')
    tabla = [[k, v[0], f"${v[1]}"] for k, v in opciones.items()]
    print(tabulate(tabla, headers=["Opcion", "Nombre", "Precio"], tablefmt="grid"))

def procesar_pago(monto, metodo):
    if metodo == 1:
        limpiar_pantalla()
        print(f"\n{BRIGHT}{VERDE}{'▬'*60}{RESET}")
        print(f"{BRIGHT}{VERDE}PROCESANDO PAGO EN EFECTIVO{RESET}".center(60))
        print(f"{BRIGHT}{VERDE}{'▬'*60}{RESET}\n")
        print(f"Monto a pagar: {BLANCO}${monto}{RESET}")
        pago = int(input("¿Con cuanto cancela?: "))
        while pago < monto:
            limpiar_pantalla()
            print(f"\n{BRIGHT}{VERDE}{'▬'*60}{RESET}")
            print(f"{BRIGHT}{VERDE}PROCESANDO PAGO EN EFECTIVO{RESET}".center(60))
            print(f"{BRIGHT}{VERDE}{'▬'*60}{RESET}\n")
            print(f"Monto a pagar: {BLANCO}${monto}{RESET}")
            print(f"{BLANCO}Insuficiente. Falta ${monto - pago}{RESET}")
            pago = int(input("¿Con cuanto cancela?: "))
        cambio = pago - monto
        if cambio > 0:
            print(f"Cambio: {BLANCO}${cambio}{RESET}")
        else:
            print(f"{BLANCO}Pago exacto{RESET}")
    elif metodo == 2:
        limpiar_pantalla()
        print(f"\n{BRIGHT}{VERDE}{'▬'*60}{RESET}")
        print(f"{BRIGHT}{VERDE}PROCESANDO PAGO EN DÉBITO{RESET}".center(60))
        print(f"{BRIGHT}{VERDE}{'▬'*60}{RESET}")
        print(f"Monto a pagar: {BLANCO}${monto}{RESET}\n")
        while True:
            codigo = getpass("Código PIN (4 dígitos): ")
            if len(codigo) == 4 and codigo.isdigit():
                print(f"{BLANCO}✓ PIN verificado{RESET}")
                break
            limpiar_pantalla()
            print(f"\n{BRIGHT}{VERDE}{'▬'*60}{RESET}")
            print(f"{BRIGHT}{VERDE}PROCESANDO PAGO EN DÉBITO{RESET}".center(60))
            print(f"{BRIGHT}{VERDE}{'▬'*60}{RESET}")
            print(f"Monto a pagar: {BLANCO}${monto}{RESET}\n")
            print(f"{BLANCO}Error: Ingrese exactamente 4 dígitos{RESET}")
    elif metodo == 3:
        limpiar_pantalla()
        print(f"\n{BRIGHT}{VERDE}{'▬'*60}{RESET}")
        print(f"{BRIGHT}{VERDE}PROCESANDO PAGO EN CUOTAS{RESET}".center(60))
        print(f"{BRIGHT}{VERDE}{'▬'*60}{RESET}")
        print(f"Monto a pagar: {BLANCO}${monto}{RESET}\n")
        while True:
            codigo = getpass("Código PIN (4 dígitos): ")
            if len(codigo) == 4 and codigo.isdigit():
                print(f"{BLANCO}✓ PIN verificado{RESET}\n")
                break
            limpiar_pantalla()
            print(f"\n{BRIGHT}{VERDE}{'▬'*60}{RESET}")
            print(f"{BRIGHT}{VERDE}PROCESANDO PAGO EN CUOTAS{RESET}".center(60))
            print(f"{BRIGHT}{VERDE}{'▬'*60}{RESET}")
            print(f"Monto a pagar: {BLANCO}${monto}{RESET}\n")
            print(f"{BLANCO}Error: Ingrese exactamente 4 dígitos{RESET}")
        cuotas = 0
        while True:
            try:
                cuotas = int(input("¿En cuantas cuotas?: "))
                if cuotas > 0:
                    break
                print(f"{BLANCO}Error: Ingrese un número mayor a 0{RESET}")
            except ValueError:
                print(f"{BLANCO}Error: Ingrese un número válido{RESET}")
        valor_cuota = monto / cuotas
        print(f"{BLANCO}Pago de ${valor_cuota:.0f} x {cuotas} cuotas{RESET}")
    print(f"\n{BRIGHT}{BLANCO}✓ Su compra ha sido realizada con éxito{RESET}")

def japoncito():
    limpiar_pantalla()
    print(f'\n{BRIGHT}{VERDE}{"▬"*60}{RESET}')
    print(f'{BRIGHT}{VERDE}BIENVENIDO A RESTAURANT JAPONCITO{RESET}'.center(60))
    print(f'{BRIGHT}{VERDE}{"▬"*60}{RESET}\n')
    print(f'{BLANCO}{"─"*60}{RESET}')
    print(f"{BLANCO}¡Hola! Creamos rolls de sushi 100% personalizados{RESET}")
    print(f"{BLANCO}según tus gustos. Elige entre nuestras proteínas,{RESET}")
    print(f"{BLANCO}contornos y envolturas para crear tu roll{RESET}")
    print(f'{BLANCO}{"─"*60}\n{RESET}')
    input(f'{VERDE}Presiona ENTER para comenzar...{RESET}')
    
    total, rolls, num_roll = 0, [], 1
    
    while True:
        precio = 0
        roll = {}
        
        proteinas = {1:["Salmon","1500"],2:["Camaron","1200"],3:["Atun","1800"],
                    4:["Pollo","1000"],5:["Cerdo","1000"],6:["Carne","1200"]}
        mostrar_menu(f"ROLL #{num_roll} - PROTEINAS", proteinas)
        sel = obtener_opcion("\nSeleccione proteina (1-6): ", 1, 6)
        roll['proteina'], precio = proteinas[sel][0], int(proteinas[sel][1])
        
        print(f'\n{"="*60}\n{BRIGHT}{VERDE}QUESO CREMA{RESET}'.center(60))
        print('='*60)
        queso_opt = obtener_opcion("¿Queso crema? (1=si, 2=no): ", 1, 2)
        roll['queso'], max_cont = ('si', 1) if queso_opt == 1 else ('no', 2)
        precio += 800 if queso_opt == 1 else 0
        
        contornos = {1:["Palta","500"],2:["Pepino","300"],3:["Zanahoria","200"],
                    4:["Palmito","200"],5:["Piña","300"],6:["Cebollin","200"],7:["Queso Crema","800"]}
        contornos_sel = []
        
        while max_cont > 0:
            limpiar_pantalla()
            mostrar_menu(f"CONTORNOS ({max_cont} disponibles)", contornos)
            sel = obtener_opcion(f"\nSeleccione contorno (1-7): ", 1, 7)
            precio += int(contornos[sel][1])
            contornos_sel.append(contornos[sel][0])
            max_cont -= 1
        
        envolturas = {1:["Sesamo","100"],2:["Palta","800"],3:["Queso Crema","1000"],
                    4:["Salmon","1500"],5:["Panko","300"],6:["Tempura","200"]}
        mostrar_menu("ENVOLTURA", envolturas)
        sel = obtener_opcion("\nSeleccione envoltura (1-6): ", 1, 6)
        roll['envoltura'] = envolturas[sel][0]
        precio += int(envolturas[sel][1])
        
        roll['contornos'], roll['costo'] = contornos_sel, precio
        rolls.append(roll)
        total += precio
        
        print(f"\n{"-"*60}")
        print(f"{BRIGHT}{BLANCO}Tu roll #{num_roll}: ${precio}{RESET}")
        print(f"{"-"*60}")
        print(f"{BLANCO}• Proteína: {roll['proteina']}")
        print(f"• Queso: {roll['queso']}")
        print(f"• Contornos: {', '.join(contornos_sel)}")
        print(f"• Envoltura: {roll['envoltura']}{RESET}")
        print(f"{"-"*60}")
        
        print(f"\n{BRIGHT}{VERDE}¿QUÉ DESEA?{RESET}")
        print(f"{BLANCO}1. Agregar otro roll  │  2. Ir a pago  │  3. Cancelar{RESET}")
        opt = obtener_opcion("Seleccione opción: ", 1, 3)
        
        if opt == 1:
            num_roll += 1
            limpiar_pantalla()
        elif opt == 2:
            break
        else:
            print(f"\n{BLANCO}Compra cancelada. ¡Hasta luego!{RESET}\n")
            return
        
    limpiar_pantalla()
    print(f'\n{BRIGHT}{VERDE}{"▬"*60}{RESET}')
    print(f'{BRIGHT}{VERDE}RESUMEN DE TU PEDIDO{RESET}'.center(60))
    print(f'{BRIGHT}{VERDE}{"▬"*60}{RESET}')
    for i, r in enumerate(rolls, 1):
        cont = ', '.join(r['contornos']) if r['contornos'] else 'ninguno'
        print(f"\n{BLANCO}Roll #{i}:{RESET}")
        print(f"  • {r['proteina']} | Queso: {r['queso']} | {cont}")
        print(f"  • Envoltura: {r['envoltura']} {BLANCO}→ ${r['costo']}{RESET}")
    print(f"\n{BRIGHT}{VERDE}{"▬"*60}{RESET}")
    print(f"{BRIGHT}{BLANCO}TOTAL A PAGAR: ${total}{RESET}")
    print(f'{BRIGHT}{VERDE}{"▬"*60}{RESET}\n')
    
    pagos = {1:"Efectivo", 2:"Débito", 3:"Cuotas"}
    print(f'{BRIGHT}{VERDE}{"▬"*60}{RESET}')
    print(f'{BRIGHT}{VERDE}MÉTODO DE PAGO{RESET}'.center(60))
    print(f'{BRIGHT}{VERDE}{"▬"*60}{RESET}')
    tabla = [[k, v] for k, v in pagos.items()]
    print(tabulate(tabla, headers=["Opción", "Método"], tablefmt="grid"))
    print(f"\n{BRIGHT}{BLANCO}Monto a pagar: ${total}{RESET}\n")
    
    metodo = obtener_opcion("Seleccione método de pago (1-3): ", 1, 3)
    procesar_pago(total, metodo)
    
    input(f'{BLANCO}Presiona ENTER para continuar...{RESET}')
    limpiar_pantalla()
    print(f'{BRIGHT}{VERDE}{"▬"*60}{RESET}')
    print(f'{BRIGHT}{VERDE}MUCHAS GRACIAS POR PREFERIR JAPONCITO{RESET}'.center(60))
    print(f'{BRIGHT}{VERDE}{"▬"*60}{RESET}\n')
    
    print(f"{BRIGHT}{VERDE}¿QUÉ DESEA HACER?{RESET}")
    print(f"{BLANCO}1. Nueva compra  │  2. Salir{RESET}")
    if obtener_opcion("Seleccione opción: ", 1, 2) == 1:
        japoncito()
    else:
        print(f"\n{BRIGHT}{BLANCO}¡Gracias por visitarnos en JAPONCITO!{RESET}\n")

japoncito()
