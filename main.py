import re

# Получить ввод от пользователя
input_string = input("Введите строку: ")

# Регулярное выражение для поиска прописных букв
reg = r'[A-ZА-Я]'

# Найти все прописные буквы в строке с помощью регулярного выражения
uppercase_letters = re.findall(reg, input_string)

# Вывести найденные прописные буквы
if uppercase_letters:
    print("Прописные буквы в строке:")
    for letter in uppercase_letters:
        print(letter)
else:
    print("Прописных букв не найдено.")