# Count the number of Sunday jack will get within n number of days.
# Example 1: Input mon-> input String denoting the start of the month.
# 13  -> input integer denoting the number of days from the start of the month.
# Output : 2    -> number of days within 13 days.
# Explanation:The month start with mon(Monday). So the upcoming sunday will arrive in next 6 days.
# And then next Sunday in next 7 days and so on.
# Now total number of days are 13. It means 6 days to first sunday and then remaining 7 days will
# end up in another sunday. Total 2 sundays may fall within 13 days.

def count_sundays (start_day, total_days):
    week = ["monday", "tuesday", "wednesday", "thrusday", "friday", "saturday", "sunday"] # Day in order
    start_index = week.index(start_day.lower())
    
    # Day to reach first sunday
    first_sunday = (6 - total_days) % 7
    # If sunday is the first day
    if first_sunday >= total_days:
        return 0
    result = total_days - (first_sunday + 1)
    sunday = 1 + (result  // 7)
    return sunday

start_day = input()
total_days = int(input())

print(count_sundays(start_day, total_days))
