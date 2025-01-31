# Введення кількості балів
points = int(input("Введіть кількість балів: "))

# Визначення оцінки
if 0 <= points < 50:
    grade = "незадовільно"
elif 50 <= points < 70:
    grade = "задовільно"
elif 70 <= points < 90:
    grade = "добре"
elif 90 <= points <= 100:
    grade = "відмінно"
else:
    grade = "неправильна кількість балів"

print(f"Оцінка: {grade}")
