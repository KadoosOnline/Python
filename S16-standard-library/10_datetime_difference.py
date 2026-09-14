from datetime import date, timedelta

today = date.today()
birthday = date(2005, 3, 21)

# Subtracting two dates gives a timedelta.
age = today - birthday
print('Days lived:', age.days)
print('Approximate age:', age.days // 365)

# Adding a duration to a date.
print('In 100 days:', today + timedelta(days=100))
print('One week ago:', today - timedelta(weeks=1))

# A small program: how many days until the end of the year?
end_of_year = date(today.year, 12, 31)
print('Days left this year:', (end_of_year - today).days)
