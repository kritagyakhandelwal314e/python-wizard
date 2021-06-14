import datetime;
birth_year = int(input('What year did you born? '))
birth_month = int(input('What month ? '))

current_year = int(str(datetime.date.today())[:4])
current_month = int(str(datetime.date.today())[5:7])

age_years = current_year - birth_year
age_months = current_month - birth_month
if age_months < 0 :
    age_years -= 1
    age_months += 12

print(f'You are {age_years} years and {age_months} months old')