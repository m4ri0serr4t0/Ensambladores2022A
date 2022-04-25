string = 'comentario    ;'
s = string.index(';')
print(s)

for i in listaElementos:
    stringElementos += i + '\n'

textoElementos = ''
textoTotal = ''
for i in listaElementos:  # recorrido analizador de cada una de las palabras
    palabra = str(i)
    palabra2 = listaElementos[listaElementos.index(palabra) + 1]
    newtextRegistros = palabra[0:2]
    if (newtextRegistros in registers) or (newtextRegistros in (i.lower() for i in
                                                                registers)):  # Hace recorrido para todos los elementos de la lista registros en minuscula
        textoTotal += (newtextRegistros + '  ------> Es Registro' + '\n')

    if (palabra in instrucciones) or (palabra in (i.lower() for i in
                                                  instrucciones)):  # Hace recorrido para todos los elementos de la lista registros en minuscula
        textoTotal += (palabra + '------> Es Instrucción' + '\n')
    if validarSimbolo(palabra):
        textoTotal += (palabra + '------> Es Simbolo' + '\n')
    if palabra2 == 'segment':
        textoElementos += (palabra + ' ' + palabra2 + '\n')


    else:

        if validarComentario(palabra) and palabra != 'segment':
            textoElementos += (palabra + '\n')


        else:
            pass