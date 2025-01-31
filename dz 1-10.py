# Введення двох чисел
a = float(input("Введіть перше число (a): "))
b = float(input("Введіть друге число (b): "))

# Введення математичної операції
operation = input("Введіть математичну дію (+, -, *, /): ")

# Виконання обчислення
if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    if b == 0:
        result = "Ділення на нуль"
    else:
        result = a / b
else:
    result = "Невідома операція"

print(f"Результат: {result}")

