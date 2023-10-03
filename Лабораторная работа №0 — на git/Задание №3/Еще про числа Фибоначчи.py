import time, tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

input = open('input.txt', 'r')
n=int(input.readline())
output = open('output.txt', 'w')


mas = [0,1]
for i in range(2, n+1):
    mas.append((mas[-1] + mas[-2]) % 10)


output.write(str(mas[n]))
input.close()
output.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
tracemalloc.stop()
