sum=int(input("enter sum value"))
arr=[2,4,5,6,8]

# srt_arr=sorted(arr)
arr.sort()  #method in class list. internally sort the given array

low=0
upp=len(arr)-1

while(low<upp):
    curr_sum=arr[low]+arr[upp]
    
    if(curr_sum==sum):
        print("pairs",arr[low],arr[upp])
        low+=1
        upp-=1
        # break   #when we need only one pair
    elif(curr_sum<sum):
        low+=1
    elif(curr_sum>sum):
        upp-=1
        