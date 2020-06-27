import time


# Определим время выполнения с помощью декоратора
def time_this(NUM_RUNS):
    def decorator(other_func):
        def search_time(*args, **kwargs):
            avg_time = 0
            for i in range(NUM_RUNS):
                t0 = time.time()
                other_func(*args, **kwargs)
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time = avg_time/NUM_RUNS
            fn = other_func.__name__
            print("Среднее время выполнения, определенное с помощью декоратора функции %s за %s запусков: %.5f секунд" % (fn, NUM_RUNS, avg_time))
        return search_time
    return decorator


# Проверяемая функция
@time_this(100)
def fibonachi(up_limit):
    fibonachi_res=[1, 2]
    i=1
    while fibonachi_res[-1] < up_limit:
        a = fibonachi_res[i]+fibonachi_res[i-1]
        fibonachi_res.append(a)
        i+=1
    return(fibonachi_res[-2])

# Вызов проверяемой функции
fibonachi(10**1000)

# Определим время выполнения с помощью класса
class Time_this:
    def __init__(self, other_func):
        self.num_runs = 100
        self.other_func = other_func

    def __call__(self, *args, **kwargs):
        avg_time = 0
        for _ in range(self.num_runs):
            t0 = time.time()
            self.other_func(*args, **kwargs)
            t1 = time.time()
            avg_time += (t1 - t0)
        avg_time = avg_time/self.num_runs
        fn = self.other_func.__name__
        print(
            "Среднее время выполнения, определенное с помощью класса функции %s за %s запусков: %.5f секунд" % (
                fn,
                self.num_runs,
                avg_time
            )
        )
        return self.other_func(*args, **kwargs)

@Time_this
def fibonachi(up_limit):
    fibonachi_res=[1, 2]
    i=1
    while fibonachi_res[-1] < up_limit:
        a = fibonachi_res[i]+fibonachi_res[i-1]
        fibonachi_res.append(a)
        i+=1
    return(fibonachi_res[-2])

# Вызов проверяемой функции
fibonachi(10**1000)