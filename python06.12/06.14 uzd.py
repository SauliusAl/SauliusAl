


# class Knyga:
#     def __init__(self, pavadinias, autorius, puslapiai):
#         self.pavadinimas = pavadinias
#         self.autorius = autorius
#         self.puslapiai = puslapiai
# #         parasyti metoda, ar knyga turi > 300 spl
#     def virs_300_psl(self):
#         if self.puslapiai > 300:
#             return True
#         else:
#             return False
#
# Knyga1 = Knyga("Dievu miskas", "Balys Sruoga", 250)
# Knyga2 = Knyga("Haris Poteris", "J.Rowling", 600)
#
# print(Knyga1.virs_300_psl())
# print(Knyga2.virs_300_psl())


# class Darbuotojas:
#     def __init__(self, vardas, pavarde, atlyginimas):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.atlyginimas = atlyginimas
# #         PARASYTI METODA, KURIS PADIDINS DARBUOTOJO ATLYGINIMA TAM TIKRU %
#     def padidinti_atlyginimas(self, procentai):
#         padidinimas = self.atlyginimas * procentai / 100
#         self.atlyginimas += padidinimas
#
#     def pakeisti_pavarde(self, nauja_pavarde):
#         self.pavarde = nauja_pavarde
#         print("Pavarde pakeista sekmingai")
#
#     def visa_informacija(self):
#         print(f"informacija apie darbuotoja: ")
#         print(f"Vardas: {self.vardas}")
#         print(f"Pavarde: {self.pavarde}")
#         print(f"Atlyginimas: {self.atlyginimas}")
#
# Darbuotojas1 = Darbuotojas("Jonas", "Jonaitis", 1000)
# Darbuotojas2 = Darbuotojas("Petras", "Petraitis", 1300)
#
# Darbuotojas1.padidinti_atlyginimas(10)
# print(f"Naujas atlyginimas: {Darbuotojas1.atlyginimas}")
# Darbuotojas1.pakeisti_pavarde("Kazlauskas")
# print(f"{Darbuotojas1.vardas} {Darbuotojas1.pavarde} pasikeite pavarde!")
#
# Darbuotojas1.visa_informacija()
#

# Darbuotojas2.padidinti_atlyginimas(20)
# print(f"Naujas atlyginimas: {Darbuotojas2.atlyginimas}")

# -------------------------------------------------------------------------------------
# class Preke:
#     def __init__(self, pavadinimas, kaina, kiekis):
#         self.pavadinimas = pavadinimas
#         self.kaina = kaina
#         self.kiekis = kiekis
#         #  PRODUKTO KAINA 5EUR, REIKIA ATNAUJINTI KAINA, nauja kaina 3.50 EUR
#     def atnaujinti_kaina(self, nauja_kaina):
#         self.kaina = nauja_kaina
#         print(f"{self.pavadinimas} nauja kaina {nauja_kaina}")
#
# # pirkejas nori pirkti 7 vnt (preke), taciau sandelyje yra 5vnt. Mums reikia pasakyti pirkejui, kad liko tik 5
#     def sandelio_likutis(self, pardavimo_kiekis):
#         if pardavimo_kiekis <= self.kiekis:
#             self.kiekis -= pardavimo_kiekis
#             print(f"Parduota {self.pavadinimas} {pardavimo_kiekis}")
#         else:
#             print(f"Nepakanka prekiu: {self.pavadinimas}")
#
#     def sandelio_papildymas(self, padidintas_likutis):
#         self.kiekis += padidintas_likutis
#         print(f"Padidintas kiekis {self.pavadinimas} {padidintas_likutis}")
#
# Preke1 = Preke ("Pienas", 5, 10)
# Preke2 = Preke ("Duona", 3, 5)
#
#
# Preke1.atnaujinti_kaina(3.50)
# Preke2.atnaujinti_kaina(2.00)
#
# Preke1.sandelio_likutis(20)
# Preke2.sandelio_likutis(10)
#
# Preke1.sandelio_papildymas(20)
# Preke2.sandelio_papildymas(12)
#
# print("Sandelio likutis", Preke1.kiekis)
# print("Sandelio likutis", Preke2.kiekis)

# -------------------------------------------------------------------------
# -------5.BLOG KURIMAS

# class Blog:
#     def __init__(self):
#         self.posts = []
#     def create_post(self, pavadinimas, aprasymas):
#         post = {
#             "pavadinimas": pavadinimas,
#             "aprasymas": aprasymas
#         }
#
#         self.posts.append(post)
#         print("Irasas sekmingai sukurtas")
#
#
#     def display_all_posts(self):
#         if not self.posts:
#             print("No blog post found")
#         else:
#             print("Blog posts: ")
#             for posts in self.posts:
#                 print(f" pavadinimas: {posts['pavadinimas']}")
#                 print(f" aprasymas: {posts['aprasymas']}")
#                 print("--------")
#
#     def update_post(self, pavadinimas, naujas_aprasymas):
#         for post in self.posts:
#             if post["pavadinimas"] == pavadinimas:
#                 post["aprasymas"] = naujas_aprasymas
#                 print(f"Blog pos updated")
#                 break
#         else:
#             print("Blog posts not found")
#
#     def delete_post(self, pavadinimas):
#         for post in self.posts:
#             if post["pavadinimas"] == pavadinimas:
#                 self.posts.remove(post)
#                 print("Post was removed")
#                 break
#         else:
#             print("Post was not found")
#
#
# post1 = Blog() #naudojame ta pati objekta, nes jis neturi apribojimu
#
# post1.create_post("Duomenu analitikos studentai uzkariavo pasauli", "Karta gyveno analitikai, kurie ismoks programuoti")
# post1.create_post("Mokslininkai isrado dvirati", "Naujos kartos dviratis be ratu...")
# post1.create_post("Didzioji sausra", "Lietuva kencia nuo lietaus stygiaus")
# post1.display_all_posts()
# post1.update_post("Duomenu analitikos studentai uzkariavo pasauli", "Dukart gyveno analitikas, kurie ismoks programuoti")
# post1.display_all_posts()
# post1.delete_post("Duomenu analitikos studentai uzkariavo pasauli")
# post1.display_all_posts()




