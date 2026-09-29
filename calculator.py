import math


def percentage(attended, total):
    if total == 0:
        return 0.0
    return attended / total * 100


def can_skip(attended, total, required):
    max_total = (attended * 100) // required
    return max(0, max_total - total)


def need_to_attend(attended, total, required):
    top = required * total - 100 * attended

    if top <= 0:
        return 0

    return math.ceil(top / (100 - required))