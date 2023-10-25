import re


class Checker:
    def __init__(self, file_path):
        self.file = file_path

    def check_file(self):
        with open(self.file, 'r') as file_txt:
            content = file_txt.read()
            content = re.sub(r'\n', ' ', content)
            pattern = (r'\b[23561]\d{12}(?:\d{3}|\d{5}|\d{7}|\d{8})?\b') #проверка номера карты
            pattern2 = r'\b\d{1,12}\/\d{1,99}\b' #проверка cvv
            pattern3 = r'\b[A-Za-z ]{3,20}\b' #проверка имени
            return (re.findall(pattern3, content))


#"C:\Users\bende\Desktop\Рабочий стол\работы уник\test.txt"