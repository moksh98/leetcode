def rectangle_fit(rectangles, xy):
    x = min(xy)
    y = max(xy)
    for r in rectangles:
        rl = min(r)
        rw = max(r)
        if not ((rl <= x) and (rw <= y)):
            return False
    return True


print(rectangle_fit([[4, 2], [2, 3]], [3, 6]))