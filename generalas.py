from random import randint
from random import random


def randombetu():
    r = randint(65,90)
    return chr(r)

    


def general(autonevek):
    betulista = []
    rauto = []
    szamlista = []
    rendszamok = []
    evjaratok = []
    ertekelesek = []
    for i in range(0, 500):
        betulista = []
        szamlista = []
        r = randint(0,len(autonevek)-1)
        rauto.append(autonevek[r])
        for i in range(3):
            betu = randombetu()
            betulista.append(betu)
        for i in range(3):
            r = randint(0,9)
            szamlista.append(r)
        x = (str(betulista[0]) + str(betulista[1]) + str(betulista[2]) + "-" + str(szamlista[0]) + str(szamlista[1]) + str(szamlista[2]))
        rendszamok.append(x)
        r = randint(2000, 2023)
        evjarat = r
        evjaratok.append(evjarat)
        r = randint(0,100) / 10
        ertekelesek.append(r)
    

    print(rauto)
    print(rendszamok)
    print(evjaratok)
    print(ertekelesek)
    return rauto , rendszamok , evjaratok , ertekelesek
        
def kiiratas(rauto , rendszamok , evjaratok , ertekelesek):
    fw = open("adatok.txt", "w")
    for i in range(0, 500):
        fw.write(str(rauto[i])+ " " + str(rendszamok[i]) + " " + str(evjaratok[i]) + " " + str(ertekelesek[i]) + "\n")
    fw.close()



def main():
    autonevek = ["Tesla", "Cadillac", "Dodge", "Lexus", "Porsche", "Nissan", "Ford", "Audi", "Mercedes", "Volkswagen", "Mitsubishi" ]
    rauto , rendszamok , evjaratok , ertekelesek = general(autonevek)
    kiiratas(rauto , rendszamok , evjaratok , ertekelesek)
    




main()