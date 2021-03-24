#cadena = "hacetreintamillonesdeañoscayounmeteoritodedoskilometrosdediametroenlassabanasdelvichadaunaregionalorientedecolombiaelimpactogenerounenormecraterenelquepocoapocofuecreciendounaselvaquehoyendaaeselhogardenoventafamiliasindigenasdelatribuseminomadasikuaniyalbergaalmenosmilquinientasespeciesdeanimalesycercademilcienespeciesdeplantassegúnestudiosdelinstitutohumboldtelcentrodeinvestigacionenbiodiversidadyecosistemasmasimportantedelcolombialuissantiagocastillobiologodelinstitutoyliderdelproyectoquebuscaestudiaryprotegerlaculturaylanaturalezadelazonacuentaportelefonoqueelantiguoagujerocausadoporuncuerpocelestemidecincuentakilometrosdediametroycombinalafaunaylafloradelassabanasconlasespeciesylavegetaciondelosbosquestropicalesdelamazonaslaselvadealiwacomolallamanlosindigenascontienebiodiversidadtipicadelosdosecosistemasestecratereslabisagraentreelllanoylaselvadicecastillo"

cadena = "PBVRQVICADSKAÑSDETSJPSIEDBGGMPSLRPWRÑPWYEDSDEÑDRDPCRCPQMNPWKUBZVSFNVRDMTIPWUEQVVCBOVNUEDIFQLONMWNUVRSEIKAZYEACEYEDSETFPHLBHGUÑESOMEHLBXVAEEPUÑELISEVEFWHUNMCLPQPMBRRNBPVIÑMTIBVVEÑIDANSJAMTJOKMDODSELPWIUFOZMQMVNFOHASESRJWRSFQCOTWVMBJGRPWVSUEXINQRSJEUEMGGRBDGNNILAGSJIDSVSUEEINTGRUEETFGGMPORDFOGTSSTOSEQOÑTGRRYVLPWJIFWXOTGGRPQRRJSKETXRNBLZETGGNEMUOTXJATORVJHRSFHVNUEJIBCHASEHEUEUOTIEFFGYATGGMPIKTBWUEÑENIEEU"


def comprobar(cadena):

    f=open("fichero.txt","w")
    j = 3
    num = 0
    long3, long4, long5, long6, long7, long8, long9, iguales3, iguales3, iguales3, iguales3, iguales3, iguales3, iguales3  = ([] for i in range(14))
    while(num <= 2):
        for i in range(len(cadena)):
            
            if (num == 0):
                f.write(cadena[i:i+j])
                f.write("\n")
                long3.append(cadena[i:i+j])

            elif (num == 1):
                f.write(cadena[i:i+j+num])
                f.write("\n")
                long4.append(cadena[i:i+j+num])

                
        f.write("\n\n")
        num = num + 1

    print("\n\n", long3)
    print("\n\n", long4)


    iguales3 = iguales(long3, cadena, 3)
    iguales4 = iguales(long4, cadena, 4)

    f.write(str(iguales3))
    f.write("\n\n\n")
    f.write(str(iguales4))
    f.write("\n\n\n")


    calcularMcd(iguales3)
    calcularMcd(iguales4)

    f.write(str(calcularMcd(iguales3)))
    f.write("\n\n\n")
    f.write(str(calcularMcd(iguales4)))
    f.write("\n\n\n")

         
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
    
    print("\n\n", val,"\n\n")
    return val


def calcularMcd(cadenas):

    auxCadena = cadenas[0][0]
    auxEspacio = cadenas[0][1]

    mcd = []

    for i in range(1, len(cadenas)):
        if (cadenas[i][0] == auxCadena):
            mcd.append(cadenas[i][1] - auxEspacio)
        auxCadena = cadenas[i][0]
        auxEspacio = cadenas[i][1]

    print(mcd)

    return mcd


comprobar(cadena)