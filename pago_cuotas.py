def cuotas(monto):    
    while True:
        nombre = input("Por favor, ingrese su nombre de usuario:").strip()
        clave = input("Por favor, ingrese su contraseña:").strip()
        if nombre == 'alex' and clave == '1234':
            print("Credenciales correctas. Bienvenido,", nombre)
            break
        else:
            print("Credenciales incorrectas. Por favor, ingrese sus datos nuevamente.")
    cuotas = int(input("¿En cuántas cuotas desea pagar?: "))
    while cuotas <= 0:
        print("La cantidad de cuotas debe ser mayor que cero.")
        cuotas = int(input("¿En cuántas cuotas desea pagar?: "))
    
    pago_mensual = monto / cuotas
    
    print("El monto a pagar es de:", monto)
    print("Usted ha elegido pagar en", cuotas, "cuotas de", int(pago_mensual), "cada una.")
    
    print("Su compra ha sido realizada con éxito.")
    print("¡Muchas gracias por su compra!")