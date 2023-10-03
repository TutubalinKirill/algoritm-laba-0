import time, tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

f = open("input.txt")
a, b = map(int, f.readline().split())
f.close()
res = str(a + b)
w = open("output.txt", 'w')
w.write(res)
w.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
tracemalloc.stop()

