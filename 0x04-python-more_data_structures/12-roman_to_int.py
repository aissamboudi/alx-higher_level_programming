#!/usr/bin/python3
def roman_to_int(roman_string):
    r = roman_string

    a = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if not isinstance(r, str):
        return 0
    else:
        romans_v = []
        for i, x in enumerate(r):
            num = 0
            if i < len(r) - 1:
                num = i + 1
            else:
                num = i
            if a[x] >= a[r[num]]:
                romans_v.append(a[x])
            else:
                romans_v.append(-a[x])
        return sum(romans_v)
