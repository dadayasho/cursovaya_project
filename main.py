import checker
from pathlib import Path

def file_extesion(file_path):
   return Path(file_path).suffix
def main():
   path = r''
   file = (input('Введите путь к  файлу: '))
   path = rf'{file}'.replace('"', '')
   checker_ex = checker.Checker(path)
   if file_extesion(path) == '.txt':
      print(checker_ex.check_file())
   if file_extesion(path) in ['.xlx', '.xlxs']:
      print(checker_ex.checker_for_excel())

if __name__ == '__main__':
   main()
