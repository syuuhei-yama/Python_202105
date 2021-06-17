#もっとも多く出現する文字をカウントする
from collections import Counter
import operator
from typing import Tuple

def count_chars_v1(strings : str) -> Tuple[str, int]:
    strings = strings.lower()
    # l = []
    # for cher in strings:
    #     if not cher.isspace():  #メソッドisspace -＞ スペースをカウントしない
    #         l.append((cher, strings.count(cher)))
    l = [(c, strings.count(c)) for c in strings if not c.isspace()]

    return max(l, key=operator.itemgetter(1))

def count_chars_v2(strings : str) -> Tuple[str, int]:
    strings = strings.lower()
    d = {}
    for cher in strings:
        if not cher.isspace():
            d[cher] = d.get(cher, 0) + 1
    max_key = max(d, key=d.get)
    return max_key, d[max_key]


def count_chars_v3(strings : str) -> Tuple[str, int]:
    strings = strings.lower()
    d = Counter()
    for cher in strings:
        if not cher.isspace():
            d[cher] += 1
    max_key = max(d, key=d.get)
    return max_key, d[max_key]




if __name__ == "__main__":
    s = "This is a pen. This is an apple. Applepen"
    print(count_chars_v3(s))
