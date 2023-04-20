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



def main():
    autonevek = []
    rendszamok = []
    evjaratok = []
    ertekelesek = []

    beolvasas(autonevek, rendszamok, evjaratok, ertekelesek)
    print(autonevek)

main()