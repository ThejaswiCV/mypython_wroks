years=[y for y in range(1800,2024)]
print(years)

# century
century=[y for y in years if y%100==0]
print(century)

# leap
leap_yr=[y for y in years if (y%100==0 and y%400==0)or(y%100!=0 and y%4==0)]
print(leap_yr)