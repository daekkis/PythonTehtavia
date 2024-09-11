# Tee ohjelma, joka kysyy kahden käyttäjän nimet ja iät. Tämän jälkeen ohjelma tulostaa käyttäjien ikien summan.

Nimi1 = input("Kerro nimesi: ")
Ika1 = int(input("Entä ikäsi: "))

Nimi2 = input("Kerro nimesi: ")
Ika2 = int(input("Entä ikäsi: "))
Summa = Ika1 + Ika2

print(f"{Nimi1} ja {Nimi2} ovat yhteensä {Summa} vuotta vanhoja")