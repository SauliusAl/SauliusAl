# import colorama
# from colorama import Fore, Style
# colorama.init()
class Skaiciuotuvas:
    def __init__(self):
        self.result = 6
    def sudetis(self, skaicius):
        self.result += skaicius

    def atimtis(self, skaicius):
        self.result -= skaicius

    def daugyba(self, skaicius):
        self.result *= skaicius

    def dalyba(self, skaicius):
        self.result /= skaicius

    def dalyba(self, skaicius):
        if skaicius != 0:
            self.result /= skaicius
        else:
            print("Dalyba is nulio negalima")

    def isvalyti(self):
        self.result = 0

    def get_result(self):             #KADANGI NERA PRINT, REIKIA GET, KURIS GRAZINTU SUSKAICIUOTA REIKSME, SET METODAS NUSTATO REIKSME, GET -gauna reiksme
        return self.result

skaiciuoklis = Skaiciuotuvas()
while True:
    print("Pasirinkite norima veiksma_> ")
    print("1. Sudetis")
    print("2. Atimtis")
    print("3. Daugybe")
    print("4. Dalyba")
    print("5. Isvalyti")
    pasirinkimas = input("Iveskite pasirinkimo numeri_> ")

    if pasirinkimas == "1":
        skaicius = int(input("Iveskite skaiciu_> "))
        skaiciuoklis.sudetis(skaicius)

    elif pasirinkimas == "2":
        skaicius = int(input("Iveskite skaiciu_> "))
        skaiciuoklis.atimtis(skaicius)

    elif pasirinkimas == "3":
        skaicius = int(input("Iveskite skaiciu_> "))
        skaiciuoklis.daugyba(skaicius)

    elif pasirinkimas == "4":
        skaicius = float(input("Iveskite skaiciu_> "))
        skaiciuoklis.dalyba(skaicius)

    elif pasirinkimas == "5":
        skaiciuoklis.isvalyti()

    else:
        print("Negalimas veiksmas")


    print("Result: ", skaiciuoklis.get_result())
    print()




