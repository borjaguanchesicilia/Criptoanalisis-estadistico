#cadena = "hacetreintamillonesdeañoscayounmeteoritodedoskilometrosdediametroenlassabanasdelvichadaunaregionalorientedecolombiaelimpactogenerounenormecraterenelquepocoapocofuecreciendounaselvaquehoyendaaeselhogardenoventafamiliasindigenasdelatribuseminomadasikuaniyalbergaalmenosmilquinientasespeciesdeanimalesycercademilcienespeciesdeplantassegunestudiosdelinstitutohumboldtelcentrodeinvestigacionenbiodiversidadyecosistemasmasimportantedelcolombialuissantiagocastillobiologodelinstitutoyliderdelproyectoquebuscaestudiaryprotegerlaculturaylanaturalezadelazonacuentaportelefonoqueelantiguoagujerocausadoporuncuerpocelestemidecincuentakilometrosdediametroycombinalafaunaylafloradelassabanasconlasespeciesylavegetaciondelosbosquestropicalesdelamazonaslaselvadealiwacomolallamanlosindigenascontienebiodiversidadtipicadelosdosecosistemasestecratereslabisagraentreelllanoylaselvadicecastillo"

cadena = "PBVRQVICADSKAÑSDETSJPSIEDBGGMPSLRPWRÑPWYEDSDEÑDRDPCRCPQMNPWKUBZVSFNVRDMTIPWUEQVVCBOVNUEDIFQLONMWNUVRSEIKAZYEACEYEDSETFPHLBHGUÑESOMEHLBXVAEEPUÑELISEVEFWHUNMCLPQPMBRRNBPVIÑMTIBVVEÑIDANSJAMTJOKMDODSELPWIUFOZMQMVNFOHASESRJWRSFQCOTWVMBJGRPWVSUEXINQRSJEUEMGGRBDGNNILAGSJIDSVSUEEINTGRUEETFGGMPORDFOGTSSTOSEQOÑTGRRYVLPWJIFWXOTGGRPQRRJSKETXRNBLZETGGNEMUOTXJATORVJHRSFHVNUEJIBCHASEHEUEUOTIEFFGYATGGMPIKTBWUEÑENIEEU"

#cadena = "IOOHUGQLÑINOJZXRÑSFGFOARTQNBPJZOFIQRSWGRESPRTYUÑPAQWSDFGFRUDNSGUPSZÑBHFDCOZDTRQÑWWOKBRNXÑOEHHWBPBZBUJSZWFRQFPZBOCWNHMWYSBQGRHSZHSDHPFBBUNSOUBIQUFBQÑRJQSPQBDQDORGJQFSSOLFBPRVBNVFZIDRJQKPNQPEONHTSXKPUNUESZRWSZWBTNOJZUDTWZGJUQPBHPHMOGUJPHVFAUPPANGBHUNVOZLZOXEFGSDBZYHÑDFOJZDXJBUHÑINVFHCHDWQVESNPJANÑFHLFFGODESYLMQUHÑSFSFQUHTRQSMOZWBHFHHJZHTIHGJDFGFZUPTIUWVIBKVAÑRMRGHMQQPUGBGFWZYFHGLHOOLPBQPCWBGJKQUTWPDENQFPHUVUSYDTANVJACRSINPUSPHMQBÑPAÑLBZHLTHNPUWNJPQNVUWXÑPPURMDSRESXLÑHGLUJGRZZUGFGPHMEERZSOWPFHHCJFFBSFWVRUDSNCUPIQJFGXDDJXWVGNBMOZDUJEDMSMDESXDADZDDJQPUOCRSIQÑFTBPPFHHFZNPUWSXPOSXKSERDOHVBRBSPGHPDJQUQDOHMSFWFAUGFQUPDJQPUOWLMDYHUGBVESPLBAQWSDLFPAÑLÑOXDGOHPBNXDGZBUBRQÑBHFDCOZDTQBPMOFHTEQFJSFBMOIHHSGDDWBPESXRTPBVRJQVUGBSJQNÑFHPHMOYDADZDTZNVFZIDESNÑJLNFPABÑBZXDNOZÑPHUPEWSHÑOFFPBGLFBQEJDPLWSEVJRNGUWCLDOPHMDFGPHQFPHUVUSYDTSFWFQEDUSEHTZNEJHNJSOQPUGQHMZXDÑDLÑBHQÑWOPLDSODTIUÑMD"

