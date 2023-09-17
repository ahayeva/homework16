x = int(input("Введіть перше число (x): "))
y = int(input("Введіть друге число (y): "))
result = x ** y
print(f"{x} у степені {y} = {result}")
#exercise2
count = 0
for num in range(100, 1000):
    digits = [int(digit) for digit in str(num)]
    if len(set(digits)) < 3:
        count += 1
print(f"Кількість чисел з двома однаковими цифрами від 100 до 999: {count}")
#exercise3
count = 0
for num in range(100, 10000):
    digits = [int(digit) for digit in str(num)]
    if len(set(digits)) == 4:
        count += 1
print(f"Кількість чисел з різними цифрами від 100 до 9999: {count}")
#exercise4
input_number = int(input("Введіть ціле число: "))
input_number_str = str(input_number)
result_str = "".join(char for char in input_number_str if char not in "36")
result_number = int(result_str)
print(f"Число після видалення цифр 3 і 6: {result_number}")
