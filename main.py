import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        time_result = round(end_time - start_time, 2)
        print(f"{func.__name__} run speed: {time_result} second/s")

    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
