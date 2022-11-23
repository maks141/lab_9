from random import randint
import logging

# Создание лог файла
logging.basicConfig(filename = "base_log.log", level=logging.INFO)

# Ввод 
while True:
    n = int(input('Введите N: '))
    logging.info(f'N: {n}')
    if n < 1:
        print('Введите положительное N, начиная от 1')
        continue
    break

while True:        
    k = int(input('Введите k: '))
    logging.info(f'k: {k}')
    if k < 1:
        print('Введите положительное k, начиная от 1')
        continue
    break

# Выбор случаного числа
secret_number = randint(1, n)
logging.info(f'Hidden number: {secret_number}')

# Попытки нахождения искомого числа 
win = False
for i in range(k):
    try_number = int(input(f'Какое число загадал компьютер? (Осталось попыток: {k-i}): '))
    logging.info(f'Try number: {try_number}')
    if try_number > secret_number:
        print('Меньше')
        logging.info('less')
    elif try_number < secret_number:
        print('Больше')
        logging.info('more')
    elif try_number == secret_number:
        print('Вы угадали!')
        logging.info('The user guessed the number')
        win = True
        break

# Проверка на исход игры
if not win:
    print('Попытки закончились')
