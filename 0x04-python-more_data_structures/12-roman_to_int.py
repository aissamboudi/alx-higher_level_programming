#!/usr/bin/python3
def roman_to_int(r):
    a = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if not isinstance(r, str):
        return 0
    else:
        romans_v = []
        for i, x in enumerate(r):
            if a[x] >= a[r[(i+1) if i < len(r)-1 else i]]:
                romans_v.append(a[x])
            else:
                romans_v.append(-a[x])
                return sum(romans_v)
