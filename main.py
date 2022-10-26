lohnstunde = input("Bitte gebe deinen Stundenlohn ein: ")
tag = 8 * int(lohnstunde)
Monat = 20 * int(tag)
jahr = 12* int(Monat)
taxes = int(jahr) * 0.10
print("Dein Stundenlohn beträgt " + str(lohnstunde) + "€")
print("Damit verdienst du " + str(tag) + "€ am tag")
print("und somit " + str(Monat) + "€ pro Monat")
print("im Jahr verdienst du " + str(jahr) +"€")
print("pro jahr zahlst du " + str(taxes) + "€ pro jahr")

input("")