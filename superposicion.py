#cadena = "hacetreintamillonesdeañoscayounmeteoritodedoskilometrosdediametroenlassabanasdelvichadaunaregionalorientedecolombiaelimpactogenerounenormecraterenelquepocoapocofuecreciendounaselvaquehoyendaaeselhogardenoventafamiliasindigenasdelatribuseminomadasikuaniyalbergaalmenosmilquinientasespeciesdeanimalesycercademilcienespeciesdeplantassegúnestudiosdelinstitutohumboldtelcentrodeinvestigacionenbiodiversidadyecosistemasmasimportantedelcolombialuissantiagocastillobiologodelinstitutoyliderdelproyectoquebuscaestudiaryprotegerlaculturaylanaturalezadelazonacuentaportelefonoqueelantiguoagujerocausadoporuncuerpocelestemidecincuentakilometrosdediametroycombinalafaunaylafloradelassabanasconlasespeciesylavegetaciondelosbosquestropicalesdelamazonaslaselvadealiwacomolallamanlosindigenascontienebiodiversidadtipicadelosdosecosistemasestecratereslabisagraentreelllanoylaselvadicecastillo"

cadena = "PBVRQVICADSKAÑSDETSJPSIEDBGGMPSLRPWRÑPWYEDSDEÑDRDPCRCPQMNPWKUBZVSFNVRDMTIPWUEQVVCBOVNUEDIFQLONMWNUVRSEIKAZYEACEYEDSETFPHLBHGUÑESOMEHLBXVAEEPUÑELISEVEFWHUNMCLPQPMBRRNBPVIÑMTIBVVEÑIDANSJAMTJOKMDODSELPWIUFOZMQMVNFOHASESRJWRSFQCOTWVMBJGRPWVSUEXINQRSJEUEMGGRBDGNNILAGSJIDSVSUEEINTGRUEETFGGMPORDFOGTSSTOSEQOÑTGRRYVLPWJIFWXOTGGRPQRRJSKETXRNBLZETGGNEMUOTXJATORVJHRSFHVNUEJIBCHASEHEUEUOTIEFFGYATGGMPIKTBWUEÑENIEEU"


def comprobar(cadena):

    f=open("kk.txt","w")
    j = 3
    k = 3
    num = 0
    long3, long4, long5, long6, long7, long8, long9, iguales3, iguales3, iguales3, iguales3, iguales3, iguales3, iguales3  = ([] for i in range(14))
    while(num <= 8):
        for i in range(0, len(cadena), k):
            
            if (num == 0):
                f.write(cadena[i:i+j+num])
                f.write("\n")
                long3.append(cadena[i:i+j+num])
            
            elif (num == 1):
                f.write(cadena[i:i+j+num])
                f.write("\n")
                long4.append(cadena[i:i+j+num])

            elif (num == 2):
                f.write(cadena[i:i+j+num])
                f.write("\n")
                long5.append(cadena[i:i+j+num])

            elif (num == 3):
                f.write(cadena[i:i+j+num])
                f.write("\n")
                long6.append(cadena[i:i+j+num])

            elif (num == 4):
                f.write(cadena[i:i+j+num])
                f.write("\n")
                long7.append(cadena[i:i+j+num])

            elif (num == 5):
                f.write(cadena[i:i+j+num])
                long8.append(cadena[i:i+j+num])

            elif (num == 6):
                f.write(cadena[i:i+j+num])
                f.write("\n")
                long9.append(cadena[i:i+j+num])
                
        f.write("\n\n")
        k = k + 1
        num = num + 1

    print("\n\n", long3)
    print("\n\n", long4)
    print("\n\n", long5)
    print("\n\n", long6)
    print("\n\n", long7)
    print("\n\n", long8)
    print("\n\n", long9)
    

    iguales3 = iguales(long3, cadena)
    #iguales4 = iguales(long4, cadena)

    
           
    f.close()

def iguales(cadenas, principal):
    
    iguales = []
    val = []
    flag = 1
    aux = 0
    for i in range(len(cadenas)):
        for k in range(len(val)):
            if cadenas[i] in val[k][0]:
                flag = 0
        if (flag == 1):
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
    
    print(val,"\n\n")
    return iguales

comprobar(cadena)