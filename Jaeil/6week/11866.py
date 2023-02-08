def josephus(n, k):
    people = list(range(1, n + 1))
    index = k - 1
    result = []
    while people:
        result.append(str(people.pop(index)))
        if people:
            index = (index + k - 1) % len(people)
    return "<" + ", ".join(result) + ">"

N, K = map(int, input().split())
print(josephus(N, K))