with open(day_1_aoc_2021_input.txt) as day1_file:
    measurements = [int(i) for i in (day1_file.readlines())]

measurement_increments = 0
window_increments = 0

for i in range(len(measurements) - 1):
    if measurements[i] < measurements[i+1]:
        measurement_increments+=1

for i in range(len(measurements) - 3):
    sum1 = measurements[i] + measurements[i+1] + measurements[i+2]
    sum2 = measurements[i+1] + measurements[i+2] + measurements[i+3]
    if sum1 < sum2:
        print(f"{sum1} < {sum2}")
        window_increments+=1


print(measurement_increments)
print(window_increments)
