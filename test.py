import logging

# Настройка логирования с исключением миллисекунд
logging.basicConfig(filename='errors.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d.%m.%Y / %H:%M:%S')

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        # Логирование ошибки деления на ноль
        logging.error(f'Division by zero: {e}')
        return None

# Пример использования функции
result = divide(10, 0)

if result is not None:
    print(f"Result: {result}")
else:
    print("Error occurred. Check the log file for details.")
