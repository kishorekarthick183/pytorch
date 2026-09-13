import functools
import time

def timer(func): 
    def wrapper(*args): 
        start_time = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - start_time
        print(f"[{func.__name__}] Executed in {elapsed:.6f} seconds")
        return result
    return wrapper

@timer
def compute_squares(n: int): 
    return [i**2 for i in range(n)]

compute_squares(1_000_000)
    