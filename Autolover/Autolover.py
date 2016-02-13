from datetime import datetime
stats_file = open('car_stats.csv')

rate = 184
spent_money = 0
first_line = True
total_volume = 0
total_km = 0
date_list = []


for record in stats_file:
    if first_line:
        first_line = False
        continue
    values = record.split(",")

    volume = values[2]
    if volume:
        total_volume += float(volume)

    km = values [1]
    if km:
        total_km += int(km)

    money = int(values[3])
    if values[5] == "RUR":
        money *= rate

    spent_money += money

    test_date = values[0]
    if test_date:
       test_date = datetime.strptime(values[0],'%m/%d/%Y')
       date_list.append(test_date)

earlier_date = max(date_list)
oldest_date = min(date_list)
months = (earlier_date - oldest_date).days / 30
month_spent = spent_money / months

average_fuel_spent = (total_volume / total_km) * 100

print ("Total amount of spent money is "  + str(spent_money) + " BYR.")
print ("Amount of spent fuel for 100 km is " + str(average_fuel_spent) +  " liter.")
print ("Amount of spent money per month is "  +  str(month_spent)  + " BYR.")