# 8. Sports Leaderboard Merger

region_a = [88, 74, 95, 61]
region_b = [79, 91, 85, 70]
region_a.extend(region_b) #both list now are together
# print(region_a)
region_a.sort(reverse=True) #this one is descending means big to small degit
print("All score: ",region_a)
top_scores =region_a[:3] #top three score
print("Top 3 finalists: ",top_scores)

status = 'A score above 90 made it to the podium!' if top_scores[0] > 90 else "No score above 90 this season"
print(status)