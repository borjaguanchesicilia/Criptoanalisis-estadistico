import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil

#cadena = "hacetreintamillonesdeañoscayounmeteoritodedoskilometrosdediametroenlassabanasdelvichadaunaregionalorientedecolombiaelimpactogenerounenormecraterenelquepocoapocofuecreciendounaselvaquehoyendaaeselhogardenoventafamiliasindigenasdelatribuseminomadasikuaniyalbergaalmenosmilquinientasespeciesdeanimalesycercademilcienespeciesdeplantassegunestudiosdelinstitutohumboldtelcentrodeinvestigacionenbiodiversidadyecosistemasmasimportantedelcolombialuissantiagocastillobiologodelinstitutoyliderdelproyectoquebuscaestudiaryprotegerlaculturaylanaturalezadelazonacuentaportelefonoqueelantiguoagujerocausadoporuncuerpocelestemidecincuentakilometrosdediametroycombinalafaunaylafloradelassabanasconlasespeciesylavegetaciondelosbosquestropicalesdelamazonaslaselvadealiwacomolallamanlosindigenascontienebiodiversidadtipicadelosdosecosistemasestecratereslabisagraentreelllanoylaselvadicecastillo"

# ABER
#cadena = "PBVRQVICADSKAÑSDETSJPSIEDBGGMPSLRPWRÑPWYEDSDEÑDRDPCRCPQMNPWKUBZVSFNVRDMTIPWUEQVVCBOVNUEDIFQLONMWNUVRSEIKAZYEACEYEDSETFPHLBHGUÑESOMEHLBXVAEEPUÑELISEVEFWHUNMCLPQPMBRRNBPVIÑMTIBVVEÑIDANSJAMTJOKMDODSELPWIUFOZMQMVNFOHASESRJWRSFQCOTWVMBJGRPWVSUEXINQRSJEUEMGGRBDGNNILAGSJIDSVSUEEINTGRUEETFGGMPORDFOGTSSTOSEQOÑTGRRYVLPWJIFWXOTGGRPQRRJSKETXRNBLZETGGNEMUOTXJATORVJHRSFHVNUEJIBCHASEHEUEUOTIEFFGYATGGMPIKTBWUEÑENIEEU"

# ARTIFICIAL
cadena = "HRVMYZGPNEADBSPWOMSÑERHWXKCGOFNDXBJWTPTZDVWWXRKSOWELLWXLGLILMVNZTMOSADSRUIRIULEVVZVOFLCCNLRVZPTUCSOCIVGBJLGKOVODUPFMNPMAATNWLMOMRZUEXUTZÑMCCALXZJUGSQFEHIKTIRWCZFMXKWMEPEXDGÑUFAGSVLQMXOTGGUDLAVMMPOQÑACDVGWAMOBAPADBSNIUPNÑIXXUFAFMLLTJBJZAGTIXODTLFAKRULNZRIPJGZGLACFMRWUTIVQMBUNMOBADEKJMHPGADOAEBTFSGAYNEJVIIMÑPLNIVGMXXGKIOSUXXPIOBADSVZCRMUBUÑIGMLJSKUSEILÑBTOWTBZLUNMPKGUTCOUXPRDGATSGRVPTUGUBSOUBDJZUPDLDPXKTAKATOMRMTFAKTPZRLTUYMFMLNOCITGPCSUSSKTUYPCÑONAKNPPSQJIZLGZWIMNPNDTZNCYWASIÑEJWMPXTWYOCLIYZMDCSNAVMBZLKIRJPJIBJÑGZLLCMEBZZCGLLNRNCWINMZLDVEIEWOICFEENIUWTBEVEWIUTYWMEVAENPLCQIGFJVLWHIWAAÑOHIZZUECECPGVMPMUBEWIUXKNUECEXTRDPPWÑMTCOKWMIPCTEERGRKTTDPNLLRYIZUCGLLFCIZFLGSADSRUIRIUKOXLRMMXXGKIOSPEIAMIMTLCZIUIMNWSMOKKCJAVZOAITTSJAFMLLMRSWRIUSADECOIIMCSIHATITTSCSLLMRGSTAKUDSGVGIXKQUTSEEXJNWFPVORKBLFLVPPSCRWMPWULODETIANAVMMLSVMBJKTITORVMSFJKAAQRRXUYZGMLVLRGWDSCAEVVRWPHMEISEICEW"

