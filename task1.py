steps_input=input("Enter the number of steps taken each day in a month")
steps=list(map(int,steps_input.split()))
high=max(steps)
low=min(steps)
average=sum(steps)/len(steps)
sort=sorted(steps,reverse=True)
print("the highest step count : ",high)
print("the lowest step count : ",low)
print("the average : ",average)
print("sorted : ",sort)