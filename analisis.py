import matplotlib.pyplot as plt
import numpy as np
import os


def divisionSubcritogramas(tam, cadena, carpeta, f):

    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    subcritograma = ""
    clave = []
    aux = 0

    f.write("\n----------------------------------------------------------------------------------")
    if tam != 0 and tam != 1:
        carpeta = carpeta + 1
        path = "./diagramasDeFrecuencias/subcritogramas" + str(carpeta)
        os.mkdir(path);
        while(aux < tam): 
            for i in range(aux, len(cadena), tam):
                subcritograma = subcritograma + cadena[i]
            stringSubcritograma = "Subcritograma " + str(aux+1)
            f.write("\n\n" + stringSubcritograma + ": "); f.write(subcritograma)
            aux = aux + 1
            clave.append(calculo(analisisFrecuencias(subcritograma, stringSubcritograma, path, f)))
            subcritograma = ""

    permutaciones = []
    total = []
    for i in range(len(clave)):
        if len(clave[i]) != 1 and len(clave[i]) != 0:
            for j in range(len(clave[i])):
                permutaciones.append(abc[clave[i][j]])
            total.append(permutaciones)
            permutaciones = []
        elif len(clave[i]) == 0:
            total.append("A")
        else:
            total.append(abc[clave[i][0]])

    print(total)
    return carpeta


def analisisFrecuencias(subcritograma, fichero, path, f):
    
    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    frecuencias = []
    resultado = []

    for i in range(len(abc)):
        frecuencias.append((abc[i], subcritograma.count(abc[i])))

    f.write("\n\nFrecuencias: "); f.write(str(frecuencias))

    for i in range(len(frecuencias)):
        resultado.append(frecuencias[i][1])

    
    graficarDiagramaDeFrecuencias(resultado, fichero, path)

    return resultado


def calculo(frecuencias):

    clave = []
    for i in range(len(frecuencias)):
        if frecuencias[i] >= 4:
            if frecuencias[(i+4) % 27] >= 3:
                if frecuencias[(i+4+11) % 27] >= 3:
                    if frecuencias[(i+4+11+4) % 27] >= 1:
                        clave.append(i)
                        i = i + 1
                    #elif frecuencias[(i+4+11+4) % 27] == 1:
                        #clave.append(i)
                        #i = i + 1                      
    return clave


def graficarDiagramaDeFrecuencias(frecuencias, fichero, path):
    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    x = np.arange(len(abc))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, frecuencias, width, label='Frecuencias en subcritograma')

    ax.set_ylabel('Total')
    ax.set_xticks(x)
    ax.set_xticklabels(abc)
    ax.legend()


    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')


    autolabel(rects1)

    fig.tight_layout()

    salida = path + "/" + fichero + ".png"
    fig.savefig(salida)
    plt.cla()
    plt.close()
