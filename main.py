# Vstupní proměnné
mesta = [
    "Praha", "Viden", "Olomouc",
    "Svitavy", "Zlin", "Ostrava"
]
domeny = ("gmail.com", "seznam.cz", "email.cz")
slevy = ("Olomouc", "Svitavy", "Ostrava")
ceny = (150, 200, 120, 120, 100, 180)
dvojita_cara = "=" * 60
cara = "-" * 60
nabidka = \
    """1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180"""

# Pozdrav a nabídka
print("Vítejte v naší aplikaci detinatio".upper())
print(dvojita_cara)
print(nabidka)
print(dvojita_cara)

# Vybrat destinaci, verifikace destinace
vyber = input("Vyber cislo destinace: ".upper())
if vyber.isnumeric() and int(vyber) in range(1, 7):
    destinace = int(vyber) - 1
    print("destinace: ".upper() + mesta[destinace] + " cena: ".upper() + str(ceny[destinace]))
    print(cara)
else:
    print(vyber + " Neexistuje! Ukončuji".upper())
    quit()

# Ověřit jestli uživatel dostane slevu
if mesta[destinace] in slevy:
    sleva = int(ceny[destinace]) * 0.25
    cena_posleve = int(ceny[destinace]) - int(sleva)
    print("Získáváte 25% slevu! ".upper() + "cena: ".upper() + str(cena_posleve))
    print(cara)
else:
    cena_posleve = ceny[destinace]
# Ověřit validní jméno a přijmení
jmeno = input("Zadej jméno: ".upper())
prijmeni = input("Zadej příjmení: ".upper())
print(dvojita_cara)
if not jmeno.isalpha() or not prijmeni.isalpha():
    print("Zadané neplatné jméno a příjmení! Ukončuji")
    print(cara)
    quit()

# Ověření validni emailové adresy
email = input("Zadej email: ".upper())
domeny1 = email.rsplit("@")
if "@" in email and domeny1[1] in domeny:
    print(email + " Email je vpořádku.")
    print(dvojita_cara)
else:
    print("Neplatná emailová adresa! Ukončuji!")
    print(cara)
    quit()

# Rekapitulace objednávky
print("Děkuji ".upper() + jmeno + ", za objednávku".upper())
print("cil. destinace: ".upper() + str(mesta[destinace]) + ", cena jizdného: ".upper() + str(cena_posleve))
print("na tvůj mail: ".upper() + email + ", jsme ti poslali lístek".upper())
print(dvojita_cara)

# Uložení do souboru
with open("objednavky.txt", mode="a") as f:
    f.write("Jméno: " + jmeno + "\n")
    f.write("Příjmení: " + prijmeni + "\n")
    f.write("Email: " + email + "\n")
    f.write("Destinace: " + mesta[destinace] + "\n")
    f.write("Cena: " + str(cena_posleve) + "\n")
    f.write("Děkujeme za nákup".upper())
    f.write("\n" + dvojita_cara + "\n\n")
