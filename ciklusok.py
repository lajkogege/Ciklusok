
#bizonyos műveletek ismétlésre való a ciklus
#ciklus változó, számlálja, hogy hányszor futott már le a ciklus
#ciklusmag - ismétlödő utasítások
#ciklus feltétel -itt adjuk meg, hogy mennyiszer fusson le a ckilus
def szamlalos_ciklus1():
    cv: int = 1

    while (cv < 10):
        print(f"{cv} Többé nem kések, mert lemaradok fontos informéciókról!")
        cv += 1

    print(cv, "A ckilus után")

def elotesztelos_ciklus():
    #kérjünk be egy 10-nél nagyobb számot a felhasználotól


    szam: int = int(input("Adjon meg egy 10-nél nagyobb számot: "))
    while szam <= 10:
        print("10-nél nagyobb számot!")
        szam: int = int(input("Adjon meg egy 10-nél nagyobb számot! "))
    print("Hurrá, végre sikerült 10-nél nagyobbat!", szam)

print("valami",end=",")
print("vége")
# készíts külön eljarást
#1. írd ki a számokat 1 és 10 között a képernyőre egymás mellé
#2. Írd ki a számokat 20 és 30 köztt a képernyőre
#3. Írd ki a 15 és 25 közötti páros számokat
#4. Írd ki a számokat egyesével 12 és 30 között forditott sorrendben

def ciklus1feldat():
    szam3:int=1
    while (szam3<11):
        print(f"{szam3}", end=",")
        szam3 += 1
    print("")
ciklus1feldat()

#2. Írd ki a számokat 20 és 30 köztt a képernyőre
def ciklus2feladat():
    szam4: int=20
    while  szam4<30:
        szam4 +=1
        print(f"{szam4}", end=",")

ciklus2feladat()

#3. Írd ki a 15 és 25 közötti páros számokat
def ciklus3feladat():
    szam5: int=15
    while  (szam5<=25):
        if szam5 % 2 ==0:
            print(f"{szam5}", end=",")
            szam5 += 1
ciklus3feladat()

def ciklus4feladat():
    szam6: int=30
    while  (szam6>=12):
        print(f"{szam6}", end=",")
        szam6 -= 1
ciklus4feladat()





