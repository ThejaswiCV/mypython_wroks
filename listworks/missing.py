lst=[1,2,3,4,632]

max_lst=max(lst)
total_sum=max_lst*(max_lst+1)/2
curr_sum=sum(lst)

diff=total_sum-curr_sum

if (diff==0):
    print(max_lst+1,"is the least +ve missing number")
    
else:
    print(diff,"is the missing number")