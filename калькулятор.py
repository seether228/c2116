def safe_calculator(func):
    def wrapper(expression):
        try:
            
            result = func(expression)
            return result
        except SyntaxError:
            print("Помилка: Неправильний синтаксис у виразі.")
        except NameError:
            print("Помилка: Використано недопустимі імена.")
        except ZeroDivisionError:
            print("Помилка: Ділення на нуль.")
        except Exception as e:
            print(f"Сталася непередбачена помилка: {e}")

    return wrapper

@safe_calculator
def calculate(expression):
    return eval(expression)


print(calculate("10 / 2"))       
print(calculate("10 / 0"))       
print(calculate("10 + (5 * 2"))  
print(calculate("invalid_name"))  
