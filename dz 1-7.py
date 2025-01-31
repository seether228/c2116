# Введення числа n
n = int(input("Введіть число n: "))

# Виведення парних чисел у зворотному порядку
even_numbers = [str(i) for i in range(2, n + 1, 2)]
print(" ".join(even_numbers[::-1]))
