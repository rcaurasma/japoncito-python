def debito(monto):
        while True:
            nombre = input("Por favor, ingrese su nombre de usuario:").strip()
            clave = input("Por favor, ingrese su contraseña:").strip()
            if nombre == 'alex' and clave == '1234':
                print("Credenciales correctas. Bienvenido,", nombre)
                break
                
            else:
                print("Credenciales incorrectas. Por favor, ingrese sus datos nuevamente.")
        print("El monto a pagar es de:",monto)
        pago = int(input("¿Con cuanto cancela?: "))
        print("Usted canceló con ",pago)
        cambio = pago - monto
        while cambio < 0:
            print("El pago es insuficiente. Usted aún debe:", cambio)
            pago = int(input("¿Con cuánto cancela?: "))
            cambio = pago - monto
            print("Usted cancela con ", pago)
            print("Usted quedó con una deuda de: ", cambio)
        if cambio == 0:
            print("El pago es suficiente. No hay cambio.")
        else:
            print("Su cambio es:", cambio)
        print("Su compra ha sido realizada con éxito.")
        print("¡Muchas gracias por su compra!")

debito()