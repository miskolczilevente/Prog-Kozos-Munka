def beolvas(nevek, jegyek, elegedettsegek, fn):
    fr = open(fn , "r")
    sor = fr.readline()
    while sor != "":
        sor = sor.split()
        nev = sor[0].strip()
        jegy = int(sor[1])
        elegedettseg = float(sor[2])
        nevek.append(nev)
        jegyek.append(jegy)
        elegedettsegek.append(elegedettseg)
        sor = fr.readline()
    #print(jegyek)
    fr.close()


def jegyszamolas(jegyek):
    f = len(jegyek)
    z = 0
    for i in range(f):
        if jegyek[i] == 5:
            z += 1
    print(z,"darab ötös van")
    return z


def osszesjegy(jegyek):
    f = len(jegyek)
    db = 0
    for i in range(f):
        db += jegyek[i]
    print(db,"az összes jegy összege")
    return db


def legalacsonyabb(elegedettsegek):
    kivalogat = []
    f = len(elegedettsegek)
    for i in range(f):
        if elegedettsegek[i] <= 5:
            kivalogat.append(elegedettsegek[i])
    print("Az 5 alatti elégedetségek ezek:",end=" ")
    for i in range(len(kivalogat)):
        print(kivalogat[i], end=" ")
    print("")
    return kivalogat

def kereses(nevek, jegyek):
    x = int(input("Ki kapott elsőnek ilyen jegyet: "))
    n = len(jegyek)
    i = 0
    while i < n and not(x == jegyek[i]):
        i += 1
    if i < n:
        print("Elsőnek", nevek[i], "kapott ilyen jegyet, ami=",x)


def maxi(nevek, elegedettsegek):
    maxim = 0
    for i in range(1, len(elegedettsegek)):
        if elegedettsegek[i] > elegedettsegek[maxim]:
            maxim = i   
    print(nevek[maxim], elegedettsegek[maxim])

def megszamolas(nevek:list,u):
    l = 0
    for i in range(len(nevek)):
        if nevek[i] == u:
            l += 1
     
    print(u, "nevu embernek", l, "darab jegye van")

def main():
    fn = input("Adatfajl: ")
    lista = []
    nevek = []
    jegyek = []
    nevek2 = ["Lilla", "Gina", "Soma", "Szavanna", "Viktor", "Levente", "Ferenc", "Csaba", "Delfina", "Dominik", "Zsombor", "Izaura", "Zsolt", "Norbert", "Fanni", "Dominika", "Luca", "Patrik", "Eszter", "Attila", "Anna", "Klaudia", "Krisztina", "Bence", "Csenge", "Kevin", "Martin"]
    elegedettsegek = []
    beolvas(nevek,jegyek,elegedettsegek, fn)
    jegyszamolas(jegyek)
    osszesjegy(jegyek)
    legalacsonyabb(elegedettsegek)
    kereses(nevek, jegyek)
    maxi(nevek, elegedettsegek)
    u = input("egy nevet kérek a listából:")
    megszamolas(nevek,u)
    
main()