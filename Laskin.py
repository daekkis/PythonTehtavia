# Laskin-ohjelma

Luku1 = float(input("Anna luku "))
Luku2 = float(input("Anna toinen luku "))
Laskutoimitus = input("Anna laskutoimitus joukosta (+, -, * ja /): ")

if Laskutoimitus == "+":
    print(f"{Luku1 + Luku2}")
elif Laskutoimitus == "-":
    print(f"{Luku1 - Luku2}")
elif Laskutoimitus == "*":
    print(f"{Luku1 * Luku2}")
elif Laskutoimitus == "/":
    print(f"{Luku1 / Luku2}")
else:
    print("Virhe")

