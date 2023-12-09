import re
import random

def generate_numbers_with_fractions():
    numbers_with_fractions = []

    for _ in range(30):
        numerator = random.randint(1, 12)
        denominator = random.randint(1, 99)
        fraction = f'{numerator}/{denominator}'
        numbers_with_fractions.append(fraction)

    return numbers_with_fractions

# Пример использования
generated_numbers_with_fractions = generate_numbers_with_fractions()
for fraction in generated_numbers_with_fractions:
    print(fraction)