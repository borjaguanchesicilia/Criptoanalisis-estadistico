import collections


def obtenerSubcriptogramas(subcriptograma):
    
    N = len(subcriptograma)
    frecuencias = collections.Counter(subcriptograma)
    total = 0


    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
   
    for letra in abc:
        total += frecuencias[letra] * (frecuencias[letra] - 1)

    ic = total / (N*(N-1))

    print("IC del subcriptograma %.4f" %ic)

    return round(ic, 4)
    

def subcriptogramas(cadena, longitud):
    
    inicio = 0
    media = 0
    resultado = []
    while(inicio != longitud):

        for i in range(inicio, len(cadena), longitud):
            resultado.append(cadena[i])
         
        resultado = ''.join(str(e) for e in resultado)
        print("Criptograma: ", resultado)
        media = media + obtenerSubcriptogramas(resultado)
        resultado = []
        inicio = inicio + 1
        
    print("La media es: ", media/longitud)
    
    return round(media/longitud, 4)