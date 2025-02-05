import random

class Encryptor:
    def __init__(self, *numbers):
        self._numbers = numbers
        self._result = self._encrypt()

    def _encrypt(self):
        operation = random.choice(['+', '-', '*', '/'])
        result = self._numbers[0]
        for num in self._numbers[1:]:
            if operation == '+':
                result += num
            elif operation == '-':
                result -= num
            elif operation == '*':
                result *= num
            elif operation == '/':
                result /= num if num != 0 else 1
        return result

    def __str__(self):
        return f"Encrypted result: {self._result}"

encryptor = Encryptor(10, 5, 2)
print(encryptor)
