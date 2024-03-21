#!/usr/bin/python3
def roman_to_int(roman_string):
    a = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
    return sum([a[x] if a[x] >= a[roman_string[(i+1) if i < len(roman_string)-1 else i]] else -a[x]for i, x in enumerate(roman_string)])
