from itertools import combinations
import time

def choose_best_sum(t, k, ls):
    highest = 0
    for entry in combinations(ls, k):
        cur_sum = sum(entry)
        if highest < cur_sum < t:
            highest = cur_sum
        elif cur_sum == t:
            return cur_sum
    # return None if highest == 0 else highest
    return highest or None

def choose_best(t,k,ls):
    # es werden im Gegensatz zu den anderen Lösungen nicht die Summe aller Kombinationen erst berechnet und dann verglichen
    # sondern die Summe wird laufend berechnet, sodass alle weiteren Kombinationen übersprungen werden, wenn bereits
    # ersichtlich ist, zB nach 2 Zahlen, dass die Summe bereits zu groß ist.
    # Dadurch werden Berechnungen gespart, und der Code ist effizienter
    if k == 0: return 0
    best = -1
    for i, v in enumerate(ls):
        if v > t: continue
        b = choose_best(t - v, k - 1, ls[i+1:])
        if b < 0: continue
        b += v
        if b > best and b <= t:
            best = b
    return best

def choose_best_sum2(t, k, ls):
    c = choose_best(t,k,ls)
    if c <= 0 : return None
    return c

def choose_best_sum1(t, k, ls):
    # wenn alle summen > t, dann ist das generator object leer und max gibt default wert aus
    return max((sum(v) for v in combinations(ls,k) if sum(v)<=t), default=None)


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
# print(choose_best_sum(230, 4, xs))  # TC 1 --> 230
# print(choose_best_sum(430, 5, xs))
# print(choose_best_sum(430, 8, xs))  # TC 3 --> None

# TC 1
time1 = time.perf_counter()
choose_best_sum(230, 4, xs)
time2 = time.perf_counter()
print(f"time: {time2 - time1}")

time1 = time.perf_counter()
choose_best_sum1(230, 4, xs)
time2 = time.perf_counter()
print(f"time: {time2 - time1}")

time1 = time.perf_counter()
choose_best_sum2(230, 4, xs)
time2 = time.perf_counter()
print(f"time: {time2 - time1}")

# TC 3
time1 = time.perf_counter()
choose_best_sum(430, 8, xs)
time2 = time.perf_counter()
print(f"time: {time2 - time1}")

time1 = time.perf_counter()
choose_best_sum1(430, 8, xs)
time2 = time.perf_counter()
print(f"time: {time2 - time1}")

time1 = time.perf_counter()
choose_best_sum2(430, 8, xs)
time2 = time.perf_counter()
print(f"time: {time2 - time1}")