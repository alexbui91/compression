import math
# from regex_example import re_show, re_delete
from IntegerCodes import dec_to_bin, get_unary


verbose = 0
mGolombDefault = 5


def encode(string, m=mGolombDefault):
    ans = ""
    b = int(math.ceil(math.log(m, 2)))
    b_ = int(math.pow(2, b) - m)
    for s in string : ## run through the symbols
        q, r = s // m, s % m
        r_b = b
        if r < b_:
            r_b = b - 1
        else:
            r += b_ 
        c = get_unary(q) + dec_to_bin(r, r_b); 
        ans += c
    return ans


def test():
    arr = [2, 6, 9, 10, 27]
    b = encode(arr)


if __name__ == '__main__':
    test()