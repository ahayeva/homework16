
expression = input("Введіть арифметичний вираз (наприклад, 23+12): ")
try:
    num1, operator, num2 = expression.split()
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Неправильний формат виразу")
    exit(1)

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        print("Ділення на нуль неможливе")
        exit(1)
    result = num1 / num2
else:
    print("Неправильний оператор")
    exit(1)

print(f"Результат: {result}")
#exercise17
import random

random_numbers = [random.randint(-100, 100) for _ in range(20)]

min_number = min(random_numbers)
max_number = max(random_numbers)
negative_count = sum(1 for num in random_numbers if num < 0)
positive_count = sum(1 for num in random_numbers if num > 0)
zero_count = sum(1 for num in random_numbers if num == 0)
print(f"Мінімальний елемент: {min_number}")
print(f"Максимальний елемент: {max_number}")
print(f"Кількість від'ємних елементів: {negative_count}")
print(f"Кількість додатніх елементів: {positive_count}")
print(f"Кількість нулів: {zero_count}")