# CIFRAR
#cadena = "UOFENQUJKRGKTEOEPIGPQZMRBGZKMNFIIGENKFDPQLJCAVMTJICLJCAKUKGRÑIHZOOTNVNVZFKRGIPZZCJFKUÑIJKTTPFVNGSQRSUIHYUUMYLSKUXLIVCYVOHBJTHOWPGGALJDOUBWGCQUXMTGANKQWMPRSCXPZCCKNGNGAJCEEBWGNKKFKDGIPXEDZFSOQSJRNCXTURKIRTOOAYJUKZHMANYZZETZJCAEPTELQÑNTOOCQVRKKFTOOBWZBWGTRSKTNKMQIPTAÑXTUENKWZPVWFEANPXZSRIWRLCLJWEOAFUEGAYRDQAZEIFWXUUTIRLENIXVGWUIRGWMWJAÑCRUICSHGNVZFSALWXKODZJVLFMXTIHZFUOFMHGDKÑTKYNIXVGWZNUAFMRCAUBJCEEWQMNKKFTIQUJK"

# GLOBALMENTE
#cadena = "NLQFTCPMZNERSZMOXPWPXETZHDAJAYZFIZODSIEAHQWSYUWMOWPXEIWJORJAWPXEIISVOTSLNEZTWJOZWINSEPTYSLGFGSAQNESXSSÑTOOIOIOUWPJAOWMYJEIEDHEXPVBÑQKXDSMOÑVNNIXOBFLBGICIGULEPCZQYQVVKNWFNÑAYZTWKVKBQFPLBRISÑOBEDPOTIKGCRFNZHIZNELLAJLSMWUGHÑQSÑADOIXTXXSPVSOXMZIPGÑOTIUGEZBCGVPFRQMEXFISZHNIVCYUGMKXIBSOETQVMKDRFAXTPNEIYJQFRNMHQFMQNWFNOETQVMKDRFPVMQGTWYOUVNOEXHWMUDRFLSYWGBXAEDIUWNSXWXKVQFNEDSPXMSGSTTSREOBSSOBCIZOMIXVYSRBDJPGBMMYESNADXEFBPVZGUAXFIPXOIZZPMMTEXÑMYDOÑTSMKBVEYEWMLZNMBESMZRFLSYWGBXAEDZLSOIEWIQAGPYOÑXBKYKMJTCLPWGÑHÑLGZPCAXQZIXVODUVFYETCQLBBTFDEXXDGÑSMAKAQNVYKXIBPZDXQEILZBPQFPIXTQZSUVOLRYVXVUNOVSLOSCIVAXQVECBSOXOKDIFMSOIOBQIFSÑTLVMXIPKEGPSÑPHUTPKEGPYNAPÑBQGVOGAFYELEELVDSAÑPONMWGMOÑADÑSZEEYOHQENTIFROGGSHEEMGUIQJOZPSMAWDÑIYEGPPSÑEXXWJOZBMLLSZTWQLHFLGMHQTOÑHODOWAONEOGWOÑLZEMZWMMOBBSNAQGBISOPJOÑTZQLWÑÑOETSBMOTHKVDTDZEIOIWÑDIFMLEIFNIICOUECPWXTFÑDOHRLPQGLIKVZMAXACXTWKVKBDSÑIOTWZSZMO"

