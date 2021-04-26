def solution(n, words):
    used = set()
    used.add(words[0])
    for i in range(1, len(words)):
        person = i % n + 1
        nth = i // n + 1
        if words[i - 1][-1] != words[i][0]:
            return [person, nth]
        if words[i] in used:
            return [person, nth]
        used.add(words[i])
    return [0, 0]
