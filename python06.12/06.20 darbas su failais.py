# darbas su failais naudojant OPEN funkcija

# file = open("eurocup2023.txt", "a", encoding="utf8")
# file.write("Tekstas faile, kuriame išbandome OPEN funkciją ir dar kai ką")
# file.close()

# darbas su failais naudojant WITH funkcija

# with open("eurocup2024.txt", "w", encoding="utf8") as file:
#     file.write("Tekstas antrame failiuke\n")
#     file.write("Antra eilute\n")
#     file.write("Trečia eilute\n")


# ------------- UZDUOTIS No 1
# filename = input("Iveskite failo pavadinima-> ")
#
# try:
#     with open(filename, "w", encoding="utf8") as file:
#         content = file.read()
#         print("File content: ")
#         print(content)
# except FileNotFoundError:
#     print("File not found!")
# except:
#     print("Something went wrong!")

# --------------UZDUOTIS No 2. Sukurti faila, irasyti naujo failo pavadinima

# filename = input("Iveskite naujo failo pavadinima-> ")
# try:
#     with open(filename, "w", encoding="utf8") as file:
#         file.write("Negaliu patiketi: \n")
#         file.write("Vardas: Saulius\n")
#         file.write("Pavarde: Netaspats\n")
#         print("Duomenys sekmingai įrašyti")
# except:
#     print("Įvyko klaida įrašant duomenis į failą!")



