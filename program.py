def beolvasas(au, re, ev, er, fn):
    fr = open(fn, "r")
    sor = fr.readline()
    while sor != "":
        sor = sor.strip().split()
        au.append(sor[0])
        re.append(sor[1])
        ev.append(int(sor[2]))
        er.append(float(sor[3]))
        sor = fr.readline()

    fr.close()


def kiiras(n):
    print(f"{n}. Feladat:")


def f1(rendszamok, ertekelesek):
    kiiras(1)
    nyolcfeletti(rendszamok, ertekelesek)
    

def f2(evjaratok, kert_evjarat):
    kiiras(2)
    evjarat(evjaratok, kert_evjarat)
    

def f3(autonevek):
    kiiras(3)
    megszamolas(autonevek)


def f4(evjaratok, autonev, autonevek, rendszamok):
    kiiras(4)
    legujabbak = kivalogatas(evjaratok, autonev, autonevek, rendszamok)
    kiiratas(legujabbak)

def f5(ertekelesek, kert_auto, autonevek):
    kiiras(5)
    atlag = minmax(ertekelesek, kert_auto, autonevek)
    print(f"{atlag} a(z) {kert_auto} legnagyobb es a legkissebb ertekelesenek atlaga")

def nyolcfeletti(re, er):
    i = 0
    while i < len(er) and not(er[i] > 8):
        i += 1
    if i < len(er):
        print(f"Az első 8.0 fölöttire értekelt autó rendszama: {re[i]}") 
    else:
        print("Nincs 8.0 fölöttire értékelt autó!")


def evjarat(evj, keev=""):
    if keev == "" or keev == "0":
        print("Nem adtál meg erteket")
    else:
        i = 0
        keev = int(keev)
        while i < len(evj) and not(evj[i] == keev):
            i += 1
        if i < len(evj):
            print(f"Van {keev} évjáratú auto")
        else:
            print(f"Nincs {keev} évjáratú auto")
       


def kivalogatas(evj, nev, autolista, rendsz):
    legujabbak = []
    for i in range(len(evj)):
        if nev == autolista[i] and 2020 < evj[i]:
            legujabbak.append(rendsz[i])
    return legujabbak


def kiiratas(leg):
    if len(leg) > 0:
        print("Ezek a legujabbak a megadott markabol: ", end="")
        for i in range(len(leg)):
            print(leg[i], end=" ")
        
        print("\n")
    else:
        print("Nincs ilyen")

def megszamolas(autonevek):
    if "Ford" in autonevek:
        darab = 0 
        for i in range(len(autonevek)):
            if autonevek[i] == "Ford":
                darab += 1
        print(f"{darab} db Ford auto van.")
    else:
        print("Nincs ilyen")

def minmax(ertekelesek,kert_auto, autonevek):
    if kert_auto in autonevek:
        maxe = 10 
        mine = 0 
        for i in range(len(autonevek)):
            if autonevek[i] == kert_auto:
                if ertekelesek[i] < maxe:
                    maxe = ertekelesek[i]

                if ertekelesek[i] > mine:
                    mine = ertekelesek[i]

        atlag = (maxe + mine) / 2
        return round(atlag, 1)
    else:
        return 0



def main():
    fajlnev = input("Add meg a beolvasni kivant fajl nevet: ")
    autonevek = []
    rendszamok = []
    evjaratok = []
    ertekelesek = []
    autonev = input("Auto nev: ")
    kert_evjarat = input("Kert evjarat: ")
    print("\n")
    beolvasas(autonevek, rendszamok, evjaratok, ertekelesek, fajlnev)
    f1(rendszamok,ertekelesek)
    print("\n")
    f2(evjaratok, kert_evjarat)
    print("\n")
    f3(autonevek)
    print("\n")
    f4(evjaratok, autonev, autonevek, rendszamok)
    print("")
    f5(ertekelesek, autonev, autonevek)

    

main()