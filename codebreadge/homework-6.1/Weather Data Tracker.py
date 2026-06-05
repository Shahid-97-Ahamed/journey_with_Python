# 3. Weather Data Tracker

cities = ['Tokyo', 'Osaka', 'Kyoto']
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']

weather = [
    [
        [18, 60, 120],
        [34, 80, 180],
        [22, 65, 140],
        [8, 50, 60]
    ],
    [
        [20, 62, 110],
        [36, 82, 170],
        [24, 64, 130],
        [9, 52, 55]
    ],
    [
        [19, 61, 105],
        [35, 79, 165],
        [23, 63, 125],
        [7, 51, 50]
    ]
]

highest_rainfall = 0
highest_rainfall_city = ""

print("=" * 42)
print("WEATHER REPORT")
print("=" * 42)

c = 0
while c < len(weather):

    print("City:", cities[c])

    hottest_temp = weather[c][0][0]
    hottest_season = seasons[0]

    total_rainfall = 0

    s = 0
    while s < len(weather[c]):

        temp = weather[c][s][0]
        humidity = weather[c][s][1]
        rainfall = weather[c][s][2]

        print(
            seasons[s],
            "| Temp:", str(temp) + "C",
            "Humidity:", str(humidity) + "%",
            "Rain:", str(rainfall) + "mm"
        )

        if temp > hottest_temp:
            hottest_temp = temp
            hottest_season = seasons[s]

        total_rainfall += rainfall

        s += 1

    print("Hottest season:", hottest_season, "(" + str(hottest_temp) + "C)")

    if total_rainfall > highest_rainfall:
        highest_rainfall = total_rainfall
        highest_rainfall_city = cities[c]

    c += 1

print("City with highest annual rainfall:", highest_rainfall_city, "(" + str(highest_rainfall) + "mm)")