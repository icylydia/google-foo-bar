def solution(x, y):
    sx = set(x)
    sy = set(y)
    if len(sx) > len(sy):
        return sx.difference(sy).pop()
    else:
        return sy.difference(sx).pop()
