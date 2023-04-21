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
       

def nyolcfeletti(re, er):
    i = 0
    while i < len(er) and not(er[i] > 8):
        i += 1
    if i < len(er):
        print (f"Az első 8.0 fölöttire értekelt autó rendszama: {re[i]}") 
    else:
        print("Nincs 8.0 fölöttire értékelt autó!")

def kivalogatas(evj, nev, autolista, rendsz):
    legujabbak = []
    for i in range(len(evj)):
        if nev == autolista[i] and 2020 < evj[i]:
            legujabbak.append(rendsz[i])
    return legujabbak

def kiiratas(leg):
    print("Ezek a legujabbak a megadott markabol: ", end="")
    for i in range(len(leg)):
        print(leg[i], end=" ")

def main():
    fajlnev = input("Add meg a beolvasni kivant fajl nevet: ")
    autonevek = []
    rendszamok = []
    evjaratok = []
    ertekelesek = []
    autonev = input("Auto nev: ")
    kert_evjarat = input("Kert evjarat: ")
    beolvasas(autonevek, rendszamok, evjaratok, ertekelesek, fajlnev)
    # print(evjaratok)
    evjarat(evjaratok, kert_evjarat)
    nyolcfeletti(rendszamok, ertekelesek)
    legujabbak = kivalogatas(evjaratok, autonev, autonevek, rendszamok)
    kiiratas(legujabbak)
    
main()