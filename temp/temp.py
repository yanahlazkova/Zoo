import time
from _datetime import datetime


# логування викликів функцій
# def log_function(func):
#     def inner(num):
#         start_time = datetime.now().time().strftime("%H:%M:%S")
#         print('start_time: ', start_time)
#         rez = func(num)
#         end_time = datetime.now().time().strftime("%H:%M:%S")
#         print('end_time: ', end_time)
#         return rez
#     return inner
#
#
# @log_function
# def time_sleep(sec):
#     time.sleep(sec)
#     return sec
#
# time_sleep(10)
#
# time_sleep(5)


# кешування результатів функції

# def cache_results(func):
#     cache_dict = {}
#     def wrapper(*args):
#         if args in cache_dict:
#             print(cache_dict)
#             print('число з кешу')
#             return cache_dict[args]
#         else:
#             cache_dict[args] = func(*args)
#             return cache_dict[args]
#     return wrapper
#
#
# @cache_results
# def power(num, exp):
#     return num ** exp
#
# print(power(2, 3))
# print(power(5, 2))
# print(power(3, 3))
# print(power(2, 3))

# Обмеження кількості викликів функції
# (наприклад, не більше 3 викликів за певний період часу).

def limit_call(func):
    counter = 0
    start_time = time.time()

    def wrapper(sec):
        nonlocal counter
        end_time = time.time()
        period_time = end_time - start_time
        if counter < 3:
            if period_time <= 10:
                counter += 1
                print('виклик функції', counter)
                res = func(sec)
                return res
        else:
            print(f'час вийшов (зроблено {counter} викликів фукнції за {period_time} сек.)')
            return
            # exit()
    return wrapper


@limit_call
def time_sleep(sec):
    time.sleep(sec)
    return sec


for i in range(5):
    time_sleep(i + 3)
