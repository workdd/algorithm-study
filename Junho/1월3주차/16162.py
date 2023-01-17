N, A, D = map(int, input().split())

pitchList = list(map(int, input().split()))

X = 0
nextPitch = A + D

for pitch in pitchList:
    if nextPitch == (pitch + D):
        X += 1
        nextPitch += D

print(X)
