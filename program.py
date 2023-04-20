def beolvasas(au, re, ev, er):
    fr = open("adatok.txt", "r")
    sor = fr.readline()
    while sor != "":
        sor = sor.strip().split()
        au.append(sor[0])
        re.append(sor[1])
        ev.append(int(sor[2]))
        er.append(float(sor[3]))
        sor = fr.readline()

    fr.close()

def evjarat(evj, keev):
    i = 0
    while not(evj[i] == keev):
        i += 1
    if i <= len(evj):
        print (f"Van {keev} évjáratú auto")
    else:
        print(f"Nincs {keev} évjáratú auto")

def nyolcfeletti(re, er):
    i = 0
    while not(er[i] > 8):
        i += 1
    if i < len(er):
        print(f"Az első 8.0 fölöttire értekelt autó rendszama: {re[i]}") 
    else:
        print("Nincs 8.0 fölöttire értékelt autó!")


def main():
    
    autonevek = []
    rendszamok = []
    evjaratok = []
    ertekelesek = []
    kert_evjarat = int(input("Kert evjarat: "))
    beolvasas(autonevek, rendszamok, evjaratok, ertekelesek)
    # print(evjaratok)
    evjarat(evjaratok, kert_evjarat)
    nyolcfeletti(rendszamok, ertekelesek)
main()