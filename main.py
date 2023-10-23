import checker

def main():
   path = r''
   file = (input('Введите путь к  файлу: '))
   path = rf'{file}'.replace('"', '')
   checker_ex = checker.Checker(path)
   print(checker_ex.check_file())

if __name__ == '__main__':
   main()