#cadena = "HRVMYZGPNEADBSPWOMSÑERHWXKCGOFNDXBJWTPTZDVWWXRKSOWELLWXLGLILMVNZTMOSADSRUIRIULEVVZVOFLCCNLRVZPTUCSOCIVGBJLGKOVODUPFMNPMAATNWLMOMRZUEXUTZÑMCCALXZJUGSQFEHIKTIRWCZFMXKWMEPEXDGÑUFAGSVLQMXOTGGUDLAVMMPOQÑACDVGWAMOBAPADBSNIUPNÑIXXUFAFMLLTJBJZAGTIXODTLFAKRULNZRIPJGZGLACFMRWUTIVQMBUNMOBADEKJMHPGADOAEBTFSGAYNEJVIIMÑPLNIVGMXXGKIOSUXXPIOBADSVZCRMUBUÑIGMLJSKUSEILÑBTOWTBZLUNMPKGUTCOUXPRDGATSGRVPTUGUBSOUBDJZUPDLDPXKTAKATOMRMTFAKTPZRLTUYMFMLNOCITGPCSUSSKTUYPCÑONAKNPPSQJIZLGZWIMNPNDTZNCYWASIÑEJWMPXTWYOCLIYZMDCSNAVMBZLKIRJPJIBJÑGZLLCMEBZZCGLLNRNCWINMZLDVEIEWOICFEENIUWTBEVEWIUTYWMEVAENPLCQIGFJVLWHIWAAÑOHIZZUECECPGVMPMUBEWIUXKNUECEXTRDPPWÑMTCOKWMIPCTEERGRKTTDPNLLRYIZUCGLLFCIZFLGSADSRUIRIUKOXLRMMXXGKIOSPEIAMIMTLCZIUIMNWSMOKKCJAVZOAITTSJAFMLLMRSWRIUSADECOIIMCSIHATITTSCSLLMRGSTAKUDSGVGIXKQUTSEEXJNWFPVORKBLFLVPPSCRWMPWULODETIANAVMMLSVMBJKTITORVMSFJKAAQRRXUYZGMLVLRGWDSCAEVVRWPHMEISEICEW"


def comprobar(cadena):

    f=open("analisis.txt","w")
    j = 3
    num = 0
    long3, long4, mcd3, mcd4, long5, long6, long7, long8, mcd5, mcd6, mcd7, mcd8 = ([] for i in range(12))
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

    print("\n\nTrigramas: ", long3); f.write("Trigramas: "); f.write(str(long3))
    print("\n\nTetragramas: ", long4); f.write("\n\nTetragramas: "); f.write(str(long4))


    iguales3 = iguales(long3, cadena, 3)
    iguales4 = iguales(long4, cadena, 4)
    iguales5 = iguales(long5, cadena, 5)
    iguales6 = iguales(long6, cadena, 6)
    iguales7 = iguales(long7, cadena, 7)
    iguales8 = iguales(long8, cadena, 8)

    print("\n\nTrigramas repetidos: ", iguales3); f.write("\n\n\nTrigramas repetidos: "); f.write(str(iguales3))
    print("\n\nTetragramas repetidos: ", iguales4); f.write("\n\nTetragramas repetidos: "); f.write(str(iguales4))
    print("\n\n5gramas repetidos: ", iguales5); f.write("\n\n5gramas repetidos: "); f.write(str(iguales5))
    print("\n\n6gramas repetidos: ", iguales6); f.write("\n\n6gramas repetidos: "); f.write(str(iguales6))
    print("\n\n7gramas repetidos: ", iguales7); f.write("\n\n7gramas repetidos: "); f.write(str(iguales7))
    print("\n\n8gramas repetidos: ", iguales8); f.write("\n\n8gramas repetidos: "); f.write(str(iguales8))


    distanciasTrigramas = calcularDistancias(iguales3)
    distanciasTetragramas = calcularDistancias(iguales4)
    distancias5gramas = calcularDistancias(iguales5)
    distancias6gramas = calcularDistancias(iguales6)
    distancias7gramas = calcularDistancias(iguales7)
    distancias8gramas = calcularDistancias(iguales8)

    print("\n\nDistancia entre trigramas repetidos: ", distanciasTrigramas); f.write("\n\n\nDistancia entre trigramas repetidos: "); f.write(str(distanciasTrigramas))
    print("\n\nDistancia entre tetragramas repetidos: ", distanciasTetragramas); f.write("\n\nDistancia entre tetragramas repetidos: "); f.write(str(distanciasTetragramas))
    print("\n\nDistancia entre 5gramas repetidos: ", distancias5gramas); f.write("\n\nDistancia entre 5gramas repetidos: "); f.write(str(distancias5gramas))
    print("\n\nDistancia entre 6gramas repetidos: ", distancias6gramas); f.write("\n\nDistancia entre 6gramas repetidos: "); f.write(str(distancias6gramas))
    print("\n\nDistancia entre 7gramas repetidos: ", distancias7gramas); f.write("\n\nDistancia entre 7gramas repetidos: "); f.write(str(distancias7gramas))
    print("\n\nDistancia entre 8gramas repetidos: ", distancias8gramas); f.write("\n\nDistancia entre 8gramas repetidos: "); f.write(str(distancias8gramas))


    mcdTrigramas = calcularMcd(distanciasTrigramas)
    mcdTetragramas = calcularMcd(distanciasTetragramas)
    mcd5gramas = calcularMcd(distancias5gramas)
    mcd6gramas = calcularMcd(distancias6gramas)
    mcd7gramas = calcularMcd(distancias7gramas)
    mcd8gramas = calcularMcd(distancias8gramas)

    print("\n\nMCD entre trigramas repetidos: ", mcdTrigramas); f.write("\n\n\nMCD entre trigramas repetidos: "); f.write(str(mcdTrigramas))
    print("\n\nMCD entre tetragramas repetidos: ", mcdTetragramas); f.write("\n\nMCD entre tetragramas repetidos: "); f.write(str(mcdTetragramas))
    print("\n\nMCD entre 5gramas repetidos: ", mcd5gramas); f.write("\n\nMCD entre 5gramas repetidos: "); f.write(str(mcd5gramas))
    print("\n\nMCD entre 6gramas repetidos: ", mcd6gramas); f.write("\n\nMCD entre 6gramas repetidos: "); f.write(str(mcd6gramas))
    print("\n\nMCD entre 7gramas repetidos: ", mcd7gramas); f.write("\n\nMCD entre 7gramas repetidos: "); f.write(str(mcd7gramas))
    print("\n\nMCD entre 8gramas repetidos: ", mcd8gramas); f.write("\n\nMCD entre 8gramas repetidos: "); f.write(str(mcd8gramas))


    f.close()
    print("\n\nTRIGRAMAS: \n")
    divisionSubcritogramas(mcdTrigramas, cadena)
    print("\n\nTETRAGRAMAS: \n")
    divisionSubcritogramas(mcdTetragramas, cadena)
    print("\n\n5GRAMAS: \n")
    divisionSubcritogramas(mcd5gramas, cadena)
    print("\n\n6GRAMAS: \n")
    divisionSubcritogramas(mcd6gramas, cadena)
    print("\n\n7GRAMAS: \n")
    divisionSubcritogramas(mcd7gramas, cadena)
    print("\n\n8GRAMAS: \n")
    divisionSubcritogramas(mcd8gramas, cadena)

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
    if lista != []:
        valor = lista[1]
        for i in range(len(lista)):
            aux = mcd(lista[i], valor)
            resultado.append(aux)
            valor = aux

        return min(resultado)
    
    return resultado


