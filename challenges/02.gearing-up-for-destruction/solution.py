def formula(pegs):
    is_even = len(pegs) % 2 == 0
    rev = list(reversed(pegs))
    ans = rev[0] + rev[-1] * (-1 if is_even else 1)
    multiplier = -2
    for idx in range(1, len(rev) - 1):
        ans += multiplier * rev[idx]
        multiplier *= -1
    return [ans * 2, 3] if is_even else [ans * -2, 1]


def euclidean(a, b):
    x, y = a, b
    while b > 0:
        a, b = b, a % b
    return [int(x / a), int(y / a)]


def check_radius(r, ratio, pegs):
    if r < ratio:
        return False
    if len(pegs) < 2:
        return True
    r_next = pegs[1] - pegs[0] - r
    return check_radius(r_next, ratio, pegs[1:])


def solution(pegs):
    if len(pegs) < 2:
        return [-1, -1]
    a, b = formula(pegs)
    if a < b:
        return [-1, -1]
    if not check_radius(a, b, [peg * b for peg in pegs]):
        return [-1, -1]
    a, b = euclidean(a, b)
    return [a, b]
