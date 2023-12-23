# renta_calculador.py

def calcular_renta(opcion, valor):
    if opcion == 'base':
        monto_renta = round(valor, 2)
        iva = round(monto_renta * 0.16, 2)
        retencion_isr = round(monto_renta * 0.10, 2)
        retencion_iva = round(iva * (2 / 3), 2)
        total_pagar_arrendador = round(monto_renta + iva - retencion_isr - retencion_iva, 2)
    elif opcion == 'total':
        total_pagar_arrendador = round(valor, 2)
        monto_renta = round(total_pagar_arrendador / .953333, 2)
        iva = round(monto_renta * 0.16, 2)
        retencion_isr = round(monto_renta * 0.10, 2)
        retencion_iva = round(iva * (2 / 3), 2)
    elif opcion == 'retencion':
        retencion_iva = round(valor, 2)
        iva = round(retencion_iva / (2 / 3), 2)
        monto_renta = round(iva / 0.16)
        retencion_isr = round(monto_renta * 0.10, 2)
        total_pagar_arrendador = round(monto_renta + iva - retencion_isr - retencion_iva, 2)
    elif opcion == 'iva':
        iva = round(valor, 2)
        monto_renta = round(iva / 0.16, 2)
        retencion_isr = round(monto_renta * 0.10, 2)
        retencion_iva = round(iva * (2 / 3), 2)
        total_pagar_arrendador = round(monto_renta + iva - retencion_isr - retencion_iva, 2)
    else:
        return "Opción no válida. Debes seleccionar 'base', 'total', 'retencion' o 'iva'."

    resultado = {
        'Monto_Renta': monto_renta,
        'IVA': iva,
        'Retencion_ISR': retencion_isr,
        'Retencion_IVA': retencion_iva,
        'Total_Pagar_Arrendador': total_pagar_arrendador
    }

    return resultado
