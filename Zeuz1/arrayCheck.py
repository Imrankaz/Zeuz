print("You just need to find a target number from an array of integers. if target exists return the index otherwise return -1.")
nums = [-1,0,3,5,9,12]

index = 0
count = 0

while index < len(nums):
    if nums[index] == 9:
        print(index)
        count = count +1
    #else:
        #print(-1)

    index = index + 1

if count == 0:
    print(-1)

