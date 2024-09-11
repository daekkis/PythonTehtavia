# Tee ohjelma, joka kysyy käyttäjältä kaksi lukua ja tulostaa niistä suuremman. Jos luvut ovat yhtä suuret, ohjelma huomaa myös tämän. 

Luku1 = float(input("Anna luku: "))
Luku2 = float(input("Anna toinen luku: "))

if Luku1 > Luku2:
    print("Suurempi luku:", Luku1)
elif Luku1 < Luku2:
    print("Suurempi luku:", Luku2)
else:
     print("Luvut ovat yhtä suuret")
