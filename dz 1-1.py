name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
venom1 = f"Привет, {name}! Тебе {age} лет, доступ разрешен"
venom2 = f"Привет, {name}! Тебе {age} лет, доступ запрещен"
if age==18 or age > 18:
    print (venom1)
else:
    print (venom2)

