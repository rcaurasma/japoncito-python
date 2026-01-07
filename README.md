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
<summary><strong>📸 Capturas de pantalla</strong></summary>

### Menú de proteínas

![Proteínas](./screenshots/proteinas.png)

### Selección de contornos

![Contornos](./screenshots/contornos.png)

### Resumen del pedido

![Resumen](./screenshots/resumen.png)

### Método de pago

![Pago](./screenshots/pago.png)

</details>
