# Tee ohjelma, joka kysyy käyttäjältä kolme lukua ja tulostaa niiden keskiarvon.

Luku1 = float(input("Anna ensimmäinen luku: "))
Luku2 = float(input("Anna toinen luku: "))
Luku3 = float(input("Anna kolmas luku: "))

Keskiarvo = (Luku1 + Luku2 + Luku3) / 3

# print(f"Lukujen {Luku1}, {Luku2} ja {Luku3} keskiarvo on {Keskiarvo:.3f}")

print(f"Lukujen {Luku1}, {Luku2} ja {Luku3} keskiarvo on {round(Keskiarvo, 3)}")




# Tai toinen tapa:

print("Anna kolme lukua (paina enter luvun syöttämisen jälkeen): ")

ekaluku = input()
tokaluku = input()
kolmasluku = input()

keskiarvo = (int(ekaluku) + int(tokaluku) + int(kolmasluku)) / 3
pyöristetty_keskiarvo = round(keskiarvo, 3)

print("Lukujen " + str(ekaluku) + " , " + str(tokaluku) + " ja " + str(kolmasluku) + " keskiarvo on " + str(pyöristetty_keskiarvo))