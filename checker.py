import re


class Checker:
    def __init__(self, file_path):
        self.file = file_path

    def check_file(self):
        pattern = (r'\b[23561]\d{12}(?:\d{3}|\d{5}|\d{7}|\d{8})?\b') #проверка номера карты
        pattern2 = r'\b\d{1,12}\/\d{1,99}\b' #проверка cvv
        pattern3 = r'\b[A-Za-z ]{3,20}\b' #проверка имени
        with open(self.file, 'r') as file_txt:
            content = file_txt.read()
            content = re.sub(r'\n', ' ', content)
            if re.findall(pattern, content):
                if re.findall(pattern2, content) or re.findall(pattern3, content) or (re.findall(pattern2, content) and re.findall(pattern3, content)):
                    return True
                return True
            else:
                return False



#"C:\Users\bende\Desktop\Рабочий стол\работы уник\test.txt"
