import random

def generate_numbers():
    numbers = []
    prefixes = ['2', '3', '5', '6', '1']

    for _ in range(30):
        prefix = random.choice(prefixes)
        number = prefix + ''.join(random.choice('0123456789') for _ in range(12))
        optional_group = ''.join(random.choice('0123456789') for _ in range(random.choice([3, 5, 7, 8])))
        generated_number = number + optional_group
        numbers.append(generated_number)

    return numbers

# Пример использования
generated_numbers = generate_numbers()
for number in generated_numbers:
    print(number)
