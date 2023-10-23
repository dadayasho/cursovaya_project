import re
import csv
import docx

class Checker:
    def __init__(self, file_path):
        self.file = file_path

    def check_file(self):
        with open(self.file, 'r', endcoding='utf-8') as file_txt:
            content = file_txt.read()

        pass
