n, a, d = map(int, input().split())

sounds = list(map(int, input().split()))

dan = 0
ap = a
for sound in sounds:
    if sound == a:
        dan += 1
        a += d

print(dan)
