# Tee ohjelma, joka kysyy käyttäjän iän ja tarkistaa, että se on mahdollinen

ikä = int(input("Ikäsi? "))
 
if 0 <= ikä <= 120:
    print("Ikä on realistinen")
else:
    print("Mahdotonta!")