def  mcd(x, y):

    if x < y:
        return mcd(y, x)

    while y != 0:
        x, y = y, x % y

    return x


def divisionSubcritogramas(tam, cadena):
    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    f=open("analisis.txt", "a")
    subcritograma = ""
    subcritogramas = []
    aux = 0
    clave = []

    if tam != []:
        while(aux < tam): 
            for i in range(aux, len(cadena), tam):
                subcritograma = subcritograma + cadena[i]
            f.write("\n\nSubcritograma %d: "%(aux+1)); f.write(subcritograma)
            aux = aux + 1
            clave.append(abc[calculo(analisisFrecuencias(subcritograma))])
            subcritograma = ""
            #print(clave)
            print("----------------------------------------------------------------------------")

        f.close()


def analisisFrecuencias(subcritograma):
    f=open("analisis.txt", "a")
    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    frecuencias = []
    resultado = []

    for i in range(len(abc)):
        frecuencias.append((abc[i], subcritograma.count(abc[i])))

    f.write("\n\nFrecuencias: "); f.write(str(frecuencias))
    f.close()

    for i in range(len(frecuencias)):
        resultado.append(frecuencias[i][1])

    return resultado


def calculo(frecuencias):
    a = e = o = s = clave = 0
    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(len(frecuencias)):
        if frecuencias[i] >= 4:
            if frecuencias[(i+4) % 27] >= 4:
                if frecuencias[(i+4+11) % 27] >= 3:
                    if frecuencias[(i+4+11+4) % 27] >= 3:
                        a = frecuencias[i]
                        e = frecuencias[(i+4) % 27]
                        o = frecuencias[(i+4+11) % 27]
                        s = frecuencias[(i+4+11+4) % 27]
                        clave = i
                        print("\nCLAVE: ", abc[clave])
                        i = i +1
                    elif frecuencias[(i+4+11+4) % 27] == 1:
                        a = frecuencias[i]
                        e = frecuencias[(i+4) % 27]
                        o = frecuencias[(i+4+11) % 27]
                        s = frecuencias[(i+4+11+4) % 27]
                        clave = i
                        print("\nCLAVE: ", abc[clave])
                        i = i +1
                          
    return clave


comprobar(cadena)