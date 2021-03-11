def check_cipher(X):
    result = []
    if X < 10000 and X >= 1000:
        cipher = [1000, 100, 10, 1]
        temp = 0
        for c in cipher:
            temp = X / c
            temp = int(temp)
            result.append(temp)
            X = X - (temp * c)
    else:
        print("done")
    for r in range(0,len(result)):
        print(result[r])
    return result

check_cipher(2523)