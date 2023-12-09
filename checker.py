import re  # библиотека для работы с регулярками
import openpyxl  #
import csv  # библиотека для работы с csv
import xml.etree.ElementTree as ET  # библиотека для работы с xml


class Checker:
    def __init__(self, file_path):
        self.file = file_path  # Инициализируем путь к файлу

    def check_file(self):
        pattern = (r'\b[23561]\d{12}(?:\d{3}|\d{5}|\d{7}|\d{8})?\b')  # проверка номера карты
        pattern_for_cvv = r'\b\d{1,2}\/\d{1,2}\b'  # проверка cvv
        pattern_for_name = r'\b[A-Za-z ]{3,20}\b'  # проверка имени

        with open(self.file, 'r') as file_txt:
            content = file_txt.read()
            content = re.sub(r'\n', ' ', content)
            if content:
                if not re.findall(pattern, content):  # если есть номер карты то идем дальше, иначе нет
                    return "не содержит ничего"
                else:
                    if re.findall(pattern_for_cvv, content) or re.findall(pattern_for_name, content) or \
                            (re.findall(pattern_for_cvv, content) and re.findall(pattern_for_name,
                                                                                 content)):  # если есть cvv или имя держателя или (cvv и имя держателя)
                        return "содержит номер карты и cvv или имя держателя"
                    else:
                        return "содержит номер карты"
            else:
                return "файл пуст"

    def checker_for_excel(self):

        workbook = openpyxl.load_workbook(self.file) # открываем эксель файл
        sheet = workbook.active # подгружаем workbook
        # Считывание значений по строкам
        values = []
        for row in sheet.iter_rows(values_only=True):
            values.extend(row)

        # Запись значений в переменную сплошным текстом
        text_content = ' '.join(map(str, values))

        # Проверка текста по регулярным выражениям
        pattern = re.compile(r'\b[23561]\d{12}(?:\d{3}|\d{5}|\d{7}|\d{8})?\b') # проверка номера карты
        pattern_for_cvv = re.compile(r'\b\d{1,12}\/\d{1,99}\b') # проверка cvv
        pattern_for_name = re.compile(r'\b[A-Za-z ]{3,20}\b') # проверка имени

        if not pattern.search(text_content): # проверяем на содержание чего-либо
            return "не содержит ничего"
        else:
            if pattern_for_cvv.search(text_content) or pattern_for_name.search(text_content) or \
                    (pattern_for_cvv.search(text_content) and pattern_for_name.search(text_content)):
                return "содержит номер карты и cvv или имя держателя"
            else:
                return "содержит номер карты"

        workbook.close() # закрываем workbook

    def checker_for_csv(self):  # Проверка файлов csv формата

        with open(self.file, 'r', newline='', encoding='utf-8') as csv_file: #открытие csv файла
            csv_reader = csv.reader(csv_file)
            values = []

            for row in csv_reader: # Считывание значений по строкам
                values.extend(row)

            text_content = ' '.join(map(str, values)) # Запись значений в переменную сплошным текстом

            pattern = re.compile(r'\b[23561]\d{12}(?:\d{3}|\d{5}|\d{7}|\d{8})?\b')
            pattern_for_cvv = re.compile(r'\b\d{1,12}\/\d{1,99}\b')
            pattern_for_name = re.compile(r'\b[A-Za-z ]{3,20}\b')

            if not pattern.search(text_content):
                return "не содержит ничего"
            else:
                if pattern_for_cvv.search(text_content) or pattern_for_name.search(text_content) or \
                        (pattern_for_cvv.search(text_content) and pattern_for_name.search(text_content)):
                    return "содержит номер карты и cvv или имя держателя"
                else:
                    return "содержит номер карты"

    def checker_for_xml(self):
        try:
            # Пытаемся загрузить XML-документ и получить корневой элемент
            tree = ET.parse(self.file)  # Загрузка XML-файла в объект ElementTree
            root = tree.getroot()  # Получение корневого элемента XML-документа

            values = []
            for element in root.iter(): # Проходимся по всем элементам XML-документа и собираем их текстовое содержимое
                values.append(element.text)

            text_content = ' '.join(map(str, values))

            pattern = re.compile(r'\b[23561]\d{12}(?:\d{3}|\d{5}|\d{7}|\d{8})?\b')
            pattern_for_cvv = re.compile(r'\b\d{1,12}\/\d{1,99}\b')
            pattern_for_name = re.compile(r'\b[A-Za-z ]{3,20}\b')

            if not pattern.search(text_content):
                return "не содержит ничего"
            else:
                if pattern_for_cvv.search(text_content) or pattern_for_name.search(text_content) or \
                        (pattern_for_cvv.search(text_content) and pattern_for_name.search(text_content)):
                    return "содержит номер карты и cvv или имя держателя"
                else:
                    return "содержит номер карты"
        except Exception as e:
            return f"Произошла ошибка при обработке XML: {e}"
