from divide import divide


def psepnum(x):
def psepnum(x):
    B = 2
    A = 0
    while B > 1:
        A = A + 1
        B = divide(x, A)
        C = round(B)
        print(C)


psepnum(147)