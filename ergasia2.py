import string
import random

sun_vimata = []

for j in range(100):

    kapakia = []
    for i in range(9):
        kapakia.append("mik") #9 mikra kapakia
        kapakia.append("mes") #9 mesaia kapakia
        kapakia.append("meg") #9 megala kapakia

    nikhths = False
    vimata = 0
    tetragwno = []
    for k in range(9):  #decleration tou tetragwnou 3x3 dhladh ths listas 9 thesewn pou h kathe mia thesh exei alles 3 gia ta mik,mes,meg
        tetragwno.append([])
        for l in range(3):              #sto 0 ta mikra, sto 1 ta mesaia, sto 2 ta megala
            tetragwno[k].append(l)
    koutakia = 0                   #h deuterh sunthikh den tha ginei pote False    
    while nikhths == False and len(kapakia) > 0 :
            if koutakia == 9:
                koutakia = 0
            x = kapakia.pop(random.randrange(len(kapakia)))    #x einai ena tuxaio kapaki

            if x == "mik":
                    for i in range(koutakia,9):        #psaxnei ta 9 koutakia mexri na vrei ena adeio gia to megethos tou x
                        if tetragwno[i][0] == 0 and tetragwno[i][1] == 1 and tetragwno[i][2] == 2:   #gia na bei ena mikro prepei na mhn uparxei megalutero
                            tetragwno[i].pop(0)
                            tetragwno[i].insert(0,x)
                            vimata+=1
                            koutakia = i + 1
                            break

                    #3ada mikrwn peiptwseis
                    if tetragwno[0][0] == tetragwno[1][0] == tetragwno[2][0] == "mik":
                        nikhths = True

                    if tetragwno[3][0] == tetragwno[4][0] == tetragwno[5][0] == "mik":
                        nikhths = True

                    if tetragwno[0][0] == tetragwno[3][0] == tetragwno[6][0] == "mik" or tetragwno[2][0] == tetragwno[4][0] == tetragwno[6][0] == "mik":
                        nikhths = True

                    if tetragwno[1][0] == tetragwno[4][0] == tetragwno[7][0] == "mik":
                        nikhths = True

                    if tetragwno[2][0] == tetragwno[5][0] == tetragwno[8][0] == "mik" or tetragwno[0][0] == tetragwno[4][0] == tetragwno[8][0] == "mik" or tetragwno[6][0] == tetragwno[7][0] == tetragwno[8][0] == "mik":
                        nikhths = True

            elif x == "mes":
                    for i in range(koutakia,9):
                        if tetragwno[i][1] == 1  and tetragwno[i][2] == 2:   #gia na bei ena messaio prepei na mhn uparxei megalo:
                            tetragwno[i].pop(1)
                            tetragwno[i].insert(1,x)
                            vimata+=1
                            koutakia = i + 1
                            break

                    #3ada mesaiwn peiptwseis
                    if tetragwno[0][1] == tetragwno[1][1] == tetragwno[2][1] == "mes":
                        nikhths = True

                    if tetragwno[3][1] == tetragwno[4][1] == tetragwno[5][1] == "mes":
                        nikhths = True

                    if tetragwno[0][1] == tetragwno[3][1] == tetragwno[6][1] == "mes" or tetragwno[2][1] == tetragwno[4][1] == tetragwno[6][1] == "mes":
                        nikhths = True

                    if tetragwno[1][1] == tetragwno[4][1] == tetragwno[7][1] == "mes":
                        nikhths = True

                    if tetragwno[2][1] == tetragwno[5][1] == tetragwno[8][1] == "mes" or tetragwno[0][1] == tetragwno[4][1] == tetragwno[8][1] == "mes" or tetragwno[6][1] == tetragwno[7][1] == tetragwno[8][1] == "mes":
                        nikhths = True

            else:
                    for i in range(koutakia,9):
                        if tetragwno[i][2] == 2:   #gia na bei ena megalo prepei apla na einai adeio to koutaki sthn thesh tou megalou
                            tetragwno[i].pop(2)
                            tetragwno[i].insert(2,x)
                            vimata+=1
                            koutakia = i + 1
                            break

                    #3ada megalwn peiptwseis
                    if tetragwno[0][2] == tetragwno[1][2] == tetragwno[2][2] == "meg":
                        nikhths = True

                    if tetragwno[3][2] == tetragwno[4][2] == tetragwno[5][2] == "meg":
                        nikhths = True

                    if tetragwno[0][2] == tetragwno[3][2] == tetragwno[6][2] == "meg" or tetragwno[2][2] == tetragwno[4][2] == tetragwno[6][2] == "meg":
                        nikhths = True

                    if tetragwno[1][2] == tetragwno[4][2] == tetragwno[7][2] == "meg":
                        nikhths = True

                    if tetragwno[2][2] == tetragwno[5][2] == tetragwno[8][2] == "meg" or tetragwno[0][2] == tetragwno[4][2] == tetragwno[8][2] == "meg" or tetragwno[6][2] == tetragwno[7][2] == tetragwno[8][2] == "meg":
                        nikhths = True

            #apo to mikrotero sto megalutero periptwseis:
            if tetragwno[0][0] == "mik" and tetragwno[1][1] == "mes" and tetragwno[2][2] == "meg" :
                nikhths = True
            elif tetragwno[3][0] == "mik" and tetragwno[4][1] == "mes" and tetragwno[5][2] == "meg":
                nikhths = True
            elif tetragwno[6][0] == "mik" and tetragwno[7][1] == "mes" and tetragwno[8][2] == "meg":
                nikhths = True
            elif tetragwno[0][0] == "mik" and tetragwno[3][1] == "mes" and tetragwno[6][2] == "meg":
                nikhths = True
            elif tetragwno[1][0] == "mik" and tetragwno[4][1] == "mes" and tetragwno[7][2] == "meg":
                nikhths = True
            elif tetragwno[2][0] == "mik" and tetragwno[5][1] == "mes" and tetragwno[8][2] == "meg":
                nikhths = True
            elif tetragwno[0][0] == "mik" and tetragwno[4][1] == "mes" and tetragwno[8][2] == "meg":
                nikhths = True
            elif tetragwno[2][0] == "mik" and tetragwno[4][1] == "mes" and tetragwno[6][2] == "meg":
                nikhths = True

    if nikhths:
        sun_vimata.append(vimata)

MO = sum(sun_vimata) / 100
print("O mesos oros vimatwn twn 100 paixnidiwn gia na liksei to kathe ena einai: " + str(MO))
