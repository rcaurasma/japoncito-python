# Japoncito - Sistema de Pedidos de Sushi

Sistema de simulación en Python para gestionar pedidos de sushi. Selecciona proteína, contornos y envoltura, calcula el total automáticamente y elige método de pago.

## Uso

```bash
python Japoncito.py
```

### Flujo

1. Selecciona proteína
2. Elige contornos (máx 2, o 1 si incluyes queso crema)
3. Selecciona envoltura
4. Calcula el total automáticamente
5. Opción de agregar más rolls
6. Resumen final del pedido
7. Método de pago

## Estructura

```
Japoncito/
├── Japoncito.py          # Programa principal
├── menu.py               # Módulo de selección
├── pago_efectivo.py      # Pago en efectivo
├── pago_debito.py        # Pago con débito
├── pago_cuotas.py        # Pago en cuotas
```

## Requisitos

- Python 3.7+

---

<details>
<summary><strong>🍣 Capturas de pantalla</strong></summary>

### Bienvenida

![Bienvenida](./assets/japoncito1.png)

### Selección de proteínas

![Selección de proteínas](./assets/japoncito2.png)

### Selección de contornos

![Selección de contornos](./assets/japoncito3.png)

### Resumen del roll actual

![Bienvenida](./assets/japoncito4.png)

### Resumen del pedido

![Bienvenida](./assets/japoncito5.png)

### Resumen del roll actual

![Bienvenida](./assets/japoncito6.png)

### Resumen del roll actual

![Bienvenida](./assets/japoncito7.png)

</details>
