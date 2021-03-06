import datetime
from typing import Callable

def logger_factory(file):
    def logger(func=Callable):
        def new_func(*args, **kwargs):
            with open(file, 'w+', encoding='utf-8') as f:
                f.write(f'Дата и время: {datetime.datetime.now()}\n')
                f.write(f'Название функции: {func.__name__}\n')
                f.write(f'Аргументы функции: {args} и {kwargs}\n')
                f.write(f'Возращаемое значение: {func(*args, **kwargs)}\n')
            with open(file, 'r', encoding='utf-8') as file_read:
                result = file_read.read()
            return result
        return new_func
    return logger

@logger_factory('result1.txt')
def my_generator(file):
    with open(file , "rb") as f:
        content = f.readlines()
        for line in content:
            try:
                hash_object = hashlib.md5(line)
                yield hash_object.hexdigest()

            except:
                yield "Error"

if __name__ == '__main__':
    var = my_generator('result1.txt')
    print(var)