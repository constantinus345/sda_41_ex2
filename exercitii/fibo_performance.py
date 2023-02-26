from fibo import fibo_recursive, fibonaci_clasic
from time import perf_counter


numbers = [5,15,25,35,40]

for n in numbers:
    start_time = perf_counter()
    print(f"Fibo_recursive n={n} este {fibo_recursive(n)}")
    print(f"Fibo_recursive n={n} took {perf_counter()-start_time} seconds")
    print(f"{'_'*10}")
    
print(f"{'_'*50}")
for n in numbers:
    start_time = perf_counter()
    print(f"Fibo_clasic n={n} este {fibonaci_clasic(n)}")
    print(f"Fibo_clasic n={n} took {perf_counter()-start_time} seconds")