year = 2100
#if year is a century year it must be divisible by 400
#i fyear is not century year it must be divisble by 4

if (year%100==0 and year%400==0):
    print(f"{year}is leap year")
elif(year%100!=0 and year%4==0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not a leap year")