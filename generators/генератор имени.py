import random
import string

def generate_names():
    names = []

    for _ in range(30):
        name_length = random.randint(3, 20)
        name = ''.join(random.choice(string.ascii_letters + ' ') for _ in range(name_length))
        names.append(name)

    return names

# Пример использования
generated_names = generate_names()
for name in generated_names:
    print(name)