# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное
# число N – количество элементов в массиве. В последующих строках записаны N
# целых чисел Ai. Последняя строка содержит число X
#
# пример
# 5
# 1 2 3 4 5
# 3
# -> 1

# n = int(input('Введите натуральное число: '))
# list_1 = []
# for i in range(1, n + 1):
#     m = int(input('Введите значение для массива: '))
#     list_1.append(m)
# print(list_1)
# x = int(input('Введите искомое число: '))
# count = 0
# for i in range(1, len(list_1)):
#     if x == list_1[i]:
#         count += 1
# print(count)


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине
# элемент к заданному числу X. Пользователь в первой строке вводит натуральное
# число N – количество элементов в массиве. В последующих строках записаны N
# целых чисел Ai. Последняя строка содержит число X
#
# пример
# 5
# 1 2 3 4 5
# 6
# -> 5

# n = int(input('Введите натуральное число: '))
# list_1 = []
# for i in range(1, n + 1):
#     m = int(input('Введите значение для массива: '))
#     list_1.append(m)
# print(list_1)
# x = int(input('Введите искомое число: '))
# temp = float
# min_diff = n
# nearest_value = int
# for y in range(1, len(list_1)):
#     temp = abs(list_1[y] - x)
#     if min_diff > temp:
#         min_diff = temp
#         nearest_value = list_1[y]
# print(nearest_value)


# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо
# только английские, либо только русские буквы.
#
# пример
#
# Ввод:
# ноутбук
# Вывод:
# 12

list_1 = ['a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r', 'а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т']
list_2 = ['d', 'g', 'д', 'к', 'л', 'м', 'п', 'у']
list_3 = ['b', 'c', 'm', 'p', 'б', 'г', 'ё', 'ь', 'я']
list_4 = ['f', 'h', 'v', 'w', 'y', 'й', 'ы']
list_5 = ['k', 'ж', 'з', 'х', 'ц', 'ч']
list_8 = ['j', 'x', 'ш', 'э', 'ю']
list_10 = ['q', 'z', 'ф', 'щ', 'ъ']
dictionary = {1: list_1, 2: list_2, 3: list_3, 4: list_4, 5: list_5, 8: list_8, 10: list_10}
n = str.lower(input('введите слово: '))
print(n)
count = 0
for i in n:
    for k, v in dictionary.items():
        if i in v:
            count = count + k
print(count)
