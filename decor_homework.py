# Доработать декоратор logger в коде ниже.
# Должен получиться декоратор, который записывает в файл 'main.log' дату и время вызова функции,
# имя функции, аргументы, с которыми вызвалась, и возвращаемое значение.
# Функция test_1 в коде ниже также должна отработать без ошибок. import os
from datetime import datetime
import os
def logger(old_function):
    def wrapper(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open('main.log', 'a') as file:
            file.write(f'date and time: {datetime.now()}\n\n')
            file.write(f'function name: {old_function.__name__}\n\n')
            file.write(f'arguments: {args}, {kwargs}\n\n')
            file.write(f'result: {result}\n\n')
            file.write('\n')
            file.write('*'*20 + '\n\n')
        return result
    return wrapper

def test_1():

    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"

    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()


def logger(path): #@logger(path='путь')
    def __logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(path, 'a') as file:
                file.write(f'date and time: {datetime.now()}\n\n')
                file.write(f'function name: {old_function.__name__}\n\n')
                file.write(f'arguments: {args}, {kwargs}\n\n')
                file.write(f'result: {result}\n\n')
                file.write('\n')
                file.write('*' * 20 + '\n\n')
            return result
        return new_function
    return __logger
def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'
if __name__ == '__main__':
    test_2()