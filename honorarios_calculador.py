# honorarios_calculador.py
def calcular_honorarios(opcion, valor):
    try:
        valor = float(valor)
    except ValueError:
        return "Error: Ingrese un valor numérico válido."

    if opcion == 'base':
        base = valor
        iva = round(base * 0.16, 2)  # Suponiendo una tasa de IVA del 16%
        retencion_isr = round(base * 0.10, 2)  # Retención ISR del 10%
        retencion_iva = round(iva * (2 / 3), 2)
        honorarios = base  # Aquí establecemos que los honorarios sean igual al valor proporcionado
        total_pagar = round(base + iva - retencion_isr - retencion_iva, 2)
    elif opcion == 'total':
        total_pagar = valor
        honorarios = round(total_pagar / .953333, 2)
        iva = round(honorarios * 0.16, 2)
        retencion_isr = round(honorarios * 0.10, 2)
        retencion_iva = round(iva * (2 / 3), 2)
    elif opcion == 'retencion':
        retencion_iva = valor
        iva = round(retencion_iva / (2 / 3), 2)
        honorarios = round(iva / 0.16, 2)
        retencion_isr = round(honorarios * 0.10, 2)
        total_pagar = round(honorarios + iva - retencion_isr - retencion_iva, 2)

    elif opcion == 'iva':
        iva = valor
        retencion_iva = round(iva * (2 / 3), 2)
        honorarios = round(iva / 0.16, 2)
        retencion_isr = round(honorarios * 0.10, 2)
        total_pagar = round(honorarios + iva - retencion_isr - retencion_iva, 2)
    else:
        return "Opción no válida. Debes seleccionar 'base', 'total', 'retencion' o 'iva'."

    resultado = {
        "Honorarios": honorarios,
        "IVA": iva,
        "Retencion_ISR": retencion_isr,
        "Retencion_IVA": retencion_iva,
        "Total_Pagar": total_pagar
    }

    return resultado


