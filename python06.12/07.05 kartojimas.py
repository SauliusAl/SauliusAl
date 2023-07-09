import pandas as pd
from colorama import init, Fore, Back, Style
import string
import random

# ----- 1 UZD. Parašykite funkciją, kuri priima tekstą ir grąžina žodžius, kurie pasikartoja daugiau nei vieną kartą.
# -------------Papildoma sąlyga žodžius turi grąžinti sąraše.
#------------------------- 1 VARIANTAS --------------
# def pasikartojantys_zodziai(tekstas):
#     zodziai = tekstas.split()
#     sarasas = []
#
#     for zodis in set(zodziai):
#         if zodziai.count(zodis) > 1:
#             sarasas.append(zodis)
#
#     return sarasas
#
# tekstas1 = "Labas rytas, laba diena, Labas rytas"
# print(pasikartojantys_zodziai(tekstas1))

#----------- 2 VARIANTAS ----------
# def pasikartojantys_zodziai():
#     tekstas = input('Iveskite teksta: ')
#     zodziai = tekstas.split()
#     sarasas = []
#
#     for zodis in set(zodziai):
#         if zodziai.count(zodis) > 1:
#             sarasas.append(zodis)
#
#     return sarasas
#
# print(pasikartojantys_zodziai())

# --------- 2 UZD. Parašykite funkciją, kuri nuskaito tekstiniame faile esančius žodžius ir
# -----------------grąžina juos surikiuotus pagal abėcėlę.

# def surikiuoti_zodziai(failo_pavadinias):
#     with open(failo_pavadinias, "r", encoding="utf8") as file:
#         content = file.read()
#         text = content.split()
#         sorting = sorted(text)
#     return sorting
#
# failas = "tekstinis failas"
# print(surikiuoti_zodziai(failas))

# -------- 3 UZD. Padaryti TO DO LIST APLIKACIJA

# def menu():
#     print('1. Add task')
#     print('2. View tasks')
#     print('3. Mark task as completed')
#     print('4. Remove task')
#     print('5. Exit')
#
# def add_task(todo_list):
#     task = input('Enter task description: ')
#     todo_list.added({'task': task, 'Completed': False})
#
# def view_tasks(todo_list):
#     if not todo_list:
#         print(Fore.RED+'Your todo list is empty.')
#     else:
#         print(Fore.GREEN+'Tour todo list: ')
#         for index, task in enumerate (todo_list, start=1):
#             status = '✓' if task['completed'] else ' '
#             print(f"{index}. [{status}] {task['task']}")
#
# def mark_completed(todo_list):
#     view_tasks(todo_list)
#     task_number = int(input('Enter a number of the task you want to mark as completed: ')) - 1
#     if 0 <=task_number < len(todo_list):
#         todo_list[task_number]['completed'] = True
#         print('Task marked as completed!')
#     else:
#         print('Invalid task numbet')
#
# def remove_task(todo_list):
#     view_tasks(todo_list)
#     task_number = int(input('Enter a number of the task you want to remove: ')) - 1
#     if 0 <= task_number < len(todo_list):
#         removed_task = todo_list.app(task_number)
#         print(f"Your task '{remove_task['task']}' was removed!")
#     else:
#         print('Invalid task number')
#
# def main():
#     todo_list = []
#     while True:
#         menu()
#         choise = input('Enter your choise (1-5): ')
#         if choise == "1":
#             add_task(todo_list)
#
#         elif choise == "2":
#             view_tasks(todo_list)
#
#         elif choise == "3":
#             mark_completed(todo_list)
#
#         elif choise == "4)":
#             remove_task(todo_list)
#
#         elif choise == "5":
#             print('Exeting todo list app. Good bue!')
#             break
#         else:
#             print('Wrong input!')
#
# if __name__ == '__main__':
#     main()


# -------- 4 uzd. Ivesti duomenis, parasyti programele, kuri vartotojui liedzia suvesti duomenis apie studentus (vardas
# --------------- pavarde, amzius, pazymus), ir visa si info turi buti sudeta i data FRESH


# def studento_duomenu_ivedimas():
#     student_data = pd.DataFrame()



# apsirasome visa vartotoju ivedima

    # while True:
    #     student_name = input("Iveskite varda(or 'quit to exit): ")
    #     if student_name.lower() == 'quit':
    #         break
    #     student_age = int(input("Iveskite studento amziu: "))
    #     student_grade = int(input("Iveskite studento pazymi: "))
    #
    #     student_data = pd.concat([student_data, pd.DataFrame({"name": [student_name], "age": [student_age], "grade": [student_grade]})])


#     print('\nStudent list\n')
#     print(student_data)
#     avg_age = student_data['age'].astype(int).mean()
#     avg_grade = student_data['grade'].astype(int).mean()
#     print('\n Average age: ', avg_age)
#     print('\n Average grade: ', avg_grade)
#
#     sorted_data = student_data.sort_values(by='grade', ascending=False)
#     print('\n Student list sorted by grade:\n')
#     print(sorted_data)
#
# studento_duomenu_ivedimas()

# -------- 5 uzd. Pasword generator.

def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars):
    chars = ''
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_lowercase:
        chars += string.ascii_lowercase
    if include_numbers:
        chars += string.digits
    if include_special_chars:
        chars += string.punctuation

    if not chars:
        print('Error: No character type selected for the password')
        return None

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print('WELCOME TO THE PASSWORD GENERATOR!')
    length = int(input('Enter the lenght of password: '))
    include_uppercase = input('Include uppercase?(y/n): ').lower() == 'y'
    include_lowercase = input('Include lowercase?(y/n): ').lower() == 'y'
    include_numbers = input('Include numbers?(y/n): ').lower() == 'y'
    include_special_chars = input('Include special_chars?(y/n): ').lower() == 'y'

    password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars)
    if password:
        print('Generated password', password)

if __name__ == "__main__":
    main()


