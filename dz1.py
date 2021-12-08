# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_file = open(r"dz1.txt", "w", encoding="utf-8")
str_user = input("Введите данные с клавиатуры: \n")
while str_user:
    my_file.writelines(str_user)
    str_user = input("Введите данные с клавиатуры: \n")
    if not str_user:
        break
my_file.close()
my_file = open("dz1.txt", "r", encoding="utf-8")
read = my_file.readlines()
print(read)
my_file.close()



