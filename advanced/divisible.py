#+ve num divisible by 3
lst=[0,1,2,3,6,9,-3,-12,0,-5]
div=[num  for num in lst if num>0 and num%3==0]
print(div)
