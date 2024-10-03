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


# Test de la función hora_mas_avistamientos









