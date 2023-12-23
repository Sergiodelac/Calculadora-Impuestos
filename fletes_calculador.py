# fletes_calculador.py

def calcular_fletes(opcion, valor):
    if opcion == 'base':
        monto_fletes = round(valor, 2)
        iva = round(monto_fletes * 0.16, 2)
        retencion_iva = round(iva * 0.04, 2)  # Cambio aquí
        total_pagar = round(monto_fletes + iva - retencion_iva, 2)
    elif opcion == 'total':
        total_pagar = round(valor, 2)
        monto_fletes = round(total_pagar / 1.1536, 2)  # Corregido aquí
        iva = round(monto_fletes * 0.16, 2)
        retencion_iva = round(iva * 0.04, 2)
    elif opcion == 'retencion':
       retencion_iva = round(valor, 2)
       iva = round(retencion_iva / 0.04, 2)
       monto_fletes = round(iva / 0.16, 2)
       total_pagar = round(monto_fletes + iva - retencion_iva, 2)
    elif opcion == 'iva':
        iva = round(valor, 2)
        retencion_iva = round(iva * 0.04, 2)
        monto_fletes = round(iva / 0.16, 2)
        total_pagar = round(monto_fletes + iva - retencion_iva, 2)
    else:
        return "Opción no válida. Debes seleccionar 'base', 'total', 'retencion' o 'iva'."

    resultado = {
        'Monto_Fletes': monto_fletes,
        'IVA': iva,
        'Retencion_IVA': retencion_iva,
        'Total_Pagar': total_pagar
    }

    return resultado
