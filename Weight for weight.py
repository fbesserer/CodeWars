import time


def order_weight(strng):
    weights = strng.split(" ")
    weighted_weights = list()
    for weight in weights:
        count = 0
        for dig in weight:
            count += int(dig)
        #if count != 0:
        weighted_weights.append((weight, count))
    weighted_weights = [x[0] for x in sorted(weighted_weights, key=lambda x: (x[1], x[0]))]

    return " ".join(weighted_weights)

def order_weight1(_str):
    # die Sortierung zu Beginn gibt die Reihenfolge vor, sodass danach nur noch nach der Quersumme sortiert werden muss
    # und bei einem Draw automatisch der richtige Wert bereits vorne steht
    return " ".join(sorted(sorted(_str.split(" ")), key=lambda x: sum(int(c) for c in x)))


def sum_string(s):
    sum = 0
    for digit in s:
        sum += int(digit)
    return sum

def order_weight2(strng):
    # your code
    initial_list = sorted(strng.split())
    result = " ".join(sorted(initial_list, key=sum_string))

    return result

i = ("2000 22 10003 1234000 44444444 9999 11 11 22 123 ")
print(order_weight(i))
i = ("2000 22 10003 1234000 44444444 9999 11 11 22 123 ")
print(order_weight1(i))

i = ("2000 22 10003 1234000 44444444 9999 11 11 22 123 ") * 100000
time1 = time.perf_counter()
order_weight(i)
time2 = time.perf_counter()
print(f"time: {time2 - time1}")

i = ("2000 22 10003 1234000 44444444 9999 11 11 22 123 ") * 100000
time1 = time.perf_counter()
order_weight1(i)
time2 = time.perf_counter()
print(f"time: {time2 - time1}")

i = ("2000 22 10003 1234000 44444444 9999 11 11 22 123 ") * 100000
time1 = time.perf_counter()
order_weight2(i)
time2 = time.perf_counter()
print(f"time: {time2 - time1}")

# 3. Variante die schnellste, die lambda funktion inkl sum() scheint zeit zu kosten
# time: 1.9878708
# time: 1.6468062000000003
# time: 1.2961744000000004