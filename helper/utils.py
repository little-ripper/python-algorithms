from time import perf_counter


def performance(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        end = perf_counter()
        string = f"""\
        Execution time for {func.__name__}_size_{str(kwargs.get("size"))}:\t{kwargs}:\t{end - start:.5f} [s]"""
        print(string)
    return wrapper
