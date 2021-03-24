#cadena = "hacetreintamillonesdeañoscayounmeteoritodedoskilometrosdediametroenlassabanasdelvichadaunaregionalorientedecolombiaelimpactogenerounenormecraterenelquepocoapocofuecreciendounaselvaquehoyendaaeselhogardenoventafamiliasindigenasdelatribuseminomadasikuaniyalbergaalmenosmilquinientasespeciesdeanimalesycercademilcienespeciesdeplantassegúnestudiosdelinstitutohumboldtelcentrodeinvestigacionenbiodiversidadyecosistemasmasimportantedelcolombialuissantiagocastillobiologodelinstitutoyliderdelproyectoquebuscaestudiaryprotegerlaculturaylanaturalezadelazonacuentaportelefonoqueelantiguoagujerocausadoporuncuerpocelestemidecincuentakilometrosdediametroycombinalafaunaylafloradelassabanasconlasespeciesylavegetaciondelosbosquestropicalesdelamazonaslaselvadealiwacomolallamanlosindigenascontienebiodiversidadtipicadelosdosecosistemasestecratereslabisagraentreelllanoylaselvadicecastillo"

cadena = "PBVRQVICADSKAÑSDETSJPSIEDBGGMPSLRPWRÑPWYEDSDEÑDRDPCRCPQMNPWKUBZVSFNVRDMTIPWUEQVVCBOVNUEDIFQLONMWNUVRSEIKAZYEACEYEDSETFPHLBHGUÑESOMEHLBXVAEEPUÑELISEVEFWHUNMCLPQPMBRRNBPVIÑMTIBVVEÑIDANSJAMTJOKMDODSELPWIUFOZMQMVNFOHASESRJWRSFQCOTWVMBJGRPWVSUEXINQRSJEUEMGGRBDGNNILAGSJIDSVSUEEINTGRUEETFGGMPORDFOGTSSTOSEQOÑTGRRYVLPWJIFWXOTGGRPQRRJSKETXRNBLZETGGNEMUOTXJATORVJHRSFHVNUEJIBCHASEHEUEUOTIEFFGYATGGMPIKTBWUEÑENIEEU"


def comprobar(cadena):

    f=open("fichero.txt","w")
    j = 3
    num = 0
    long3, long4, mcd3, mcd4, long7, long8, long9, iguales3, iguales3, iguales3, iguales3, iguales3, iguales3, iguales3  = ([] for i in range(14))
    while(num <= 2):
        for i in range(len(cadena)):          
            if (num == 0):
                long3.append(cadena[i:i+j])

            elif (num == 1):
                long4.append(cadena[i:i+j+num])
        num = num + 1

    print("\n\nTrigramas: ", long3); f.write("Trigramas: "); f.write(str(long3))
    print("\n\nTetragramas: ", long4); f.write("\n\nTetragramas: "); f.write(str(long4))


    iguales3 = iguales(long3, cadena, 3)
    iguales4 = iguales(long4, cadena, 4)

    print("\n\nTrigramas repetidos: ", iguales3); f.write("\n\n\nTrigramas repetidos: "); f.write(str(iguales3))
    print("\n\nTetragramas repetidos: ", iguales4); f.write("\n\nTetragramas repetidos: "); f.write(str(iguales4))


    distanciasTrigramas = calcularDistancias(iguales3)
    distanciasTetragramas = calcularDistancias(iguales4)

    print("\n\nDistancia entre trigramas repetidos: ", distanciasTrigramas); f.write("\n\n\nDistancia entre trigramas repetidos: "); f.write(str(distanciasTrigramas))
    print("\n\nDistancia entre tetragramas repetidos: ", distanciasTetragramas); f.write("\n\nDistancia entre tetragramas repetidos: "); f.write(str(distanciasTetragramas))


    mcdTrigramas = calcularMcd(distanciasTrigramas)
    mcdTetragramas = calcularMcd(distanciasTetragramas)

    print("\n\nMCD entre trigramas repetidos: ", mcdTrigramas); f.write("\n\n\nMCD entre trigramas repetidos: "); f.write(str(mcdTrigramas))
    print("\n\nMCD entre tetragramas repetidos: ", mcdTetragramas); f.write("\n\nMCD entre tetragramas repetidos: "); f.write(str(mcdTetragramas))

         
    f.close()

def iguales(cadenas, principal, longitud):
    
    iguales = []
    val = []
    flag = 1
    aux = 0
    for i in range(len(cadenas)):
        for k in range(len(val)):
            if cadenas[i] in val[k][0]:
                flag = 0
        if (flag == 1):
            if len(cadenas[i]) == longitud:
                if (cadena.find(cadenas[i], aux, len(cadena)) != -1):
                    aux = cadena.find(cadenas[i], aux, len(cadena)) + 1
                    if (cadena.find(cadenas[i], aux, len(cadena)) != -1):
                        val.append((cadenas[i], cadena.find(cadenas[i], 0, len(cadena))))
                        while(flag != 0):
                            if (cadena.find(cadenas[i], aux, len(cadena)) != -1):
                                val.append((cadenas[i], cadena.find(cadenas[i], aux, len(cadena))))
                                aux = cadena.find(cadenas[i], aux, len(cadena)) + 1
                            else:
                                flag = 0
        flag = 1
        aux = 0
    
    return val


def calcularDistancias(cadenas):

    auxCadena = cadenas[0][0]
    auxEspacio = cadenas[0][1]

    mcd = []

    for i in range(1, len(cadenas)):
        if (cadenas[i][0] == auxCadena):
            mcd.append(cadenas[i][1] - auxEspacio)
        auxCadena = cadenas[i][0]
        auxEspacio = cadenas[i][1]

    return mcd


def calcularMcd(lista):

    resultado = []
    valor = lista[1]
    for i in range(len(lista)):
        aux = mcd(lista[i], valor)
        resultado.append(aux)
        valor = aux

    return min(resultado)


def  mcd(x, y):

    if x < y:
        return mcd(y, x)

    while y != 0:
        x, y = y, x % y

    return x

comprobar(cadena)