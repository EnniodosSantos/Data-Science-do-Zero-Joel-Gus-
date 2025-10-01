from typing import List

def mean (xs: List[float]) -> float:
    return sum(xs) / len(xs)

def _median_odd(xs: List[float]) -> float:
    return sorted(xs)[len(xs)//2]

def _median_even(xs: List[float]) -> float:
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs)//2
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2

def median(v: List[float]) -> float:
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)

def quantile(xs: List[float], p: float) -> float:
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]

def mode(x: List[float]) -> List[float]:
    max_count = max(count.values())
    return [x_i for x_i, count in counts.items()
    if count == max_count]

def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)

from scratch.linear_algebra import sum_of_squares

def de_mean(xs: List[float]) -> List[float]:
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]

def variance(xs: List[float]) -> float:
    assert len(xs) >= 2
    n = len(xs)
    deviantions = de_mean(xs)
    return sum_of_squares(deviations) / (n - 1)

import math
def standard_deviation(xs: List[float]) -> float:
    return math.sqrt(variance(xs))