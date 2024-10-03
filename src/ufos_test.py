from ufos import *

# Test de la función lee_avistamientos
avistamientos = lee_avistamientos('../data/ovnis.csv')
for a in avistamientos:
    print(a)

#Test de la función duracion_total
duracion_total(avistamientos, 'in')
duracion_total(avistamientos, 'nm')
duracion_total(avistamientos, 'pa')
duracion_total(avistamientos, 'wa')

# Test de la función comentario_mas_largo
anyo = 2009
palabra = "ghostly"
avistamiento_mas_largo = comentario_mas_largo(avistamientos, anyo, palabra)

if avistamiento_mas_largo:
    print("Avistamiento con el comentario más largo:")
    print(avistamiento_mas_largo)



# Test de la función indexa_formas_por_mes
formas_por_mes = indexa_formas_por_mes(avistamientos)
for mes, formas in formas_por_mes.items():
    print(f"{mes}: {formas}")

from datetime import date

# Test de la función avistamientos_fechas
fecha_inicial = date(2005, 5, 1)
fecha_final = date(2005, 6, 1)

avistamientos_rango = avistamientos_fechas(avistamientos, fecha_inicial, fecha_final)

print(f"Mostrando los avistamientos entre el {fecha_inicial} y el {fecha_final}:")
for avistamiento in avistamientos_rango:
    print(avistamiento)



# Test de la función hora_mas_avistamientos
hora_mas_frecuente = hora_mas_avistamientos(avistamientos)

# Test de la función dicc_estado_longitud_media_comentario
longitud_media_comentarios = dicc_estado_longitud_media_comentario(avistamientos)
for estado, media in longitud_media_comentarios.items():
    print(f" {estado}:, {media:.2f}")










