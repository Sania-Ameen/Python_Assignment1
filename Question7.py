# the conversion function

# define the function
def conversion_of_seconds(seconds_since_midnight):
    # if there is an invalid input of seconds
    if seconds_since_midnight < 0 or seconds_since_midnight >= 86400:
        return "ERROR: PLEASE ENTER A VALID NUMBER FOR SECONDS"
    # consider for the hours

    # count the hours since midnight in accordance to the seconds
    hour_counter = seconds_since_midnight // 3600
    remaining_seconds_of_the_hour = seconds_since_midnight % 3600

    # count the minutes and seconds with the remaining amount of seconds entered
    minutes_after_last_hour = remaining_seconds_of_the_hour // 60
    seconds_after_last_minute = remaining_seconds_of_the_hour % 60

    # account for AM and PM
    if hour_counter < 12:
        period_of_time = "AM"
    else:
        period_of_time = "PM"

    # for the 12am case make it valid for the seconds to be 0
    hour_counter_for_12_hours = hour_counter % 12
    # if the hour counter is 0, it should be represented as 12 (am)
    if hour_counter_for_12_hours == 0:
        hour_counter_for_12_hours = 12

    # return the hour, minute, second and AM/PM as a string and allow the minutes and seconds to be 2 digits
    return(f"{hour_counter_for_12_hours}:{minutes_after_last_hour:02d}:{seconds_after_last_minute:02d} {period_of_time}")

print(conversion_of_seconds(0))
print(conversion_of_seconds(3661))
print(conversion_of_seconds(8))
print(conversion_of_seconds(86400))