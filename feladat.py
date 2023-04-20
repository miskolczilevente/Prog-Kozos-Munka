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
        print ("Van ilyen evjáratú auto")
    else:
        print("Nincs ilyen evjáratú auto")

def main():
    
    autonevek = []
    rendszamok = []
    evjaratok = []
    ertekelesek = []
    kert_evjarat = int(input("Kert evjarat: "))
    beolvasas(autonevek, rendszamok, evjaratok, ertekelesek)
    # print(evjaratok)
    evjarat(evjaratok, kert_evjarat)

main()