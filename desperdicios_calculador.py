# desperdicios_calculador.py

def calcular_desperdicios(opcion, valor):
    if opcion == 'base':
        monto_desperdicio = round(valor, 2)
        iva = round(monto_desperdicio * 0.16, 2)
        retencion_iva = round(iva * (2 / 3), 2)  # Retención IVA como las 2/3 partes del IVA
        total_pagar = round(monto_desperdicio + iva - retencion_iva, 2)
    elif opcion == 'total':
        total_pagar = round(valor, 2)
        monto_desperdicio = round(total_pagar /  1.053334, 2)  # Monto de Desperdicio
        iva = round(monto_desperdicio * 0.16, 2)  # IVA basado en el Monto de Desperdicio
        retencion_iva = round(iva * (2 / 3), 2)  # Retención IVA como las 2/3 partes del IVA    
    elif opcion == 'retencion':
        retencion_iva = round(valor, 2)
        iva = round(retencion_iva / (2 / 3), 2)  # IVA como las 2/3 partes de la retención de IVA
        monto_desperdicio = round(iva / 0.16, 2)
        total_pagar = round(monto_desperdicio + iva - retencion_iva, 2)
    elif opcion == 'iva':
        iva = round(valor, 2)
        retencion_iva = round(iva * (2 / 3), 2)  # Retención IVA como las 2/3 partes del IVA
        monto_desperdicio = round(iva / 0.16, 2)
        total_pagar = round(monto_desperdicio + iva - retencion_iva, 2)
    else:
        return "Opción no válida. Debes seleccionar 'base', 'total', 'retencion' o 'iva'."

    resultado = {
        'Monto_Desperdicio': monto_desperdicio,
        'IVA': iva,
        'Retencion_IVA': retencion_iva,
        'Total_Pagar': total_pagar
    }

    return resultado

