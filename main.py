import checker # импортируем наш файл с классом
from pathlib import Path # библиотека для работы с путями к файлам

def file_extesion(file_path): # 'Вырезаем расширение в виде текста'
   return Path(file_path).suffix
def main():
   path = r''
   file = (input('Введите путь к  файлу: ')) # вводим путь к файлу
   path = rf'{file}'.replace('"', '') # заменяем кавычки на те, с которыми не будет возникать ошибок
   checker_ex = checker.Checker(path) # создаем экземпляр класс, в который инициализируем наш путь к файлу
   # Далее исходя из расширения файла обращаемся к функциям
   if file_extesion(path) == '.txt':
      print(checker_ex.check_file())
   if file_extesion(path) in ['.xlx', '.xlxs']:
      print(checker_ex.checker_for_excel())
   if file_extesion(path) in ['.csv']:
      print(checker_ex.checker_for_csv())
   if file_extesion(path) in ['.xml']:
      print(checker_ex.checker_for_xml())

if __name__ == '__main__':
   main()
