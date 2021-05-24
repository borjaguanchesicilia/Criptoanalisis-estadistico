import collections


def obtenerIC(subcriptograma, g):
    
    N = len(subcriptograma)
    frecuencias = collections.Counter(subcriptograma)
    total = 0

    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
   
    for letra in abc:
        total += frecuencias[letra] * (frecuencias[letra] - 1)

    IC = total / (N*(N-1))

    g.write("\n\nIC del subcriptograma %.4f" %IC)

    return round(IC, 4)
    

def obtenerICsubcriptogramas(cadena, longitud, g):
    
    inicio = media = 0
    resultado = []
    while(inicio != longitud):

        for i in range(inicio, len(cadena), longitud):
            resultado.append(cadena[i])
         
        resultado = ''.join(str(e) for e in resultado)
        g.write("\n\nEl subcriptograma es: ");g.write(str(resultado))
        media = media + obtenerIC(resultado, g)
        resultado = []
        inicio = inicio + 1
        
    g.write("\n\n\nLa media entre el IC y la potencial longitud de clave es: ");g.write(str(media/longitud))
    
    return round(media/longitud, 4)
    

def calculoIC(cadena):

    g = open("indiceCoincidencia.txt","w")
    g.write("El análisis por índice de coincidencia es el siguiente: \n\n")

    mediasIC = []
    longitudClave = 1

    while longitudClave <= 10:

        if longitudClave == 1:
            mediasIC.append(obtenerIC(cadena, g))
        else:
            g.write("\n\n-----------------------------------------------------------------------------")
            g.write("\n\n\nDivision del criptograma en ");g.write(str(longitudClave));g.write(" subcritogramas.")
            mediasIC.append(obtenerICsubcriptogramas(cadena, longitudClave, g))
        longitudClave = longitudClave + 1
        
    probabilidadIC = 0

    for i in range(len(mediasIC)):
        if (round((mediasIC[i] / 0.0775), 3)) >= 0.90:
            probabilidadIC = i+1
            break;

    g.write("\n\n-----------------------------------------------------------------------------")
    g.write("\n\nLa longitud de la clave de acuerdo al IC es: ");g.write(str(probabilidadIC))

    return probabilidadIC
