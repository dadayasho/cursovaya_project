import re # библиотека для работы с регулярками
import openpyxl #
import csv # библиотека для работы с csv
import xml.etree.ElementTree as ET # библиотека для работы с xml
class Checker:
    def __init__(self, file_path):
        self.file = file_path # Инициализируем путь к файлу

    def check_file(self):
        pattern = (r'\b[23561]\d{12}(?:\d{3}|\d{5}|\d{7}|\d{8})?\b') #проверка номера карты
        pattern_for_cvv = r'\b\d{1,12}\/\d{1,99}\b' #проверка cvv
        pattern_for_name = r'\b[A-Za-z ]{3,20}\b' #проверка имени

        with open(self.file, 'r') as file_txt:
            content = file_txt.read()
            content = re.sub(r'\n', ' ', content)
            if re.findall(pattern, content): # если есть номер карты то идем дальше, иначе нет
                if re.findall(pattern_for_cvv, content) or re.findall(pattern_for_name, content) or \
                   (re.findall(pattern_for_cvv, content) and re.findall(pattern_for_name, content)): # если есть cvv или имя держателя или (cvv и имя держателя)
                    return "да"
            else:
                return "нет"

    def checker_for_excel(self):
        workbook = openpyxl.load_workbook(self.path)
        sheet = workbook.active
        pattern = re.compile(r'\b[23561]\d{12}(?:\d{3}|\d{5}|\d{7}|\d{8})?\b')
        pattern_for_cvv = re.compile(r'\b\d{1,12}\/\d{1,99}\b')
        pattern_for_name = re.compile(r'\b[A-Za-z ]{3,20}\b')
        for row in sheet.iter_rows(): # Пройдемся по каждой ячейке в листе
            for cell in row:
                if cell.data_type != 's': # Проверяем, содержит ли ячейка текст
                    return "нет"
                else:
                    if pattern.search(cell.value): # если есть номер карты то идем дальше, иначе нет
                        if pattern_for_cvv.search(cell.value) or pattern_for_name.search(cell.value) or \
                           pattern_for_cvv.search(cell.value) and pattern_for_name.search(cell.value): # если есть cvv или имя держателя или (cvv и имя держателя)
                            return "да"
                    else:
                        return "нет"
        workbook.close() # закрываем файл
        return
    def checker_for_csv(self): #Проверка файлов csv формата
        pattern = re.compile(r'\b[23561]\d{12}(?:\d{3}|\d{5}|\d{7}|\d{8})?\b')
        pattern_for_cvv = re.compile(r'\b\d{1,12}\/\d{1,99}\b')
        pattern_for_name = re.compile(r'\b[A-Za-z ]{3,20}\b')

        with open(self.path, 'r', newline='') as csv_file: # открытие и чтение csv файла
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                for cell in row:
                    if not isinstance(cell, str):  # Check if cell contains text
                        return "нет"
                    else:
                        if pattern.search(cell): # если есть CVV то идем дальше, иначе нет
                            if pattern_for_cvv.search(cell) or pattern_for_name.search(cell) or \
                               pattern_for_cvv.search(cell) and pattern_for_name.search(cell): # если есть cvv или имя держателя или (cvv и имя держателя)
                                return "да"
                        else:
                            return "нет"
        return "нет"

    def checker_for_xml(self):
        pattern = re.compile(r'\b[23561]\d{12}(?:\d{3}|\d{5}|\d{7}|\d{8})?\b')
        pattern_for_cvv = re.compile(r'\b\d{1,12}\/\d{1,99}\b')
        pattern_for_name = re.compile(r'\b[A-Za-z ]{3,20}\b')

        try:
            tree = ET.parse(self.path)
            root = tree.getroot()

            for element in root.iter():
                if not isinstance(element.text, str):  # Check if element text is a string
                    return "нет"
                else:
                    if pattern.search(element.text): # если есть номер карты то идем дальше, иначе нет
                        if pattern_for_cvv.search(element.text) or pattern_for_name.search(element.text) or \
                           pattern_for_cvv.search(element.text) and pattern_for_name.search(element.text): # если есть cvv или имя держателя или (cvv и имя держателя)
                            return "да"
                    else:
                        return "нет"
        except ET.ParseError:
            return "нет"  # Return "нет" if there's an error parsing the XML file
        return "нет"

#"C:\Users\bende\Desktop\Рабочий стол\работы уник\test.txt"
