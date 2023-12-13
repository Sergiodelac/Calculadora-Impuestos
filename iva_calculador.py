# iva_calculador.py
def calcular_iva(opcion, valor):
    try:
        valor = float(valor)
    except ValueError:
        return "Error: Ingrese un valor numérico válido."

    if opcion == 'base':
        base = valor
        iva = base * 0.16  # Suponiendo una tasa de IVA del 16%
        total = base + iva
    elif opcion == 'total':
        total = valor
        base = total / 1.16  
        iva = total - base
    elif opcion == 'iva':
        iva = valor
        base = iva / 0.16
        total = base + iva
    else:
        return "Opción no válida. Debes seleccionar 'base', 'total' o 'iva'."

    return f"Base: {base:.2f} | IVA: {iva:.2f} | Total: {total:.2f}"