# POCHITO
#cadena = "WOELBLSXBVHTBZADOLAWSPCQZKTNEJOSMNSEGKAWWSSDUQPEDBSVYWMRTRKHTXIHDGTSTHIODHUTHSSNCPVVPRCBUTGTUKVUTZEGKLUNSSSEVSIAQWCLSBAFOEAWZSCSTVCGSCDTSMVGPIGYMGSAFWLXIQEORVKITKSEYMVWTBFVCGOISNCIKJTVQFMGRPOGZMEVEUCYLXBEKGTBTTPAKRPTHXBFOÑXBPHFLSTIHWDBAXAXBQSIWOIWMBIGWÑONIMLUPONSMGDIAKRYÑWCWGTBTHTHRLKBSIRGHUBAPZGZGVSHQCKMFWAQKLUXHFSEOMMRTENHUNOIHGNCGSIIWKPIHSSNOUMIXIWAWAJBPQRLNSAQGTBLDSSKTDXHJWIHKBDCSOIPIRXKGYABRPRALKIHXHVLTTHBOUOTJDHICTBXRTZEVSIAQWCRCBHIOOAPTUEQCZBBZADDOWEDVDFLSBBIIKACNDÑZKKMLRTZRYWRSRIQXCXPKHEHMMIKRKHZREHDVLÑXGAOEBSNJHOARIGOJJTHSXÑPRGRISDCOEBMGIPEQYBXZTTQTWKJTSNHUNWVJQHÑÑXTGQJIÑHPRQWWLJCQWLZJDRSNLANSBWFLKBBRJGTBTYXZQSMNGEHFLLBOBSVYWRQEADOUTZPTCBUTNAOHRWLOSSNHAMOQOOHAVDCZCZMMETQKLARZPKGNMNORWQTLXZEHDVAKJTHVYWJWRONLAWSAOÑHHIBPHNHAXZLOFLIEWMOEVTIZPZNHTTBADUOUWWVSOHAVDCIKLUXPXDFODXGIWFHLNWFWEHLXZEHFVAXQEHKZBXAPHGZBXQHOVLZXHAODOATUHOGTBLSTZNRIGDÑZCZMEKPRKJMVOIIKRSI"


def comprobar(cadena):

    f=open("analisis.txt","w")
    shutil.rmtree("./diagramasDeFrecuencias", ignore_errors=True)
    os.mkdir("diagramasDeFrecuencias")
    j = 3
    num = 0
    carpeta = 0
    long3, long4, mcd3, mcd4, long5, long6, long7, long8, mcd5, mcd6, mcd7, mcd8 = ([] for i in range(12))
    mcdTrigramas = mcdTetragramas = mcdPentagramas = mcdHexagramas = mcdHeptagramas = mcdOctogramas = 0
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

    f.write("Trigramas: "); f.write(str(long3))
    f.write("\n\nTetragramas: "); f.write(str(long4))
    f.write("\n\nPentagramas: "); f.write(str(long5))
    f.write("\n\nHexagramas: "); f.write(str(long6))
    f.write("\n\nHeptagramas: "); f.write(str(long7))
    f.write("\n\nOctogramas: "); f.write(str(long8))



    iguales3 = iguales(long3, cadena, 3)
    iguales4 = iguales(long4, cadena, 4)
    iguales5 = iguales(long5, cadena, 5)
    iguales6 = iguales(long6, cadena, 6)
    iguales7 = iguales(long7, cadena, 7)
    iguales8 = iguales(long8, cadena, 8)

    f.write("\n\n\nTrigramas repetidos: "); f.write(str(iguales3))
    f.write("\n\nTetragramas repetidos: "); f.write(str(iguales4))
    f.write("\n\nPentagramas repetidos: "); f.write(str(iguales5))
    f.write("\n\nHexagramas repetidos: "); f.write(str(iguales6))
    f.write("\n\nHeptagramas repetidos: "); f.write(str(iguales7))
    f.write("\n\nOctogramas repetidos: "); f.write(str(iguales8))


    distanciasTrigramas = calcularDistancias(iguales3)
    distanciasTetragramas = calcularDistancias(iguales4)
    distanciasPentagramas = calcularDistancias(iguales5)
    distanciasHexagramas = calcularDistancias(iguales6)
    distanciasHeptagramas = calcularDistancias(iguales7)
    distanciasOctogramas = calcularDistancias(iguales8)

    f.write("\n\n\nDistancia entre trigramas repetidos: "); f.write(str(distanciasTrigramas))
    f.write("\n\nDistancia entre tetragramas repetidos: "); f.write(str(distanciasTetragramas))
    f.write("\n\nDistancia entre Pentagramas repetidos: "); f.write(str(distanciasPentagramas))
    f.write("\n\nDistancia entre Hexagramas repetidos: "); f.write(str(distanciasHexagramas))
    f.write("\n\nDistancia entre Heptagramas repetidos: "); f.write(str(distanciasHeptagramas))
    f.write("\n\nDistancia entre Octogramas repetidos: "); f.write(str(distanciasOctogramas))


    mcdTrigramas = calcularMcd(distanciasTrigramas)
    mcdTetragramas = calcularMcd(distanciasTetragramas)
    mcdPentagramas = calcularMcd(distanciasPentagramas)
    mcdHexagramas = calcularMcd(distanciasHexagramas)
    mcdHeptagramas = calcularMcd(distanciasHeptagramas)
    mcdOctogramas = calcularMcd(distanciasOctogramas)


    f.write("\n\n\nMCD entre trigramas repetidos: "); f.write(str(mcdTrigramas))
    f.write("\n\nMCD entre tetragramas repetidos: "); f.write(str(mcdTetragramas))
    f.write("\n\nMCD entre Pentagramas repetidos: "); f.write(str(mcdPentagramas))
    f.write("\n\nMCD entre Hexagramas repetidos: "); f.write(str(mcdHexagramas))
    f.write("\n\nMCD entre Heptagramas repetidos: "); f.write(str(mcdHeptagramas))
    f.write("\n\nMCD entre Octogramas repetidos: "); f.write(str(mcdOctogramas))


    print("\n\nPor Trigramas: \n")
    carpeta = divisionSubcritogramas(mcdTrigramas, cadena, carpeta)


    print("\n\nPor tetragramas: \n")
    carpeta = divisionSubcritogramas(mcdTetragramas, cadena, carpeta)
 

    print("\n\nPor Pentagramas: \n")
    carpeta = divisionSubcritogramas(mcdPentagramas, cadena, carpeta)


    print("\n\nPor Hexagramas: \n")
    carpeta = divisionSubcritogramas(mcdHexagramas, cadena, carpeta)

    print("\n\nPor Heptagramas: \n")
    carpeta = divisionSubcritogramas(mcdHeptagramas, cadena, carpeta)

    print("\n\nPor Octogramas: \n")
    carpeta = divisionSubcritogramas(mcdOctogramas, cadena, carpeta)

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


