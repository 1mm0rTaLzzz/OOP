scores = list(map(int, input().split()))
minScore = sum(scores) + (10 * int(scores[-1] > 20 and scores[8] == 10))

strike, maxScore = 0, 0
for item in scores[:-1]:
    maxScore += item * (1 + strike)
    strike = min(2, strike + 1) * int(item >= 10)
maxScore += min(scores[-1], 10) * (1 + strike)
maxScore += (min(10, (scores[-1] - 10)) * (1 + int(strike in [1, 2])) + max(scores[-1] - 20, 0)) * int(scores[-1] > 10)

print(minScore, maxScore)