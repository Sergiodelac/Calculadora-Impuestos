# comisiones_calculador.py
def calcular_comisiones(opcion, valor):
    try:
        valor = float(valor)
    except ValueError:
        return "Error: Ingrese un valor numérico válido."

    if opcion == 'base':
        monto_comision = valor
        iva = round(monto_comision * 0.16, 2)  # Suponiendo una tasa de IVA del 16%
        retencion_iva = round(iva * (2 / 3), 2)
        total_pagar_arrendador = round(monto_comision + iva - retencion_iva, 2)
    elif opcion == 'total':
        total_pagar_arrendador = valor
        monto_comision = round(total_pagar_arrendador / (1 + 0.16), 2)  # Monto de Comisión
        iva = round(monto_comision * 0.16, 2)  # IVA basado en el Monto de Comisión
        retencion_iva = round(iva * (2 / 3), 2)  # Retención IVA basada en el IVA
        # Se mantiene el Total a Pagar al Arrendador igual al valor ingresado
        total_pagar_arrendador = round(total_pagar_arrendador, 2)
    elif opcion == 'retencion':
        retencion_iva = valor
        iva = round(retencion_iva / (2 / 3), 2)
        monto_comision = round(iva / 0.16, 2)
        total_pagar_arrendador = round(monto_comision + iva - retencion_iva, 2)
    elif opcion == 'iva':
        iva = valor
        retencion_iva = round(iva * (2 / 3), 2)
        monto_comision = round(iva / 0.16, 2)
        total_pagar_arrendador = round(monto_comision + iva - retencion_iva, 2)
    else:
        return "Opción no válida. Debes seleccionar 'base', 'total', 'retencion' o 'iva'."

    resultado = {
        "Monto_Comision": monto_comision,
        "IVA": iva,
        "Retencion_IVA": retencion_iva,
        "Total_Pagar_Arrendador": total_pagar_arrendador
    }

    return resultado
