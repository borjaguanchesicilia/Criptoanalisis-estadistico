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
    

    iguales3 = iguales(long3)
    iguales4 = iguales(long4)
    iguales5 = iguales(long5)
    iguales6 = iguales(long6)
    iguales7 = iguales(long7)
    iguales8 = iguales(long8)
    iguales9 = iguales(long9)
    
    print("\n\n", iguales3)
    print("\n\n", iguales4)
    print("\n\n", iguales5)
    print("\n\n", iguales6)
    print("\n\n", iguales7)
    print("\n\n", iguales8)
    print("\n\n", iguales9)
        
    f.close()

def iguales(cadenas):
    
    iguales = []
    for i in range(len(cadenas)):
        for j in range(len(cadenas)):
            if (cadenas[i] == cadenas[j]) and (i != j):
                print(cadenas[i], i, " --> ", cadenas[j], j)
                if (j-i > 0):
                    iguales.append((cadenas[j], j-i))
                    break

    return iguales

comprobar(cadena)