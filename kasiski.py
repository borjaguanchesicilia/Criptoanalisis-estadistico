def iguales(cadenas, principal, longitud):
    
    val = []
    flag = 1
    aux = 0
    for i in range(len(cadenas)):
        for k in range(len(val)):
            if cadenas[i] in val[k][0]:
                flag = 0
        if (flag == 1):
            if len(cadenas[i]) == longitud:
                if (principal.find(cadenas[i], aux, len(principal)) != -1):
                    aux = principal.find(cadenas[i], aux, len(principal)) + 1
                    if (principal.find(cadenas[i], aux, len(principal)) != -1):
                        val.append((cadenas[i], principal.find(cadenas[i], 0, len(principal))))
                        while(flag != 0):
                            if (principal.find(cadenas[i], aux, len(principal)) != -1):
                                val.append((cadenas[i], principal.find(cadenas[i], aux, len(principal))))
                                aux = principal.find(cadenas[i], aux, len(principal)) + 1
                            else:
                                flag = 0
        flag = 1
        aux = 0
    
    return val


def calcularDistancias(cadenas):

    mcd = []

    if cadenas != []:
        auxCadena = cadenas[0][0]
        auxEspacio = cadenas[0][1]

        for i in range(1, len(cadenas)):
            if (cadenas[i][0] == auxCadena):
                mcd.append(cadenas[i][1] - auxEspacio)
            auxCadena = cadenas[i][0]
            auxEspacio = cadenas[i][1]
    
    return mcd


def calcularMcd(lista):

    resultado = []

    if len(lista) != 0 and len(lista) != 1:
        valor = lista[1]
        for i in range(len(lista)):
            aux = mcd(lista[i], valor)
            resultado.append(aux)
            valor = aux

        return min(resultado)
    else:
        return 0


def  mcd(x, y):

    if x < y:
        return mcd(y, x)

    while y != 0:
        x, y = y, x % y

    return x


def kasiski(cadena):

    f = open("kasiski.txt","w")
    j = 3
    long3, long4, long5, long6, long7, long8 = ([] for i in range(6))
    num = mcdTrigrafos = mcdTetragrafos = mcdPentagrafos = mcdHexagrafos = mcdHeptagrafos = mcdOctografos = 0

    # Se obtiene el criptograma dividido en n-grafos
    
    while(num <= 8):
        for i in range(len(cadena)):          
            if (num == 0):
                long3.append(cadena[i:i+j])

            elif (num == 1):
                long4.append(cadena[i:i+j+num])

            elif (num == 2):
                long5.append(cadena[i:i+j+num])

            elif (num == 3):
                long6.append(cadena[i:i+j+num])

            elif (num == 4):
                long7.append(cadena[i:i+j+num])

            elif (num == 5):
                long8.append(cadena[i:i+j+num])
        num = num + 1

    f.write("Trigrafos: "); f.write(str(long3))
    f.write("\n\nTetragrafos: "); f.write(str(long4))
    f.write("\n\nPentagrafos: "); f.write(str(long5))
    f.write("\n\nHexagrafos: "); f.write(str(long6))
    f.write("\n\nHeptagrafos: "); f.write(str(long7))
    f.write("\n\nOctografos: "); f.write(str(long8))


    # Se obtienen las secuencias de caracteres repetidas en los n-grafos

    iguales3 = iguales(long3, cadena, 3)
    iguales4 = iguales(long4, cadena, 4)
    iguales5 = iguales(long5, cadena, 5)
    iguales6 = iguales(long6, cadena, 6)
    iguales7 = iguales(long7, cadena, 7)
    iguales8 = iguales(long8, cadena, 8)

    f.write("\n\n\nTrigrafos repetidos: "); f.write(str(iguales3))
    f.write("\n\nTetragrafos repetidos: "); f.write(str(iguales4))
    f.write("\n\nPentagrafos repetidos: "); f.write(str(iguales5))
    f.write("\n\nHexagrafos repetidos: "); f.write(str(iguales6))
    f.write("\n\nHeptagrafos repetidos: "); f.write(str(iguales7))
    f.write("\n\nOctografos repetidos: "); f.write(str(iguales8))


    # Se calculan las distancias entre las secuencias de caracteres repetidas en los n-grafos

    distanciasTrigrafos = calcularDistancias(iguales3)
    distanciasTetragrafos = calcularDistancias(iguales4)
    distanciasPentagrafos = calcularDistancias(iguales5)
    distanciasHexagrafos = calcularDistancias(iguales6)
    distanciasHeptagrafos = calcularDistancias(iguales7)
    distanciasOctografos = calcularDistancias(iguales8)

    f.write("\n\n\nDistancia entre Trigrafos repetidos: "); f.write(str(distanciasTrigrafos))
    f.write("\n\nDistancia entre Tetragrafos repetidos: "); f.write(str(distanciasTetragrafos))
    f.write("\n\nDistancia entre Pentagrafos repetidos: "); f.write(str(distanciasPentagrafos))
    f.write("\n\nDistancia entre Hexagrafos repetidos: "); f.write(str(distanciasHexagrafos))
    f.write("\n\nDistancia entre Heptagrafos repetidos: "); f.write(str(distanciasHeptagrafos))
    f.write("\n\nDistancia entre Octografos repetidos: "); f.write(str(distanciasOctografos))


    # Se aplica el mcd a las distancias entre las secuencias de caracteres repetidas en los n-grafos. 
    # Se obtendrá la longitud de la clave

    mcdTrigrafos = calcularMcd(distanciasTrigrafos)
    mcdTetragrafos = calcularMcd(distanciasTetragrafos)
    mcdPentagrafos = calcularMcd(distanciasPentagrafos)
    mcdHexagrafos = calcularMcd(distanciasHexagrafos)
    mcdHeptagrafos = calcularMcd(distanciasHeptagrafos)
    mcdOctografos = calcularMcd(distanciasOctografos)


    f.write("\n\n\nMCD entre Trigrafos repetidos: "); f.write(str(mcdTrigrafos))
    f.write("\n\nMCD entre Tetragrafos repetidos: "); f.write(str(mcdTetragrafos))
    f.write("\n\nMCD entre Pentagrafos repetidos: "); f.write(str(mcdPentagrafos))
    f.write("\n\nMCD entre Hexagrafos repetidos: "); f.write(str(mcdHexagrafos))
    f.write("\n\nMCD entre Heptagrafos repetidos: "); f.write(str(mcdHeptagrafos))
    f.write("\n\nMCD entre Octografos repetidos: "); f.write(str(mcdOctografos))


    return mcdTrigrafos, mcdTetragrafos, mcdPentagrafos, mcdHexagrafos, mcdHeptagrafos, mcdOctografos
