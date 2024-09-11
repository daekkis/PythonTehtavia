# Tee ohjelma, joka kysyy käyttäjältä salasanan. Jos salasana on oikea, ohjelma tulostaa salaisen tiedon. 

salasana = "Jekku"
#tieto = "Rakastan sua, mutta olen nainen"
#Kysymys = input("Salasana? ")

#while Kysymys != salasana:
#    print("Yritä uudestaan")
#    Kysymys = input("Salasana? ")
#else:
#    print(tieto) 



# Käytetään for-silmukkaa 3 yrityksen ajan

for yritys in range(3):
    Kysymys = input("Salasana? ")
    if Kysymys == salasana:
        print("Onnea, pääsit salaiseen tietooni:")
        print("Rakastan sua, mutta olen nainen")
        break
    else:
        print("Yritä uudestaan")
else:
    print("GAME OVER")
