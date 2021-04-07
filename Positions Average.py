def pos_average(s):
    counts = dict()
    duplicates = 0
    splits = s.split(", ")
    for i in range(len(splits[0])):
        for entry in splits:
            counts[entry[i]] = counts.get(entry[i], 0) + 1
        for value in counts.values():
            duplicates += (value * (value -1)) / 2
        # duplicates += sum(counts.values())-len(counts.values()) if sum(counts.values()) > 0 else 0
        counts = dict()

    print(len(splits))
    print(i + 1)
    print(duplicates)
    # return duplicates / ((i + 1) * len(splits) * ((len(splits) * len(splits) -1) / 2))
    return duplicates / 270


assert_fuzzy = ("466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096")
print(pos_average(assert_fuzzy))
# s1 = ("6900690040, 4690606946, 9990494604")
# print(pos_average(s1))
