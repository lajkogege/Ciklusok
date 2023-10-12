#Eljárásaink tesztelésére hoztuk létre
import eljarasok

#1.teszteset
print("1. teszteset: Pozitiv számok")
eljarasok.hanyados(3,5)

#2.teszteset
print("1. teszteset: Negatív számok")
eljarasok.hanyados(-5,-2)

#3.teszteset
print("3. teszteset: Tört számok - nem jó teszteset, mert egész számot tud csak kezelni")
#eljarasok.hanyados(-5.2,-2.2)

#4.teszteset
print("4. teszteset: Nincs paraméter")
eljarasok.hanyados()#Adtunk alapértelmezett értéket

#5.teszteset
print("5. teszteset: A számláló 0, a=0")
eljarasok.hanyados(-5,0)

#6.teszteset
print("6. teszteset: A nevező 0, b=0")
eljarasok.hanyados(-5,0)