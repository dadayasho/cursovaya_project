import re


class Checker:
    def __init__(self, file_path):
        self.file = file_path

    def check_file(self):
        with open(self.file, 'r') as file_txt:
            content = file_txt.read()
            content = re.sub(r'\n', ' ', content)
            pattern = (r'\b[23561]\d{12}(?:\d{3}|\d{5}|\d{7}|\d{8})?\b')
            return (re.findall(pattern, content))


