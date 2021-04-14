def order_weight(strng):
    weights = strng.strip().split(" ")
    weighted_weights = list()
    for weight in weights:
        count = 0
        for dig in weight:
            count += int(dig)
        if count != 0:
            weighted_weights.append((weight, count))
    weighted_weights = [x[0] for x in sorted(weighted_weights, key=lambda x: (x[1], x[0]))]

    return " ".join(weighted_weights)

def order_weight1(_str):
    _str.split(" ")



i = "    2000 22   10003 1234000   44444444 9999 11 11 22 123   "
print(order_weight(i))
"11 11 2000 10003 22 123 1234000 44444444 9999"