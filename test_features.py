import opejjjnpyxl
import re

path = r''
file = (input('Введите путь к  файлу: '))
path = rf'{file}'.replace('"', '')
# Открываем файл Excel
workbook = openpyxl.load_workbook(path)

# Выбираем активный лист (может потребоваться адаптировать под вашу ситуацию)
sheet = workbook.active

# Регулярные выражения для поиска
pattern = re.compile(r'\b[23561]\d{12}(?:\d{3}|\d{5}|\d{7}|\d{8})?\b') #проверка номера карты
pattern_for_cvv = re.compile(r'\b\d{1,12}\/\d{1,99}\b')
pattern_for_name = re.compile(r'\b[A-Za-z ]{3,20}\b')
#проверка cvv
# Пройдемся по каждой ячейке в листе
for row in sheet.iter_rows():
    for cell in row:
        # Проверяем, содержит ли ячейка текст
        if cell.data_type != 's':
            print(f"нет")
        else:
            if pattern.search(cell.value):
                # Если найдено первое слово, ищем второе
                if pattern_for_cvv.search(cell.value) or pattern_for_name.search(cell.value) or pattern_for_cvv.search(cell.value) and pattern_for_name.search(cell.value):
                    print(f"да")
            else:
                print(f"нет")
#добавить паттерн для поиска имени, испарвить условие, создать хэш таблицу с ключами да/нет
#"C:\Users\bende\Desktop\Рабочий стол\работы уник\Книга1.xlsx"
# Закрываем файл Excel
workbook.close()
