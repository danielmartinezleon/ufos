from datetime import datetime
from collections import namedtuple
import csv

def lee_avistamientos(fichero):
    Avistamiento = namedtuple('Avistamiento', 'fecha, hora, lugar, estado, forma, duracion, descripcion, latitud, longitud')
    avistamientos = []

    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)

        for fila in lector:
            fecha_hora_str = fila[0]
            lugar = fila[1]
            estado = fila[2]
            forma = fila[3]
            duracion = fila[4]
            descripcion = fila[5]
            latitud = fila[6]
            longitud = fila[7]

            fecha_hora = datetime.strptime(fecha_hora_str, '%m/%d/%Y %H:%M')
            fecha = fecha_hora.date()
            hora = fecha_hora.time()

            avistamiento = Avistamiento(fecha, hora, lugar, estado, forma, duracion, descripcion, latitud, longitud)
            avistamientos.append(avistamiento)

    avistamientos_ordenados = sorted(avistamientos, key=lambda x: (x.fecha, x.hora))

    return avistamientos_ordenados

def duracion_total(registros, estado):
    duracion_total = 0
    for avistamiento in registros:
        if avistamiento.estado.lower() == estado.lower():
            duracion_total += int(avistamiento.duracion)
    print(f"Duración total de los avistamientos en {estado}: {duracion_total} segundos.")
    return duracion_total

def comentario_mas_largo(registros, anyo, palabra):
    avistamientos_filtrados = [
        avistamiento for avistamiento in registros
        if avistamiento.fecha.year == anyo and palabra.lower() in avistamiento.descripcion.lower()
    ]

    if not avistamientos_filtrados:
        print(f"No se encontraron avistamientos en {anyo} que contengan la palabra '{palabra}'.")
        return None


    avistamiento_con_comentario_mas_largo = max(avistamientos_filtrados, key=lambda x: len(x.descripcion))

    return avistamiento_con_comentario_mas_largo


def indexa_formas_por_mes(registros):
    nombres_meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                     'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

    formas_por_mes = {mes: set() for mes in nombres_meses}

    for avistamiento in registros:
        nombre_mes = nombres_meses[avistamiento.fecha.month - 1]
        formas_por_mes[nombre_mes].add(avistamiento.forma)

    return formas_por_mes

def avistamientos_fechas(registros, fecha_inicial=None, fecha_final=None):

    if fecha_inicial is None and fecha_final is None:
        registros_filtrados = registros
    else:
        registros_filtrados = []
        for avistamiento in registros:
            fecha_avistamiento = avistamiento.fecha

            if fecha_inicial and fecha_final:
                if fecha_inicial <= fecha_avistamiento <= fecha_final:
                    registros_filtrados.append(avistamiento)
            elif fecha_inicial:
                if fecha_avistamiento >= fecha_inicial:
                    registros_filtrados.append(avistamiento)
            elif fecha_final:
                if fecha_avistamiento <= fecha_final:
                    registros_filtrados.append(avistamiento)

    registros_filtrados.sort(key=lambda x: x.fecha, reverse=True)

    return registros_filtrados

def hora_mas_avistamientos(registros):
    contador_horas = {hora: 0 for hora in range(24)}

    for avistamiento in registros:
        hora = avistamiento.hora.hour
        contador_horas[hora] += 1

    hora_mas_frecuente = max(contador_horas, key=contador_horas.get)

    print(f"Hora en la que se han observado más avistamientos: {hora_mas_frecuente}")
    return hora_mas_frecuente

def dicc_estado_longitud_media_comentario(registros):
    suma_longitudes = {}
    contador_avistamientos = {}

    for avistamiento in registros:
        estado = avistamiento.estado
        longitud_comentario = len(avistamiento.descripcion)

        if estado not in suma_longitudes:
            suma_longitudes[estado] = 0
            contador_avistamientos[estado] = 0

        suma_longitudes[estado] += longitud_comentario
        contador_avistamientos[estado] += 1

    longitud_media_por_estado = {estado: suma_longitudes[estado] / contador_avistamientos[estado]
                                 for estado in suma_longitudes}

    return longitud_media_por_estado
