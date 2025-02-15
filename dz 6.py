result = []

def divider(a, b):
    if a < b:
        raise ValueError("Перше число повинно бути більшим або рівним другому.")
    if b > 100:
        raise IndexError("Друге число не повинно перевищувати 100.")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (ValueError, IndexError, ZeroDivisionError, TypeError) as e:
        print(f"Виник виняток: {e}")

print(result)
