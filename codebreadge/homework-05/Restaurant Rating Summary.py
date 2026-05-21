# 6. Restaurant Rating Summary
ratings = [3.8,4.5,2.9,4.8,4.1]
highest =max(ratings)
lowest = min(ratings)
highest_to_lowest =sorted(ratings,reverse=True)
# print(highest_to_lowest)
status = "Top restaurant qualifies for Featured badge!" if highest >= 4.5 else "No featured badge this week"
print("Highest: ",highest,"|","Lowest: ",lowest)
print("Ranked: ",highest_to_lowest)
print(status)
