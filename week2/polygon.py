# -*- coding: utf-8 -*-
"""Assignment solution for Week 2 of edX MITx: 6.00.1x
"""

import math


def polysum(n: int, s: float) -> float:
    """Sums the area and square of the perimeter of the regular polygon.

    Args:
        n (int): Number of sides, larger than 3.
        s (float): Length of a side, larger than 0.0.

    Returns:
        float: Sum of the area and square of the perimeter rounded to 4 decimal spaces.

    Raises:
        ValueError: If n is smaller than 3 or if s is smaller or equal to 0.

    Examples:
        >>>print(polysum(5, 1.1))
        2.7615
    """

    if n < 3 or s <= 0.0:
        raise ValueError('')

    area = (0.25*(s**2)) / math.tan(math.pi/n)
    perimeter = n * s

    return area + (perimeter**2)
