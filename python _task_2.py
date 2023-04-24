# Python3 program for the above approach
import math


def isPossible(l, arr, n, k):
    used = 0
    for i in range(n):
        used += int((arr[i]) / l)
    return used <= k


def newList(l, arr):
    new = []
    for n in arr:
        if n > l:
            k = math.ceil(n / l)
            for r in range(k):
                g = n / k
                if r == k - 1:
                    new.append(math.ceil(g))
                else:
                    new.append(math.floor(g))
        else:
            new.append(n)
    return new


def distance(bankomats, n, k):
    low = 0
    high = 1e8
    while (high - low > 1e-6):
        mid = (low + high) / 2.0;
        if (isPossible(mid, bankomats, n, k)):
            high = mid
        else:
            low = mid
    return round(low, 2);


if __name__ == "__main__":
    arr = [53, 100, 180, 50, 60, 150];
    k = 3
    n = len(arr)
    l = distance(arr, n, k)
    print('Исходные растояния между банкоматами: ', arr)
    print('Новые растояния между банкоматами:    ', newList(l, arr))

    # This code is contributed by AnkThon
