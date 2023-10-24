def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact    
    
print(factorial(3))    


def leap_yr(year):
    if year%100==0 and year%400==0:
        return True
    elif year%100!=0 and year%4==0:
        return True
    else:
        return False
print(leap_yr(2023))    
    