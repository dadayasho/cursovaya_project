import re
import openpyxl

class Checker:
    def __init__(self, file_path):
        self.file = file_path

    def check_file(self):
        pattern = r'\b[23561]\d{12}(?:\d{3}|\d{5}|\d{7}|\d{8})?\b' #проверка номера карты
        pattern2 = r'\b\d{1,12}\/\d{1,99}\b' #проверка cvv
        pattern3 = r'\b[A-Za-z ]{3,20}\b' #проверка имени
        with open(self.file, 'r') as file_txt:
            content = file_txt.read()
            content = re.sub(r'\n', ' ', content)
            if re.findall(pattern, content):
                if re.findall(pattern2, content) or re.findall(pattern3, content) or (re.findall(pattern2, content) and re.findall(pattern3, content)):
                    return True
            else:
                return False
    def checker_for_excel(self):
        workbook = openpyxl.load_workbook(self.path)
        sheet = workbook.active
        pattern = re.compile(r'\b[23561]\d{12}(?:\d{3}|\d{5}|\d{7}|\d{8})?\b')
        pattern_for_cvv = re.compile(r'\b\d{1,12}\/\d{1,99}\b')
        pattern_for_name = re.compile(r'\b[A-Za-z ]{3,20}\b')
        for row in sheet.iter_rows(): # Пройдемся по каждой ячейке в листе
            for cell in row:
                if cell.data_type != 's': # Проверяем, содержит ли ячейка текст
                    return(f"нет")
                else:
                    if pattern.search(cell.value):
                        if pattern_for_cvv.search(cell.value) or pattern_for_name.search(cell.value) or pattern_for_cvv.search(cell.value) and pattern_for_name.search(cell.value):
                            return (f"да")
                    else:
                        return(f"нет")
        workbook.close()
#"C:\Users\bende\Desktop\Рабочий стол\работы уник\test.txt"
