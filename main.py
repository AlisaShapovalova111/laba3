import re

# Получить ввод от пользователя
input_string = input("Введите строку: ")

# Регулярное выражение для поиска прописных букв
reg = r'[A-ZА-Я]'

# Найти все прописные буквы в строке с помощью регулярного выражения
uppercase_letters = re.findall(reg, input_string)
