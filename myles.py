import random
from statistics import mean

throws = 1000  # rolling 100 times
results = []
resultsavg = []
for i in range(0, throws):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    die3 = random.randint(1, 6)
    a = [die1, die2, die3]
    b = sum(a)
    resultsavg.append(mean(results))

answer = mean(results)
print(f"The average is {answer}")