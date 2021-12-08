# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

my_file = open("dz2.txt", "r", encoding="utf-8")
with my_file as file:
    my_list = file.readlines()
for i in range(len(my_list)):
    new_l = my_list[i].split()
    print(f'Количество строк в файле {len(my_list)}. В {i + 1}-ой строке {len(new_l)} слов(а)')
