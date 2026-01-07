Resumen rápido del estado

Código disperso: hay lógica de menú y de pago replicada en varios archivos y con ejecución a nivel de módulo (llamadas top-level), lo que impide importarlos sin efectos laterales.
Funciones con bugs: varias funciones imprimen o piden datos pero no retornan valores; otras se llaman sin pasar argumentos (p. ej. debito() sin monto).
Flujo incompleto: sushi_japoncito contiene el flujo principal pero no usa los módulos de pago; Funcion_Menu/Funcion_Menu2 contienen partes del menú pero no están organizadas para ser reutilizadas.
Qué conservar, fusionar y archivar/eliminar

Conservar y convertir en módulos limpios:
sushi_Japoncito.py — mantener como punto de entrada (refactorizar).
Funcion_Menu.py y Funcion_Menu2.py — fusionar en un único módulo (ej. menu.py) con funciones que reciben entrada y retornan selección y precio.
pago_debito.py, pago_cuotas.py, pagos_efectivo.py — fusionar en payments.py con funciones claras (aceptar monto, gestionar credenciales/inputs y retornar resultado).
Archivar/Eliminar (temporalmente mover a carpeta archive):
Import.py (no aporta; contiene import y print roto).
maquina_de_pagos.py (duplicado/confuso).
dic.py, Japoncito.py, tempCodeRunnerFile.py — revisar si contienen ideas útiles; si no, mover a archive.
Plan paso a paso (ejecutable, sin código listo)

Hacer copia de seguridad / crear carpeta archive:
Mueve los archivos que no vas a tocar ahora a archive para no perderlos.
Crear módulo de menú (ej. menu.py):
Extrae de Funcion_Menu/Funcion_Menu2 las funciones del menú.
Cada función debe: pedir/validar la entrada, y RETURN un valor estructurado (p. ej. ('Salmon',1500) o {'nombre':'Salmon','precio':1500}).
Evita prints masivos dentro de la lógica; devuelve valores y deja la impresión para el main o una función de presentación.
Diseñar estructura de datos del pedido:
Usa una lista de diccionarios: cada roll = {'proteina':..., 'contornos':[...], 'envoltura':..., 'precio':int}.
Implementa funciones auxiliares: add_roll(), calculate_total(orders), describe_order(orders).
Refactorizar sushi_japoncito.py como "main":
Importa menu.py y payments.py.
Loop principal: permitir agregar roll(s) llamando a funciones de menu, añadir al pedido, preguntar si desea otro roll.
Al finalizar, calcular total con calculate_total y mostrar resumen claro antes del pago.
Añadir if __name__ == "__main__": main() para permitir import sin ejecutar.
Crear módulo payments.py:
Unificar pago_efectivo, debito y cuotas.
Firmas claras: pago_efectivo(monto) -> devuelve {'status': True, 'metodo':'efectivo', 'cambio': X}, debito(monto) -> similar, cuotas(monto, n_cuotas) -> similar.
No ejecute nada al import; sólo definir funciones.
Integración y manejo de errores:
En main, según opción de pago, llamar a la función correspondiente con el monto.
Validar entradas (números, opciones) y manejar excepciones ValueError.
Si el pago falla, permitir reintentos o volver al resumen.
Pruebas manuales y automatizadas:
Probar escenarios: 1 roll, múltiples rolls; pago sufciente; pago insuficiente; cuotas.
Considera añadir un pequeño test script o usar asserts para las funciones puras (calculate_total, parse_selections).
Limpieza final:
Eliminar o archivar los módulos duplicados.
Añadir README corto con instrucciones para ejecutar: comando python sushi_japoncito.py.
Conceptos de Python a repasar (breve lista)

Funciones y valores de retorno vs. efectos secundarios (print/input): preferir return para lógica reutilizable.
Modularización e imports: cada archivo debe exponer funciones sin ejecutar lógica al import (usar if __name__ == "__main__":).
Estructuras de datos: listas y diccionarios para representar órdenes.
Validación y manejo de errores: try/except y validación de tipos.
Separación de responsabilidades (Separation of Concerns): UI/input, lógica de negocio, y pago deberían estar separados.
Testing básico: pruebas unitarias simples para funciones puras (calculo de total).
Buenas prácticas: nombres claros, evitar código duplicado, documentar funciones (docstrings).
Pequeños checks / cosas que corregir inmediatamente

Quitar llamadas top-level en pago_debito.py y similares (no llamar a debito() sin argumentos).
Hacer que las funciones de menú retornen datos en lugar de asignar variables globales.
Revisar coherencia de índices y claves en diccionarios/tuplas (p. ej. índices fuera de rango).
Sanitizar inputs: .strip().lower() y validar int con try/except.
Siguiente paso recomendado (acción que puedes hacer ahora)

Mueve a archive los archivos que mencioné y crea un archivo menu.py vacío + payments.py vacío; luego dime si prefieres que te guíe paso a paso en la refactorización (te doy el orden exacto de cambios y las firmas de las funciones), o si quieres que yo aplique los cambios y los pruebe aquí.