def divisionSubcritogramas(tam, cadena, carpeta):
    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    f=open("analisis.txt", "a")
    subcritograma = ""
    subcritogramas = []
    aux = 0
    clave = []

    f.write("\n----------------------------------------------------------------------------------");
    if tam != 0 and tam != 1:
        carpeta = carpeta + 1
        path = "./diagramasDeFrecuencias/subcritogramas" + str(carpeta)
        os.mkdir(path);
        while(aux < tam): 
            for i in range(aux, len(cadena), tam):
                subcritograma = subcritograma + cadena[i]
            stringSubcritograma = "Subcritograma " + str(aux+1)
            f.write("\n\n" + stringSubcritograma); f.write(subcritograma)
            aux = aux + 1
            clave.append(calculo(analisisFrecuencias(subcritograma, stringSubcritograma, path)))
            subcritograma = ""

    f.close()
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


def analisisFrecuencias(subcritograma, fichero, path):
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

    
    diagramaDeFrecuencias(resultado, fichero, path)

    return resultado


def calculo(frecuencias):
    clave = []
    for i in range(len(frecuencias)):
        if frecuencias[i] >= 4:
            if frecuencias[(i+4) % 27] >= 4:
                if frecuencias[(i+4+11) % 27] >= 3:
                    if frecuencias[(i+4+11+4) % 27] >= 1:
                        clave.append(i)
                        i = i + 1
                    elif frecuencias[(i+4+11+4) % 27] == 1:
                        clave.append(i)
                        i = i + 1                         
    return clave


def diagramaDeFrecuencias(frecuencias, fichero, path):
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
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')


    autolabel(rects1)

    fig.tight_layout()

    salida = path + "/" + fichero + ".png"
    fig.savefig(salida)
    plt.cla()
    plt.close()


comprobar(cadena)