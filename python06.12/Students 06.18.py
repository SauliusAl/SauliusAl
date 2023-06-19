# # Sukurkite tuščią žodyną, kuris bus naudojamas kaip studentų sąrašas.
# # Leiskite vartotojui įvesti studento vardą, pavardę ir amžių.
# # Sukurkite naują studento žodyną su įvestais duomenimis ir pridėkite jį prie studentų sąrašo.
# # Po kiekvieno naujo studento pridėjimo, išveskite pranešimą apie sėkmingą pridėjimą.
# # Leiskite vartotojui pasirinkti, ar nori pridėti dar vieną studentą. Jei taip, grįžkite į žingsnį 2. Jei ne, tęskite į žingsnį 6.
# # Išveskite visus pridėtus studentus su jų vardais, pavardėmis ir amžiais

# class Studentai:
#     def __init__(self):
#         self.sarasas = []
#
#     def create_card(self, vardas, pavarde, amzius):
#         card = {
#             "vardas": vardas,
#             "pavarde": pavarde,
#             "amzius": amzius
#         }
#
#         self.card.append(kortele)
#         print("Kortele sekmingai sukurta")
#
#     def display_all_cards(self):
#         if not self.cards:
#             print("Kortele nera sukurta")
#         else:
#             print("Korteles: ")
#             for card in self.cards:
#                 print(f" vardas: {card['vardas']}")
#                 print(f" pavarde: {card['pavarde']}")
#                 print(f" amzius: {card['amzius']}")
#                 print("----------")
#
#     def delete_card(self, vardas, pavarde):
#         for post in self.cards:
#             if post["vardas"] == vardas:
#                 self.posts.remove(post)
#                 print("Kortele buvo istrinta")
#                 break
#             else:
#                 print("Kortele nebuvo rasta")
#
# card1 = Studentai()
# card1.create_card("Jonas", "Jonaitis", 19)
# card1.create_card("Valdas", "Valdenis", 20)
# card1.create_card("Arnas", "Arnaitis", 18)
# card1.display_all_cards()
# card1.delete_card("Jonas", "Jonaitis")
# card1.display_all_cards()







