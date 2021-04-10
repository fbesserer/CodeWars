import time


def pos_average(s):
    # Werte werden alle gleich verglichen in dictionary gespeichert und über arithmetische folge berechnet
    # dadurch bleibt die durchlaufzeit linear, da x * n * 4, mit x = substringlänge und n = substring Anzahl und 4 = 4 mögliche Zahlen in substring
    counts = dict()
    duplicates = 0
    splits = s.split(", ")
    n = len(splits)
    for i in range(len(splits[0])):
        for entry in splits:
            counts[entry[i]] = counts.get(entry[i], 0) + 1
        for value in counts.values():
            duplicates += (value * (value - 1)) / 2
        counts.clear()

    word_length = len(splits[0])
    return duplicates / (n * (n - 1) / 2 * word_length) * 100

# alternative Möglichkeit
from statistics import mean
from itertools import combinations


def pos_average1(s):
    # Funktionsweise:
    # combinations erstellt eine Menge aller Kombinationen (keine Duplikate - Reihenfolge der Tuple egal)
    # zip(*combo) packt jede Stelle jeder Kombination in einem Tuple zum Vergleich zusammen
    # und a == b bestimmt ob Werte gleich (1) oder ungleich (0)
    # Die gesamte Anzahl aller 1 und 0 werden in einem Generator Object an die Funktion mean übergeben, die die daraus
    # generierten iterator Werte zusammenrechnet und durch die Gesamtzahl der Werte teilt.
    # quadratische Laufzeit
    return mean(a == b for combo in combinations(s.split(', '), 2) for a, b in zip(*combo)) * 100.


# assert_fuzzy = ("466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096")
assert_fuzzy = ("466960, " * 1000)[:-2]
time1 = time.perf_counter()
print(pos_average(assert_fuzzy))
time2 = time.perf_counter()
print(f"linear time: {time2 - time1}")

time1 = time.perf_counter()
print(pos_average1(assert_fuzzy))
time2 = time.perf_counter()
print(f"quadratic time: {time2 - time1}")

# assert_fuzzy1 = ("444996, 699990, 666690, 096904, 600644, 640646, 606469, 409694, 666094, 606490")
# print(pos_average(assert_fuzzy1))
# s1 = ("6900690040, 4690606946, 9990494604")
# print(pos_average(s1))
