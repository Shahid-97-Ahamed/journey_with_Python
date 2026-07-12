n =int(input())

scores =list(map(int,input().split()))
scores.sort(reverse=True)

for score in scores:
    if score !=scores[0]:
        print(score)
        break