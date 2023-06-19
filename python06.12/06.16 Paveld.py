

# class Animal:           #META KLAIDA DEL 4 EILUTES, LYGIAVIMAS
#     def __init__(self, name):
#
#     def make_sound(self):
#         print("The animal makes a sound")
#
#
# class Dog(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#     def make_sound(self):
#         print("The dog barks")
#
#
# dog = Dog("Bob", 5)
# dog.make_sound()
# print(f"My dog name is {dog.name}" + " and age is " + str(dog.age))


# class Vehicle:          # motinine klase
#     def __init__(self, brand):
#         self.brand = brand
#
#
#     def start_engine(self):
#         print("Engine started")
#
#     def stop_engine(self):
#         print("Engine stopper!")
#
#
# class Car(Vehicle):         #vaiko klase, kuri paveldi motinines klases tam tikras funkcijas
#     def drive(self):
#         print("car is driving!")
#
# car = Car("Toyota")
# print(car.brand)
# car.start_engine()
# car.drive()
# car.stop_engine()

# class Zmogus:    #kuriama motinine klase
#     def __init__(self, name, age):      #sukuriamos, isvardinamos savybes
#         self.name = name                #aprasome savybes
#         self.age = age
#
#
#     def display_info(self):             #aprasomos savybes
#         print(f"Zmogaus vardas yra {self.name}")
#         print(f"Zmogaus amzius yra {self.age}")
#
#
# class Darbuotojas(Zmogus):              #sukuriame vaiko klase (IHERITANCE)
#     def __init__(self, name, age, salary):  #isvardiname, kokias savybes tures darbuotojas
#         super().__init__(name, age)         #nurodome, kurias savybes tures is motinines klases
#         self.salary = salary                #aprasome papildoma darbuotojo savybe
#
#
#     def display_info(self):
#         super().display_info()       #panaudosiu motinines klases metoda. print vardas, amzius
#         print(f"Darbuotojo atlyginimas yra {self.salary}")
#
# zmogus = Zmogus("Antanas", 12)         #sukuriame motinines klases objekta
# darbuotojas = Darbuotojas("Jonas", 25, 1000)    #sukuriame vaiko klases objekta
#
# zmogus.display_info()
# print()
# darbuotojas.display_info()


#--------------------------------------------------- EGIDIJAUS DARBAS

# sukurti pirkiniu krepselio funkcionaluma. turim produkta ir turim krepseli

# class Product:
#     def __init__(self, title, price):
#         self.title = title
#         self.price = price
#
#
#     def display_info(self):
#         print(f" Produkto pavadinimas yra {self.title}")
#         print(f" Produkto kaina {self.price} €")
#
#
# class DiscountedProduct(Product):
#     def __init__(self, title, price, discount_percentage):
#         super().__init__(title, price)
#         self.discount_percentage =discount_percentage
#
#     def calculate_discount_price(self):
#         discount_amount = self.price * (self.discount_percentage / 100)
#         discounted_price = self.price - discount_amount
#         return discounted_price
#
#
#     def display_info(self):
#         super().display_info()
#         print(f" Nuolaida {self.discount_percentage} %")
#         print(f" Galutine kaina {self.calculate_discount_price()} €")
#
#
# class ShoppingCart(Product):
#     def __init__(self):
#         super(). __init__(title=None, price=None)
#         self.products = []
#
#     def add_product(self, product):
#         self.products.append(product)        #dedame produkta i krepseli
#         print(f" Produktas {product.title} priedetas i krepseli ")
#
#     def remove_product(self, product):      # kad isimti is krepselio produkta, turime patikrinti, ar jis ten yra
#         if product in self.products:            # tikriname, ar produktas idetas i krepseli
#             self.products.remove(product)
#             print(f" Produktas {product.title} pasalintas is krepselio ")
#         print(f" Produktas {product.title} nerastas krepselyje")
#
#
#     def calculate_total_price(self):
#         total_price = 0
#         for product in self.products:       # tikriname, kas yra musu krepselyje
#             total_price += product.price
#         return total_price
#
#
#
#
# produktas = Product("Pienas", 2.99)
# produktas1 = DiscountedProduct("Obuolys", 1.99, 15)
# produktas2 = Product("Sviestas", 4.99)
#
# shoppingcart = ShoppingCart()
# shoppingcart.add_product(produktas)
# shoppingcart.add_product(produktas1)
# shoppingcart.add_product(produktas2)
# print()
# for product in shoppingcart.products:
#     product.display_info()
#     print()
#
# total_price = shoppingcart.calculate_total_price()
# print(f" Bendra krepselio kaina {total_price} €")
# print()
#
# shoppingcart.remove_product(produktas)
#
# total_price = shoppingcart.calculate_total_price()
# print(f" Nauja bendra krepselio kaina {total_price} €")
# print()


#---------------------------- random listo pateikimas

# import random
# import time
# studentai = ["Rugile", "Egidijus", "Deividas", "Tomas", "Migle", "SauliusS", "SauliusA", "Ausrine", "Mantas", "Vaidas",
#              "Jurate", "Modestas"]
# random_student = random.choice(studentai)
# time.sleep(3)
# print("Atsitiktinai parinktas studentas: ", random_student)
#--------------------------------------------------------------------------

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_age(self):
#         return self.age
#
#     def set_age(self, age):
#         if age >= 0:
#             self.age = age
#         else:
#             print("Zmogaus amzius negali buti neigiamas")
#
# person = Person("Jonas", 32)
#
# print("name", person.get_name())
# print("age", person.get_age())
#
# person.set_name("Petras")
# person.set_age(10)
#
# print("New name", person.get_name())
# print("New age", person.get_age())
