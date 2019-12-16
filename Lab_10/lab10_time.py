import time

print(time.time())  # nr de secunde de la 01.01.1970, in float
# Ca sa masuram timpul de executie:
t1 = time.monotonic()
t2 = time.perf_counter()
s = 0
for i in range(1, 10000):
    s += i
tf1 = time.monotonic() - t1
tf2 = time.perf_counter() - t2
print(tf1)
print(tf2)
# time.perf_counter_ns()
time.sleep(3)
print("dormi Costi?")

print(time.process_time())  # timpul in secunde pe care l-a adunat programul curent pe procesor
