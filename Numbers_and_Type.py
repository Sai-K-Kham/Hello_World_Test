seconds_per_minute = 60
minutes_per_hour = 60
hours_per_day = 24
def main():
    seconds_per_hour = seconds_per_minute * minutes_per_hour
    seconds_per_day = seconds_per_hour * hours_per_day

    divided = seconds_per_day / seconds_per_hour
    remainder = seconds_per_day // seconds_per_hour
    print(f"Seonds per hour is: {seconds_per_hour} Seconds per day is: {seconds_per_day} Division is {divided} Remainder is {remainder}")

main()

#git push second attemp