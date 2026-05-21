# 5. News Feed — Latest 3 Headlines
# Headlines list (oldest first)
headlines = [
    'weather update released',
    'sports team wins championship',
    'new ai law passed',
    'budget cuts announced',
    'school reform bill'
]


# headlines checking
if len(headlines) < 3:
    print("'Not enough news yet'.")
else:
# slice headlines from headlines
    recent =headlines[-3:]
# print(recent)
# count headlines from updated headlines list
    updated_headlines =len(recent)
    print("Total headlines: ",len(headlines)," | Showing: ",updated_headlines)
# headlines numbers and title case add in headlines list
    print("1",recent[0].title())
    print("2",recent[1].title())
    print("3",recent[2].title())