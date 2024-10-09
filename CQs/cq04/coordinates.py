"""CQ04 Coordinates File"""

__author__ = "730580155"


def get_coords(xs: str, ys: str) -> None:
    idx_x = 0
    idx_y = 0
    while idx_x < len(xs):
        while idx_y < len(ys):
            print(xs[idx_x], ys[idx_y])
            idx_y += 1
        idx_x += 1
        idx_y = 0
