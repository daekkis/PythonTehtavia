# Tee ohjelma, joka kysyy käyttäjältä kaksi lukua ja tulostaa niiden osamäärän.

Luku1 = float(input("Anna ensimmäinen luku: "))
Luku2 = float(input("Anna toinen luku: "))
Osamäärä = Luku1 / Luku2

# Haluttujen desimaalien määrä rajataan :.3f -> 
print(f"Lukujen osamäärä: {Osamäärä:.3f}")
