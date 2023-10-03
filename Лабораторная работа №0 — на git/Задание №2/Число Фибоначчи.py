import time, tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
#оптимизация рекурсии
input = open('input.txt', 'r')
n=int(input.readline())
output = open('output.txt', 'w')
from functools import lru_cache
@lru_cache()
def calc_fib(n):
    if (n <= 1):
        return n
    return calc_fib(n - 1) + calc_fib(n - 2)
output.write(str(calc_fib(n)))
input.close()
output.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
tracemalloc.stop()


#решение без рекурсии
#n=int(input())
#n<=100
#f_1=0
#f_2=1
#for i in range(0,n):
    #f_1,f_2=f_2,f_1+f_2
    #print(f_1, end=' ')
