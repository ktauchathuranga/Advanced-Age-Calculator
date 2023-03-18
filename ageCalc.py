from datetime import datetime, timedelta


def calculate_age_and_duration(birth_date, end_date):
    age_delta = end_date - birth_date
    age_years = age_delta.days // 365
    age_months = age_delta.days % 365 // 30
    age_days = age_delta.days % 365 % 30

    total_months = (end_date.year - birth_date.year) * 12 + (end_date.month - birth_date.month)
    remaining_days = end_date.day - birth_date.day
    if remaining_days < 0:
        total_months -= 1
        remaining_days += (end_date - timedelta(days=remaining_days)).day
    total_weeks = age_delta.days // 7
    remaining_weeks = total_weeks % 52

    duration = end_date - birth_date
    seconds = duration.total_seconds()
    weeks = duration.days // 7
    days = duration.days % 7
    hours = seconds // 3600
    minutes = seconds // 60

    return age_years, age_months, age_days, total_months, remaining_days, total_weeks, remaining_weeks, weeks, days, hours, minutes, duration.days, seconds


birth_date_str = input("Enter your birth date (YYYY-MM-DD): ")
end_date_str = input("Enter an ending date (YYYY-MM-DD): ")

birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

age_years, age_months, age_days, total_months, remaining_days, total_weeks, remaining_weeks, weeks, days, hours, minutes, total_days, seconds = calculate_age_and_duration(
    birth_date, end_date)

print("Your age is: {} years, {} months, and {} days".format(age_years, age_months, age_days))
print("The duration between the two dates is:")
print("- {} seconds".format(seconds))
print("- {} months and {} days".format(total_months, remaining_days))
print("- {} weeks and {} days".format(total_weeks, remaining_weeks))
print("- {} days".format(total_days))
print("- {} hours".format(hours))
print("- {} minutes".format(minutes))
