from math import sqrt, atan, pi


ax, ay, bx, by = map(int, input().split())
R = max(sqrt(ax**2 + ay**2), sqrt(bx**2 + by**2))
r = min(sqrt(ax**2 + ay**2), sqrt(bx**2 + by**2))
if not (ax or ay) or not (bx or by):
    print(max(r, R))
else:
    if ax:
        if not ay:
            a = -pi/2 * abs(ax) / ax + pi/2
        else:
            a = atan(ay/ax)
            if ax < 0:
                a += pi
    else:
        a = pi/2 * abs(ay) / ay
    if bx:
        if not by:
            b = -pi/2 * abs(bx) / bx + pi/2
        else:
            b = atan(by/bx)
            if bx < 0:
                b += pi
    else:
        b = pi/2 * abs(by) / by
    t = abs(a - b) % (2 * pi)
    if t > pi:
        t = 2 * pi - t
    print(min(r * t + R - r, r + R))
